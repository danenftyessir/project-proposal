"""PreToolUse guard for the 13-agent orchestration (docs/ORCHESTRATION_ARCHITECTURE.md §7.2 E4, §8.3).

Reads the hook payload on stdin and the policy in .claude/policy/write_scopes.json. A denial is exit code 2
with the reason on stderr; Claude Code feeds that reason back to the agent. Everything else exits 0.

Who is checked how:
- roster agents (agent_type = a01..a13): global rules + their own write scope, Bash allowlist, read limits.
- the main session and non-roster agent types: global rules only (RSIA originals, dangerous Git, staging).
Errors inside the guard fail closed for roster agents and fail open for everyone else.
"""
import json, os, posixpath, re, shlex, sys
from _common import (CASE_INSENSITIVE, ROOT, RUNS_LOG, SKILLS_DIR, any_match, append_jsonl, load_policy, now_iso,
                     path_matches, short_hash, to_rel)

SEPARATORS = {"&&", "||", ";", "|", "&", "|&"}
REDIRECTS = {">", ">>", "&>", ">|"}
WRITE_VERBS = {"rm", "rmdir", "mv", "touch", "chmod", "chown", "icacls", "attrib", "truncate", "dd", "ln",
               "shred", "del", "rename", "mkdir", "tee"}
PY = {"python", "python3", "py"}
GIT_GLOBAL_OPTS_WITH_ARG = {"-C", "-c", "--git-dir", "--work-tree"}
# D-20 (TSK-014): mkdir/cp only for agents with bash_dest; skill scripts only for agents with skill_scripts.
DEST_VERBS = {"mkdir", "cp"}
MKDIR_OPTS = {"-p", "-v", "--parents", "--verbose"}
CP_SHORT = set("rRfvnp")       # no -a/-d/-P (copy links as links), -l/-s (create links), -L/-H, -t/-T (target)
CP_LONG = {"--recursive", "--force", "--verbose", "--no-clobber"}
CP_RECURSIVE = {"-r", "-R", "--recursive"}
SHELL_EXPANSION = set("${}~")
GLOB_CHARS = set("*?[]")
WALK_LIMIT = 2000
# Argument roles of the user-level skill scripts, taken from the scripts' own argparse/argv handling (5 Nov 2026).
# validate.py writes only through --auto-repair, which is never allowed; without it, packed input is extracted to
# the system temp directory. unpack.py and convert_pdf_to_images.py write into their output directory.
# Options are matched exactly, so argparse abbreviations such as --auto are refused.
SKILL_SPECS = {
    "docx/scripts/office/validate.py": {"pos": ["input"], "flags": {"-v", "--verbose"},
                                        "opts": {"--original": "input", "--author": "text"}},
    "docx/scripts/office/unpack.py": {"pos": ["input", "output"], "flags": set(),
                                      "opts": {"--merge-runs": "bool", "--simplify-redlines": "bool"}},
    "pdf/scripts/convert_pdf_to_images.py": {"pos": ["input", "output"], "flags": set(), "opts": {}},
}
_isjunction = getattr(os.path, "isjunction", lambda p: False)


class Deny(Exception):
    pass


def norm_cmd(word):
    base = os.path.basename(word.replace("\\", "/")).lower()
    base = base[:-4] if base.endswith(".exe") else base
    return "python" if base in PY else base


def segments(command):
    """Split a shell command into simple-command segments: [(words, redirect_targets)]."""
    out = []
    for line in command.splitlines():
        lex = shlex.shlex(line, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        lex.commenters = ""
        words, targets, expect_target = [], [], False
        for tok in lex:
            if tok in SEPARATORS:
                if words or targets:
                    out.append((words, targets))
                words, targets, expect_target = [], [], False
            elif tok in REDIRECTS:
                expect_target = True
            elif expect_target:
                targets.append(tok)
                expect_target = False
            elif tok in {"(", ")", "<"}:
                continue
            else:
                words.append(tok)
        if words or targets:
            out.append((words, targets))
    cleaned = []
    for words, targets in out:
        while words and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", words[0]):
            words = words[1:]
        if words and words[-1].isdigit() and targets:   # "2>" splits into "2" + ">"
            words = words[:-1]
        cleaned.append((words, targets))
    return cleaned


def git_parts(words):
    """('sub', rest) for a git command with global options removed, else (None, [])."""
    if not words or norm_cmd(words[0]) != "git":
        return None, []
    i = 1
    while i < len(words) and words[i].startswith("-"):
        i += 2 if words[i] in GIT_GLOBAL_OPTS_WITH_ARG else 1
    return (words[i], words[i + 1:]) if i < len(words) else (None, [])


def mentions(words, targets, needle):
    n = needle.lower()
    return any(n in w.replace("\\", "/").lower() for w in list(words) + list(targets))


def check_git(words, policy, actor):
    sub, rest = git_parts(words)
    if sub is None:
        return
    for pat in policy["global"]["deny_bash_patterns"]:
        ptoks = pat.split()
        if ptoks[0] != "git" or len(ptoks) < 2 or ptoks[1] != sub:
            continue
        need = ptoks[2:]
        if all((t == "+" and any(r.startswith("+") for r in rest)) or t in rest for t in need):
            raise Deny(f"perintah Git '{pat}' dilarang (§A-15.4)")
    if sub == "add":
        paths = [r for r in rest if not r.startswith("-")]
        for p in paths:
            if any(ch in p for ch in "*?[") or p in {".", "./", ":/"}:
                raise Deny("git add harus menyebut path eksplisit tanpa wildcard (§A-15.4)")
            rel = to_rel(p)
            if rel is not None and any_match(rel, policy["global"]["deny_stage_paths"]):
                raise Deny(f"path '{p}' tidak boleh di-stage (R-5, D-11)")


def check_protected_bash(words, targets, policy):
    protect = policy["global"]["protect_paths"]
    for t in targets:
        if any_match(to_rel(t), protect):
            raise Deny("redirection ke RSIA-source/ dilarang; berkas asli tidak boleh diubah (R-2)")
    if not mentions(words, targets, "rsia-source"):
        return
    if not words:
        return
    verb = norm_cmd(words[0])
    args = words[1:]
    if verb in WRITE_VERBS:
        raise Deny(f"'{verb}' pada RSIA-source/ dilarang; berkas asli tidak boleh diubah, dipindah, atau dihapus (R-2)")
    if verb in {"cp", "rsync", "install"} and args and "rsia-source" in args[-1].replace("\\", "/").lower():
        raise Deny("menyalin ke dalam RSIA-source/ dilarang (R-2)")
    if verb == "sed" and any(a == "-i" or a.startswith("-i") or a.startswith("--in-place") for a in args):
        raise Deny("sed -i pada RSIA-source/ dilarang (R-2)")
    if verb == "unzip":
        if "-l" in args or "-p" in args or "-Z" in args:
            return
        if "-d" in args:
            i = args.index("-d")
            dest = to_rel(args[i + 1]) if i + 1 < len(args) else None
            if dest is not None and path_matches(dest, ".scratch/rsia/**"):
                return
        raise Deny("unzip arsip RSIA hanya boleh -l, -p, atau -d .scratch/rsia/ (R-2, R-3)")
    if verb in {"7z", "tar"}:
        raise Deny(f"'{verb}' pada RSIA-source/ dilarang; gunakan unzip -l/-p/-d .scratch/rsia/ (R-2)")
    if verb == "git":
        sub, _ = git_parts(words)
        if sub in {"add", "rm", "mv", "checkout", "restore"}:
            raise Deny(f"git {sub} pada RSIA-source/ dilarang (R-2, R-5)")


def fold(p):
    return p.lower() if CASE_INSENSITIVE else p


def has_link(absp):
    """True if absp or any of its parents inside the repository is a symbolic link or junction."""
    root = os.path.normcase(os.path.normpath(str(ROOT)))
    p = os.path.normpath(absp)
    while len(os.path.normcase(p)) > len(root) and os.path.normcase(p).startswith(root):
        if os.path.islink(p) or _isjunction(p):
            return True
        p = os.path.dirname(p)
    return False


def repo_path(p, cwd, what):
    """(lexical rel, canonical rel, absolute path) of a path that must be explicit, inside the repo, link-free."""
    if any(ch in GLOB_CHARS for ch in p):
        raise Deny(f"{what} '{p}' tidak boleh memuat wildcard/glob (D-20)")
    rel = to_rel(p, cwd)
    if rel is None:
        raise Deny(f"{what} '{p}' berada di luar repository (D-20)")
    absp = os.path.normpath(os.path.join(str(ROOT), rel))
    if has_link(absp):
        raise Deny(f"{what} '{p}' melewati symbolic link atau junction (D-20)")
    try:
        real = os.path.relpath(os.path.realpath(absp), os.path.realpath(str(ROOT))).replace("\\", "/")
    except ValueError:
        real = "../"
    if real == ".":
        real = ""
    if real.startswith("../") or real == "..":
        raise Deny(f"{what} '{p}' berada di luar repository setelah resolusi path (D-20)")
    return rel, real, absp


def read_blocked(policy, agent):
    """Paths an agent's Bash write helpers may not take as input: RSIA originals and restricted-read paths."""
    g = policy["global"]
    pats = list(g["protect_paths"]) + list(g.get("audit_read_paths", []))
    return pats + [p for p, allowed in g.get("restricted_read", {}).items() if agent not in allowed]


def write_blocked(policy):
    g = policy["global"]
    return list(g["protect_paths"]) + list(g["deny_write_paths"])


def pattern_base(pat):
    parts = []
    for seg in pat.strip("/").split("/"):
        if any(ch in GLOB_CHARS for ch in seg):
            break
        parts.append(seg)
    return "/".join(parts)


def touches(rel, pats):
    """rel matches a pattern, or rel is the repo root / an ancestor of a pattern's fixed base."""
    if any_match(rel, pats):
        return True
    r = fold(rel)
    for pat in pats:
        b = fold(pattern_base(pat))
        if b and (r == "" or b == r or b.startswith(r + "/")):
            return True
    return False


def check_output(p, scope, policy, cwd, what):
    """Destination/output path: inside scope (bash_dest), not protected, not deny_write_paths, link-free."""
    rel, real, absp = repo_path(p, cwd, what)
    for r in {rel, real}:
        if not any_match(r, scope):
            raise Deny(f"{what} '{p}' di luar bash_dest ({', '.join(scope)}; D-20)")
        if any_match(r, write_blocked(policy)):
            raise Deny(f"{what} '{p}' termasuk path yang tidak boleh ditulis (deny_write_paths/protect_paths)")
    return rel, absp


def check_input(p, scope, policy, agent, cwd, what):
    """Input path: explicit, inside the repo, link-free, not RSIA/restricted; directories only from scope."""
    rel, real, absp = repo_path(p, cwd, what)
    if "rsia-source" in p.replace("\\", "/").lower() or any(touches(r, read_blocked(policy, agent)) for r in {rel, real}):
        raise Deny(f"{what} '{p}' adalah, berada di, atau memuat path terlindungi/terbatas (D-20, R-2, P2-03)")
    if os.path.isdir(absp) and not all(any_match(r, scope) for r in {rel, real}):
        raise Deny(f"{what} berupa direktori hanya boleh dari bash_dest ({', '.join(scope)}; D-20)")
    return rel, real, absp


def check_cp(pos, recursive, scope, policy, agent, cwd):
    srcs, dest = pos[:-1], pos[-1]
    drel, dabs = check_output(dest, scope, policy, cwd, "tujuan cp")
    dest_is_dir = os.path.isdir(dabs) or dest.endswith(("/", "\\")) or len(srcs) > 1
    src_blocked = read_blocked(policy, agent) + list(policy["global"]["deny_write_paths"])
    for s in srcs:
        srel, sreal, sabs = repo_path(s, cwd, "sumber cp")
        if "rsia-source" in s.replace("\\", "/").lower() or any(touches(r, src_blocked) for r in {srel, sreal}):
            raise Deny(f"sumber cp '{s}' adalah, berada di, atau memuat path terlindungi/terbatas (D-20)")
        base = posixpath.join(drel, posixpath.basename(srel)) if dest_is_dir else drel
        targets = [base]
        if os.path.isdir(sabs):
            if not recursive:
                continue                                 # cp refuses a directory without -r
            n = 0
            for dirpath, dirnames, filenames in os.walk(sabs, followlinks=False):
                for name in dirnames + filenames:
                    e = os.path.join(dirpath, name)
                    n += 1
                    if n > WALK_LIMIT:
                        raise Deny(f"sumber cp '{s}' memuat lebih dari {WALK_LIMIT} entri (D-20)")
                    if os.path.islink(e) or _isjunction(e):
                        raise Deny(f"sumber cp '{s}' memuat symbolic link atau junction (D-20)")
                    erel = to_rel(e)
                    if erel is None or any_match(erel, src_blocked):
                        raise Deny(f"sumber cp '{s}' memuat path terlindungi/terbatas (D-20)")
                    targets.append(posixpath.join(base, posixpath.relpath(erel, srel)))
        for t in targets:
            if not any_match(t, scope) or any_match(t, write_blocked(policy)) or \
                    has_link(os.path.join(str(ROOT), t)):
                raise Deny(f"hasil salinan '{t}' di luar bash_dest atau termasuk path yang tidak boleh ditulis "
                           "(mis. **/*.docx; D-20)")


def check_dest_bash(words, cfg, policy, agent, has_cd, cwd):
    """D-20: mkdir/cp only into bash_dest, with known-safe options and no shell expansion in arguments."""
    verb = norm_cmd(words[0])
    scope = cfg.get("bash_dest")
    if not scope:
        raise Deny(f"'{verb}' memerlukan bash_dest di kebijakan {agent} (D-20)")
    if has_cd:
        raise Deny(f"'{verb}' tidak boleh digabung dengan cd; jalankan dengan path relatif terhadap root repository (D-20)")
    opts, pos, end = [], [], False
    for w in words[1:]:
        if any(ch in SHELL_EXPANSION for ch in w):
            raise Deny(f"argumen {verb} tidak boleh memuat $, ~, atau kurung kurawal (D-20)")
        if not end and w == "--":
            end = True
        elif not end and w.startswith("-") and w != "-":
            opts.append(w)
        else:
            pos.append(w)
    for o in opts:
        good = o in MKDIR_OPTS if verb == "mkdir" else \
            (o in CP_LONG or (not o.startswith("--") and len(o) > 1 and set(o[1:]) <= CP_SHORT))
        if not good:
            raise Deny(f"opsi '{o}' untuk {verb} tidak diizinkan bagi {agent} (D-20)")
    if verb == "cp":
        if len(pos) < 2:
            raise Deny("cp memerlukan sumber dan tujuan eksplisit (D-20)")
        recursive = any(o in CP_RECURSIVE or (not o.startswith("--") and set(o[1:]) & {"r", "R"}) for o in opts)
        check_cp(pos, recursive, scope, policy, agent, cwd)
        return
    if not pos:
        raise Deny("mkdir memerlukan path tujuan eksplisit (D-20)")
    for d in pos:
        check_output(d, scope, policy, cwd, "path mkdir")


def skill_script(words, cwd):
    """Folded path of a user-level skill script relative to SKILLS_DIR when the command is `python <it>`."""
    if len(words) < 2 or norm_cmd(words[0]) != "python" or not SKILLS_DIR:
        return None
    p = words[1]
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)
    if m and os.name == "nt":
        p = f"{m.group(1)}:/{m.group(2)}"
    p = p.replace("\\", "/")
    if not os.path.isabs(p):
        p = os.path.join(cwd or str(ROOT), p)
    a, sk = os.path.normcase(os.path.normpath(p)), os.path.normcase(os.path.normpath(SKILLS_DIR))
    if not a.startswith(sk + os.sep):
        return None
    return fold(a[len(sk) + 1:].replace("\\", "/"))


def check_skill(words, script, cfg, policy, agent, cwd):
    """D-20: only agents with skill_scripts; inputs readable and explicit, outputs inside bash_dest."""
    allowed = {fold(s) for s in cfg.get("skill_scripts", [])}
    spec = SKILL_SPECS.get(script)
    if script not in allowed or spec is None:
        raise Deny(f"skrip skill '{script}' tidak diizinkan untuk {agent}; D-20 hanya mengizinkan a12 "
                   "menjalankan validate.py dan unpack.py")
    scope = cfg.get("bash_dest")
    if not scope:
        raise Deny(f"skrip skill memerlukan bash_dest di kebijakan {agent} (D-20)")
    args, pos, end, i = words[2:], [], False, 0

    def value(kind, v):
        if any(ch in SHELL_EXPANSION or ch in GLOB_CHARS for ch in v):
            raise Deny("argumen skrip skill tidak boleh memuat $, ~, kurung kurawal, atau wildcard (D-20)")
        if kind == "input":
            check_input(v, scope, policy, agent, cwd, "input skrip skill")
        elif kind == "output":
            check_output(v, scope, policy, cwd, "output skrip skill")
        elif kind == "bool" and v.lower() not in {"true", "false"}:
            raise Deny(f"nilai '{v}' harus true atau false (D-20)")
        elif kind == "text" and (not v or v.startswith("-")):
            raise Deny("nilai teks skrip skill tidak valid (D-20)")

    while i < len(args):
        w = args[i]
        if not end and w == "--":
            end = True
        elif not end and w.startswith("-") and w != "-":
            name, eq, val = w.partition("=")
            if script.endswith("validate.py") and len(name) >= 3 and "--auto-repair".startswith(name):
                raise Deny("validate.py --auto-repair menulis ke berkas yang divalidasi; selalu ditolak (D-20)")
            if name in spec["flags"] and not eq:
                pass
            elif name in spec["opts"]:
                if not eq:
                    if i + 1 >= len(args):
                        raise Deny(f"opsi '{name}' memerlukan nilai (D-20)")
                    i += 1
                    val = args[i]
                value(spec["opts"][name], val)
            else:
                raise Deny(f"opsi '{w}' tidak diizinkan untuk skrip skill {script} (D-20)")
        else:
            pos.append(w)
        i += 1
    if len(pos) != len(spec["pos"]):
        raise Deny(f"{script} memerlukan tepat {len(spec['pos'])} argumen posisi ({', '.join(spec['pos'])}; D-20)")
    for kind, v in zip(spec["pos"], pos):
        value(kind, v)


def check_agent_bash(words, targets, cfg, policy, agent, has_cd=False, cwd=None):
    raw = " ".join(words)
    if "$(" in raw or "`" in raw:
        raise Deny("substitusi perintah ($(...) atau backtick) tidak diizinkan untuk agent")
    if not words:
        return
    norm = [norm_cmd(words[0])] + words[1:]
    ok = False
    script = skill_script(words, cwd)
    if script is not None:                             # skill scripts never go through prefix matching
        check_skill(words, script, cfg, policy, agent, cwd)
        ok = True
    elif cfg.get("bash") and norm[0] in set(policy["global"].get("safe_bash", [])):
        if norm[0] == "cd" and len(words) > 1 and to_rel(words[1]) is None:
            raise Deny(f"cd ke luar repository tidak diizinkan untuk {agent}")
        ok = True
    for prefix in ([] if ok else cfg.get("bash", [])):
        ptoks = prefix.split()
        ptoks = [norm_cmd(ptoks[0])] + ptoks[1:]
        if len(norm) < len(ptoks):
            continue
        head, last = ptoks[:-1], ptoks[-1]
        if len(ptoks) == 1 and last in DEST_VERBS and norm[0] != last:
            continue                                   # 'cp' must not admit 'cpio', 'mkdir' not 'mkdirhier'
        if all(a.replace("\\", "/") == b for a, b in zip(norm, head)) and \
                norm[len(ptoks) - 1].replace("\\", "/").startswith(last):
            ok = True
            break
    if not ok:
        shown = " ".join(norm[:2]) if norm[0] == "git" and len(norm) > 1 else norm[0]
        hint = "; untuk hash gunakan sha256sum" if norm[0] == "python" and "-c" in norm[1:2] else ""
        raise Deny(f"perintah '{shown}' di luar allowlist Bash {agent} (A-7.2, .claude/policy/write_scopes.json){hint}")
    if norm[0] in DEST_VERBS:
        check_dest_bash(words, cfg, policy, agent, has_cd, cwd)
    if norm[0] == "git":
        sub, rest = git_parts(words)
        if sub == "hash-object" and any(r == "-w" or (r.startswith("-") and not r.startswith("--") and "w" in r[1:])
                                        for r in rest):
            raise Deny("git hash-object -w menulis objek ke .git; agent hanya boleh mode read-only (D-20)")
    for t in targets:
        rel = to_rel(t)
        if t in {"/dev/null", "nul", "NUL"}:
            continue
        if rel is None or not any_match(rel, cfg.get("write", [])):
            raise Deny(f"redirection ke '{t}' di luar scope tulis {agent}")
    if norm[0] == "pdftotext":
        pos = [w for w in words[1:] if not w.startswith("-") and not re.fullmatch(r"\d+", w)]
        if len(pos) >= 2 and pos[-1] != "-":
            rel = to_rel(pos[-1])
            if rel is None or not any_match(rel, cfg.get("write", [])):
                raise Deny(f"keluaran pdftotext '{pos[-1]}' di luar scope tulis {agent}")
    for path_pat, allowed in policy["global"].get("restricted_read", {}).items():
        base = path_pat.split("/")[0].lower() + "/"
        if agent not in allowed and mentions(words, targets, base):
            raise Deny(f"akses '{path_pat}' hanya untuk {', '.join(allowed)} (P2-03)")


def check_bash(command, policy, agent, cfg, cwd=None):
    for pat in policy["global"]["deny_bash_patterns"]:
        if not pat.startswith("git ") and pat.lower() in command.replace("\\", "/").lower():
            raise Deny(f"'{pat}' dilarang dijalankan (P2-02)")
    if cfg is not None and ("$(" in command or "`" in command or "<(" in command):
        raise Deny("substitusi perintah ($(...), backtick, atau <(...)) tidak diizinkan untuk agent")
    try:
        segs = segments(command)
    except ValueError:
        if cfg is not None:
            raise Deny("perintah tidak dapat diurai; tulis ulang tanpa kutip yang tidak berpasangan")
        return
    has_cd = any(words and norm_cmd(words[0]) in {"cd", "pushd"} for words, _ in segs)
    for words, targets in segs:
        check_git(words, policy, agent)
        check_protected_bash(words, targets, policy)
        if cfg is not None:
            check_agent_bash(words, targets, cfg, policy, agent, has_cd, cwd)


def read_targets(tool, ti):
    if tool == "Read":
        return [ti.get("file_path")], []
    if tool in {"Grep", "Glob"}:
        return [ti.get("path")], [ti.get("pattern") or "", ti.get("glob") or ""]
    return [], []


def audit_rsia(tool, agent, texts):
    hits = [t for t in texts if t and "rsia-source" in str(t).replace("\\", "/").lower()]
    if hits:
        append_jsonl(RUNS_LOG, {"ts": now_iso(), "event": "rsia_access", "agent_type": agent or "main",
                                "tool": tool, "target_hash": short_hash("|".join(map(str, hits)))})


def decide(payload, policy):
    tool = payload.get("tool_name", "")
    ti = payload.get("tool_input") or {}
    agent = payload.get("agent_type") or ""
    cwd = payload.get("cwd")
    cfg = policy["agents"].get(agent)
    g = policy["global"]

    if tool == "Bash":
        cmd = ti.get("command", "")
        audit_rsia(tool, agent, [cmd])
        check_bash(cmd, policy, agent, cfg, cwd)
        return
    if tool in {"Edit", "Write", "NotebookEdit"}:
        target = ti.get("file_path") or ti.get("notebook_path")
        rel = to_rel(target, cwd)
        if any_match(rel, g["protect_paths"]):
            raise Deny("RSIA-source/ tidak boleh diubah atau ditambah berkas (R-2)")
        if cfg is not None:
            if rel is None:
                raise Deny(f"{agent} tidak boleh menulis di luar repository")
            if any_match(rel, g["deny_write_paths"]):
                raise Deny(f"'{rel}' termasuk berkas yang tidak boleh ditulis agent (§A-7.1)")
            if not any_match(rel, cfg.get("write", [])):
                raise Deny(f"'{rel}' di luar scope tulis {agent} (write_scopes.json)")
        return
    if tool in {"Read", "Grep", "Glob"}:
        paths, patterns = read_targets(tool, ti)
        audit_rsia(tool, agent, paths + patterns)
        if cfg is not None:
            for path_pat, allowed in g.get("restricted_read", {}).items():
                if agent in allowed:
                    continue
                base = path_pat.split("/")[0].lower() + "/"
                rels = [to_rel(p, cwd) for p in paths if p]
                if any(any_match(r, [path_pat]) for r in rels) or \
                        any(base in str(p).replace("\\", "/").lower() for p in patterns):
                    raise Deny(f"akses '{path_pat}' hanya untuk {', '.join(allowed)} (P2-03)")
        return
    if tool == "Agent":
        if cfg is not None and agent != "a01-orchestrator":
            raise Deny("subagent tidak boleh memanggil subagent lain (D-02)")
        if agent == "a01-orchestrator":
            sub = ti.get("subagent_type", "")
            if sub not in policy["agents"] or sub == "a01-orchestrator":
                raise Deny(f"A01 hanya boleh memanggil a02–a13; '{sub}' bukan bagian roster")
        return
    if tool in {"WebSearch", "WebFetch"}:
        if cfg is not None and not cfg.get("web"):
            raise Deny(f"{agent} tidak memiliki izin penelusuran web (P2-01)")
        return


ASCII_MAP = str.maketrans({"§": "", "–": "-", "—": "-", "…": "...", "’": "'", "→": "->"})


def ascii_only(text):
    """Hook stderr is shown through the Windows code page; keep the message ASCII so it stays readable."""
    return text.translate(ASCII_MAP).encode("ascii", "replace").decode("ascii")


def log_denial(payload, agent):
    """Record which rule fired, without paths or command arguments (they may name RSIA files)."""
    tool = payload.get("tool_name", "")
    first = ""
    if tool == "Bash":
        cmd = (payload.get("tool_input") or {}).get("command", "").split()
        first = norm_cmd(cmd[0]) if cmd else ""
    append_jsonl(RUNS_LOG, {"ts": now_iso(), "event": "guard_deny", "agent_type": agent or "main",
                            "tool": tool, "command": first})


def main():
    raw = sys.stdin.read()
    agent, payload = "", {}
    try:
        payload = json.loads(raw or "{}")
        agent = payload.get("agent_type") or ""
        decide(payload, load_policy())
    except Deny as e:
        log_denial(payload, agent)
        sys.stderr.write(ascii_only(f"[guard] Ditolak: {e}. Jangan mencari jalan memutar; "
                                    "laporkan penolakan ini ke A01.\n"))
        return 2
    except Exception as e:  # noqa: BLE001 - the guard must never crash silently
        try:
            roster = agent in load_policy()["agents"]
        except Exception:
            roster = bool(agent)
        if roster:
            sys.stderr.write(f"[guard] Galat internal ({type(e).__name__}); tool call ditolak (fail-closed).\n")
            return 2
        sys.stderr.write(f"[guard] Galat internal ({type(e).__name__}); diloloskan untuk sesi utama.\n")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
