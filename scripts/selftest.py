"""Deterministic self-tests for the orchestration scripts (docs/TESTING_CHECKLIST.md, part A).

Usage: python scripts/selftest.py
Uses synthetic hook payloads and synthetic files only. The guard is asked for decisions; no tested command is
executed. No real RSIA-source file and no proposal file is read or modified. Temporary files live under
.scratch/selftest/ and a temporary folder that is removed at the end.
"""
import json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
ROOT = HERE.parent
PY = sys.executable
results = []
_LOG_DIR = Path(tempfile.mkdtemp(prefix="orch_selftest_log_"))
os.environ["ORCH_RUNS_LOG"] = str(_LOG_DIR / "agent_runs.jsonl")  # keep synthetic events out of the real log


def guard(tool, tool_input, agent=None):
    payload = {"tool_name": tool, "tool_input": tool_input, "cwd": str(ROOT), "hook_event_name": "PreToolUse"}
    if agent:
        payload["agent_type"] = agent
    r = subprocess.run([PY, str(HERE / "guard.py")], input=json.dumps(payload), capture_output=True, text=True, encoding="utf-8")
    return r.returncode


def expect(test_id, name, actual, expected):
    ok = actual == expected
    results.append((test_id, name, ok, actual, expected))


def bash(cmd, agent=None):
    return guard("Bash", {"command": cmd}, agent)


ALLOW, DENY = 0, 2


def test_guard():
    # T-05 — RSIA: read allowed and logged; writes denied (main session and agents)
    log = Path(os.environ["ORCH_RUNS_LOG"])
    before = log.read_text(encoding="utf8").count("\n") if log.exists() else 0
    expect("T-05", "Read RSIA diizinkan (sesi utama)", guard("Read", {"file_path": "RSIA-source/contoh.pdf"}), ALLOW)
    expect("T-05", "Read RSIA diizinkan (a02)", guard("Read", {"file_path": "RSIA-source/contoh.pdf"}, "a02-research-evidence"), ALLOW)
    expect("T-05", "Write ke RSIA ditolak", guard("Write", {"file_path": "RSIA-source/baru.txt"}), DENY)
    expect("T-05", "Edit RSIA ditolak (a02)", guard("Edit", {"file_path": "RSIA-source/contoh.pdf"}, "a02-research-evidence"), DENY)
    for cmd in ["rm RSIA-source/a.zip", "mv RSIA-source/a.zip b.zip", "cp x.txt RSIA-source/", "echo x > RSIA-source/a.txt",
                "touch RSIA-source/a", "sed -i s/a/b/ RSIA-source/a.txt", "unzip RSIA-source/a.zip", "unzip -o RSIA-source/a.zip",
                "tar -xf RSIA-source/a.tar", "git add RSIA-source/a.zip", "icacls RSIA-source /deny x"]:
        expect("T-05", f"Bash ditolak: {cmd}", bash(cmd), DENY)
    for cmd in ["unzip -l RSIA-source/a.zip", "unzip -p RSIA-source/a.zip m.pdf", "unzip -o -d .scratch/rsia/raw/ RSIA-source/a.zip"]:
        expect("T-05", f"Bash diizinkan: {cmd}", bash(cmd), ALLOW)
    expect("T-05", "a02 unzip ke .scratch/rsia diizinkan",
           bash("unzip -o -d .scratch/rsia/raw/ RSIA-source/a.zip", "a02-research-evidence"), ALLOW)
    # T-24 — access log stores a hash, not the path
    lines = log.read_text(encoding="utf8").splitlines() if log.exists() else []
    new = lines[before:]
    expect("T-24", "log akses RSIA tercatat", any('"rsia_access"' in ln for ln in new), True)
    expect("T-24", "log akses tanpa nama berkas", any("RSIA-source" in ln or "contoh.pdf" in ln for ln in new), False)
    # T-04 — dangerous Git and staging (applies to everyone)
    for cmd in ["git add -A", "git add .", "git add --all", "git add -f x", "git add *.md", "git commit -a -m x",
                "git commit --no-verify -m x", "git commit -n -m x", "git push -f origin main", "git push --force origin main",
                "git push --force-with-lease", "git push origin +main", "git push --delete origin x", "git reset --hard",
                "git clean -fd", "git stash", "git rebase main", "git checkout -- CLAUDE.md", "git -C . add -A",
                'git add -- "Penyelarasan Pemahaman Capstone.md"', "git add -- .scratch/x.txt",
                "python tools/build_docx.py", "python -I tools/build_with_toc.py"]:
        expect("T-04", f"ditolak: {cmd}", bash(cmd), DENY)
    for cmd in ["git status --porcelain", "git log --oneline -5", "git add -- memory/PROJECT_STATE.md"]:
        expect("T-04", f"diizinkan (sesi utama): {cmd}", bash(cmd), ALLOW)
    # T-04 — per-agent write scopes and Bash allowlists
    w = lambda p, a: guard("Write", {"file_path": p, "content": "x"}, a)
    expect("T-04", "a04 tulis bab2 ditolak", w("bab2/x.md", "a04-supervisor"), DENY)
    expect("T-04", "a04 Bash apa pun ditolak", bash("ls", "a04-supervisor"), DENY)
    expect("T-04", "a03 tulis bab2/*.md diizinkan", w("bab2/II_baru.md", "a03-academic-writer"), ALLOW)
    expect("T-29", "a03 tulis docx ditolak", w("bab2/x.docx", "a03-academic-writer"), DENY)
    expect("T-04", "a03 tulis memory ditolak", w("memory/PROJECT_STATE.md", "a03-academic-writer"), DENY)
    expect("T-04", "a03 tulis di luar repo ditolak", w(str(Path(tempfile.gettempdir()) / "x.md"), "a03-academic-writer"), DENY)
    expect("T-04", "a03 tulis template ditolak", w("template/x.md", "a03-academic-writer"), DENY)
    expect("T-29", "a03 build_modular diizinkan (prompt ask dari settings)", bash("python -I tools/build_modular.py --only II", "a03-academic-writer"), ALLOW)
    expect("T-04", "a13 tulis memory diizinkan", w("memory/PROJECT_STATE.md", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 tulis bab2 ditolak", w("bab2/x.md", "a13-memory-manager"), DENY)
    expect("T-04", "a13 git add path eksplisit diizinkan", bash("git add -- memory/PROJECT_STATE.md", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 commit diizinkan (prompt ask)", bash("git commit -m 'memory: update'", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 push biasa diizinkan (prompt ask)", bash("git push origin setup/orchestration", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 push force ditolak", bash("git push --force origin setup/orchestration", "a13-memory-manager"), DENY)
    expect("T-04", "a02 pdftotext ke stdout diizinkan", bash("pdftotext -f 1 -l 1 source/x.pdf -", "a02-research-evidence"), ALLOW)
    expect("T-04", "a02 pdftotext ke bab2 ditolak", bash("pdftotext -f 1 -l 1 source/x.pdf bab2/out.txt", "a02-research-evidence"), DENY)
    expect("T-04", "a02 redirection ke .scratch diizinkan", bash("pdfinfo source/x.pdf > .scratch/info.txt", "a02-research-evidence"), ALLOW)
    expect("T-04", "a02 redirection ke bab2 ditolak", bash("pdfinfo source/x.pdf > bab2/info.txt", "a02-research-evidence"), DENY)
    expect("T-04", "a02 curl ditolak", bash("curl https://example.org", "a02-research-evidence"), DENY)
    expect("T-04", "a02 substitusi perintah ditolak", bash("pdfinfo $(ls source | head -1)", "a02-research-evidence"), DENY)
    expect("T-04", "a01 git commit ditolak (bukan allowlist a01)", bash("git commit -m x", "a01-orchestrator"), DENY)
    expect("T-04", "a01 check_memory diizinkan", bash("python scripts/check_memory.py", "a01-orchestrator"), ALLOW)
    expect("T-04", "agent non-roster hanya aturan global", bash("ls", "Explore"), ALLOW)
    # T-25 — material/ only for a10
    expect("T-25", "a07 Read material ditolak", guard("Read", {"file_path": "material/9_slide.pdf"}, "a07-qa-academic"), DENY)
    expect("T-25", "a07 Grep di material ditolak", guard("Grep", {"pattern": "x", "path": "material"}, "a07-qa-academic"), DENY)
    expect("T-25", "a07 Glob material/** ditolak", guard("Glob", {"pattern": "material/**/*.pdf"}, "a07-qa-academic"), DENY)
    expect("T-25", "a06 pdftotext material ditolak", bash("pdftotext material/9_slide.pdf -", "a06-cross-proposal"), DENY)
    expect("T-25", "a10 Read material diizinkan", guard("Read", {"file_path": "material/9_slide.pdf"}, "a10-qa-structure"), ALLOW)
    expect("T-25", "a10 pdftotext material diizinkan", bash("pdftotext -f 1 -l 1 material/9_slide.pdf -", "a10-qa-structure"), ALLOW)
    expect("T-25", "sesi utama Read material diizinkan", guard("Read", {"file_path": "material/9_slide.pdf"}), ALLOW)
    # T-07 / D-02 — no nesting; a01 roster only
    expect("T-07", "a05 memanggil Agent ditolak", guard("Agent", {"subagent_type": "a07-qa-academic"}, "a05-critical-reviewer"), DENY)
    expect("T-07", "a01 memanggil a03 diizinkan", guard("Agent", {"subagent_type": "a03-academic-writer"}, "a01-orchestrator"), ALLOW)
    expect("T-07", "a01 memanggil general-purpose ditolak", guard("Agent", {"subagent_type": "general-purpose"}, "a01-orchestrator"), DENY)
    # T-28 — web only for a02/a08 (prompt itself comes from settings ask)
    expect("T-28", "a09 WebSearch ditolak", guard("WebSearch", {"query": "x"}, "a09-qa-editorial"), DENY)
    expect("T-28", "a08 WebSearch diizinkan guard", guard("WebSearch", {"query": "doi"}, "a08-qa-citation"), ALLOW)

    # Runtime feedback 5 Nov 2026: read-only helpers must not make A01/A13 PARTIAL
    expect("T-04", "a13 cd ke dalam repo diizinkan", bash(f'cd "{ROOT}" && python scripts/check_memory.py', "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 cd ke luar repo ditolak", bash("cd C:/Windows && ls", "a13-memory-manager"), DENY)
    expect("T-04", "a13 pipe ke head diizinkan", bash("python scripts/check_memory.py 2>&1 | head -60", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 git ls-tree diizinkan", bash("git ls-tree -r --name-only 7d59b85 | grep -Ei RULES | head -40", "a13-memory-manager"), ALLOW)
    expect("T-04", "a13 python -c tetap ditolak", bash('python -c "print(1)"', "a13-memory-manager"), DENY)
    expect("T-04", "a01 echo pemisah diizinkan", bash('git status --porcelain; echo "---"; git log --oneline -5', "a01-orchestrator"), ALLOW)
    expect("T-04", "a01 echo dengan redirection ke bab2 ditolak", bash("echo x > bab2/x.md", "a01-orchestrator"), DENY)
    expect("T-25", "a07 cat material lewat safe_bash tetap ditolak", bash("cat material/9_slide.pdf", "a06-cross-proposal"), DENY)
    payload = {"tool_name": "Bash", "tool_input": {"command": "rm RSIA-source/a.zip"}, "cwd": str(ROOT)}
    r = subprocess.run([PY, str(HERE / "guard.py")], input=json.dumps(payload).encode("utf-8"), capture_output=True)
    expect("T-04", "pesan penolakan hanya ASCII", all(b < 128 for b in r.stderr), True)
    deny_lines = [l for l in log.read_text(encoding="utf8").splitlines() if '"guard_deny"' in l]
    expect("T-24", "penolakan tercatat di log", len(deny_lines) > 0, True)
    expect("T-24", "log penolakan tanpa path", any("RSIA-source" in l or "a.zip" in l for l in deny_lines), False)


def make_link(link, target):
    """Directory junction (Windows) or symlink (elsewhere) pointing at a synthetic folder; False if not possible."""
    try:
        if os.name == "nt":
            import _winapi
            _winapi.CreateJunction(str(target), str(link))
        else:
            os.symlink(str(target), str(link), target_is_directory=True)
        return True
    except (OSError, ImportError, AttributeError):
        return False


def remove_link(link):
    """Remove the link itself, never its target."""
    for fn in (os.rmdir, os.unlink):
        try:
            fn(str(link))
            return
        except OSError:
            continue


def test_d20():
    """D-20 / TSK-014 after G2 FAIL: findings F1-F5, A02 unchanged, A12 limited to D-20, A13 hash-object."""
    from _common import SKILLS_DIR
    a12, a13, a02 = "a12-qa-integrity", "a13-memory-manager", "a02-research-evidence"
    fx = ROOT / "_selftest_d20"
    dlink = ROOT / ".scratch" / "_selftest_d20_link"
    shutil.rmtree(fx, ignore_errors=True)
    remove_link(dlink)
    (fx / "ok").mkdir(parents=True)
    (fx / "ok" / "a.md").write_text("sintetis", encoding="utf8")
    (fx / "withdocx").mkdir()
    (fx / "withdocx" / "b.docx").write_bytes(b"PK\x03\x04")
    (fx / "target").mkdir()
    (fx / "target" / "t.md").write_text("sintetis", encoding="utf8")
    (fx / "withlink").mkdir()
    (ROOT / ".scratch").mkdir(exist_ok=True)
    links_ok = make_link(fx / "withlink" / "j", fx / "target") and make_link(dlink, fx / "target")
    expect("T-04", "fixture junction/symlink dapat dibuat", links_ok, True)
    try:
        V = f'python "{SKILLS_DIR}/docx/scripts/office/validate.py"'
        U = f'python "{SKILLS_DIR}/docx/scripts/office/unpack.py"'
        C = f'python "{SKILLS_DIR}/pdf/scripts/convert_pdf_to_images.py"'
        P = f'python "{SKILLS_DIR}/docx/scripts/office/pack.py"'
        gitbash = "/" + SKILLS_DIR[0].lower() + SKILLS_DIR[2:] if re.match(r"^[A-Za-z]:/", SKILLS_DIR) else SKILLS_DIR
        # F1 - skill scripts (a12): read-only validation in place, extraction output only to .scratch/**
        for cmd in [f"{V} template/x.docx", f"{V} -v template/x.docx", f"{V} --verbose bab2/x.docx",
                    f"{V} --original template/x.docx .scratch/t19", f"{V} --author=Penguji template/x.docx",
                    f"{U} template/x.docx .scratch/t19/", f"{U} template/x.docx .scratch/t19 --merge-runs false",
                    f"{U} template/x.docx .scratch/t19 --simplify-redlines=true",
                    f'python "{gitbash}/docx/scripts/office/validate.py" template/x.docx']:
            expect("T-19", f"F1 a12 diizinkan: {cmd.replace(SKILLS_DIR, '<SKILLS>')}", bash(cmd, a12), ALLOW)
        for cmd in [f"{V} --auto-repair template/x.docx", f"{V} template/x.docx --auto-repair",
                    f"{V} --auto template/x.docx", f"{V} --auto-r .scratch/t19", f"{V} --auto-repair .scratch/t19",
                    f"{V} --verb template/x.docx", f"{V} -vv template/x.docx", f"{V} template/x.docx extra",
                    f"{V} RSIA-source/x.docx", f"{V} material/x.docx", f"{V} ../x.docx", f"{V} template/*.docx",
                    f"{V} .", f"{V} template", f"{V} --original RSIA-source/x.docx template/x.docx",
                    f"{V} {fx.name}/withlink/j/t.docx",
                    f"{U} template/x.docx bab2/u", f"{U} template/x.docx RSIA-source/u",
                    f"{U} template/x.docx template/u", f"{U} template/x.docx source/u",
                    f"{U} template/x.docx material/u", f"{U} template/x.docx .scratch/u.docx",
                    f"{U} template/x.docx .scratch/../bab2/u", f"{U} template/x.docx ../u",
                    f"{U} template/x.docx .scratch/_selftest_d20_link/u", f"{U} material/x.docx .scratch/u",
                    f"{U} RSIA-source/x.docx .scratch/rsia/u", f"{U} template/x.docx",
                    f"{U} template/x.docx .scratch/u --merge-runs", f"{U} template/x.docx .scratch/u --merge true",
                    f"{U} template/x.docx .scratch/u --merge-runs maybe",
                    f"{P} .scratch/u template/x.docx", f"{C} source/x.pdf .scratch/img",
                    f'python "{SKILLS_DIR}/docx/../pdf/scripts/convert_pdf_to_images.py" x.pdf .scratch/i',
                    f'python "{SKILLS_DIR}/docx/scripts/office/../office/pack.py" .scratch/u x.docx']:
            expect("T-19", f"F1 a12 ditolak: {cmd.replace(SKILLS_DIR, '<SKILLS>')}", bash(cmd, a12), DENY)
        # A02 - behaviour before TSK-014 (DENY) is kept; no other agent gains skill scripts
        for agent, cmd in [(a02, f"{C} source/x.pdf .scratch/img"), (a02, f"{C} source/x.pdf bab2/img"),
                           (a02, f"{C} source/x.pdf RSIA-source/img"), (a02, f"{C} source/x.pdf template"),
                           (a02, f'python "{gitbash}/pdf/scripts/convert_pdf_to_images.py" x.pdf .scratch/i'),
                           (a02, f"{V} template/x.docx"), (a02, f"{U} template/x.docx .scratch/u"),
                           ("a06-cross-proposal", f"{C} x.pdf .scratch/i"), ("a03-academic-writer", f"{V} x.docx"),
                           (a13, f"{V} template/x.docx"), ("a04-supervisor", f"{V} template/x.docx")]:
            expect("T-04", f"A02/lain tetap ditolak ({agent}): {cmd.replace(SKILLS_DIR, '<SKILLS>')}",
                   bash(cmd, agent), DENY)

        def run_hook(agent):
            p = {"hook_event_name": "SubagentStart", "agent_type": agent, "agent_id": "x", "session_id": "y"}
            return subprocess.run([PY, str(HERE / "log_run.py")], input=json.dumps(p).encode("utf-8"),
                                  capture_output=True)
        r = run_hook(a12)
        try:
            ctx = json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]
        except (ValueError, KeyError):
            ctx = ""
        expect("T-19", "SubagentStart a12 menyuntikkan validate.py dan unpack.py",
               f"{SKILLS_DIR}/docx/scripts/office/validate.py" in ctx and
               f"{SKILLS_DIR}/docx/scripts/office/unpack.py" in ctx and r.returncode == 0, True)
        expect("T-19", "SubagentStart a12 tidak menyuntikkan skrip lain", "convert_pdf_to_images" in ctx, False)
        for agent in (a02, "a04-supervisor"):
            r = run_hook(agent)
            expect("T-19", f"SubagentStart {agent} tanpa suntikan", r.stdout.strip() == b"" and r.returncode == 0, True)
        # A12 - only what D-20 needs is allowed
        for cmd in ["mkdir -p .scratch/render", "mkdir .scratch", "cp bab2/x.md .scratch/x.md",
                    "cp -- bab2/x.md .scratch/", "cp bab2/a.md bab3/b.md .scratch/",
                    f"cp -r {fx.name}/ok .scratch/ok", f"cp -rf {fx.name}/ok .scratch/ok2"]:
            expect("T-04", f"A12 diizinkan: {cmd}", bash(cmd, a12), ALLOW)
        # F2 - wildcard, recursive, protected/restricted source, parent directory, links, unsafe options
        for cmd in ["cp R*/a.pdf .scratch/a.pdf", "cp RSIA-sourc?/a.pdf .scratch/a.pdf", "cp [R]SIA-source/a.pdf .scratch/",
                    "cp mat*/9_slide.pdf .scratch/9.pdf", "cp ma?erial/9_slide.pdf .scratch/", "cp bab2/*.md .scratch/",
                    "cp -r . .scratch/all", "cp -r ./ .scratch/all", "cp -R bab2/.. .scratch/all",
                    "cp -r .scratch/.. .scratch/all", f"cp -r {fx.name} .scratch/x", f"cp -r {fx.name}/withlink .scratch/x",
                    f"cp {fx.name}/withlink/j/t.md .scratch/t.md", "cp RSIA-source/a.pdf .scratch/a.pdf",
                    "cp rsia-SOURCE/a.pdf .scratch/a.pdf", "cp 'RSIA-source\\a.pdf' .scratch/a.pdf",
                    "cp RSIA-source .scratch/r", "cp material/9_slide.pdf .scratch/9.pdf", "cp MATERIAL/9_slide.pdf .scratch/",
                    "cp -r material .scratch/m", "cp source/x.pdf .scratch/x.pdf", "cp -r source .scratch/s",
                    "cp capstone-teammate-propose/x.md .scratch/", "cp 'Penyelarasan Pemahaman Capstone.md' .scratch/p.md",
                    "cp -r template .scratch/t", "cp -a bab2/x.md .scratch/", "cp --archive bab2/x.md .scratch/",
                    "cp -s bab2/x.md .scratch/x.md", "cp -l bab2/x.md .scratch/x.md", "cp -L bab2/x.md .scratch/",
                    "cp -P bab2/x.md .scratch/", "cp -d bab2/x.md .scratch/", "cp -t .scratch bab2/x.md",
                    "cp -T bab2/x.md .scratch/x.md", "cp --target-directory=.scratch bab2/x.md",
                    "cp bab2/x.md .scratch/_selftest_d20_link/x.md", "cp bab2/x.md .scratch/*",
                    "cd bab2 && cp x.md .scratch/x.md", "cp x.md", "cpio -o", "find . -name x"]:
            expect("T-04", f"F2 a12 ditolak: {cmd}", bash(cmd, a12), DENY)
        # F3 - docx stays protected by deny_write_paths **/*.docx, also through cp
        for cmd in ["cp template/x.docx .scratch/x.docx", "cp bab2/x.docx .scratch/x.docx",
                    "cp bab2/x.md .scratch/x.docx", "cp modular/x.docx .scratch/", f"cp -r {fx.name}/withdocx .scratch/w",
                    "mkdir .scratch/x.docx"]:
            expect("T-04", f"F3 a12 ditolak: {cmd}", bash(cmd, a12), DENY)
        # F4 - sources outside the repository
        outside = Path(tempfile.gettempdir()).resolve().as_posix() + "/x.txt"   # long form: no 8.3 '~'
        for cmd in ["cp ../x.txt .scratch/x.txt", "cp C:/Windows/win.ini .scratch/w", "cp /c/Windows/win.ini .scratch/w",
                    f'cp "{outside}" .scratch/x.txt', "cp ../../.ssh/id_rsa .scratch/k"]:
            expect("T-04", f"F4 a12 ditolak: {cmd}", bash(cmd, a12), DENY)
        # mkdir - destination rules
        for cmd in ["mkdir bab2/x", "mkdir -p .scratch/a bab2/b", "mkdir .scratch/../bab2", "mkdir RSIA-source/x",
                    "mkdir -m 777 .scratch/x", "mkdir .scratch/$X", "mkdir .scratch/{a,../../bab2}", "mkdir ~/x",
                    "mkdir .scratch/_selftest_d20_link/sub", "mkdir .scratch/x*"]:
            expect("T-04", f"mkdir a12 ditolak: {cmd}", bash(cmd, a12), DENY)
        # F5 - read policy and .scratch access unchanged outside the decision
        w = lambda p, a: guard("Write", {"file_path": p, "content": "x"}, a)
        r_ = lambda p, a: guard("Read", {"file_path": p}, a)
        for name, actual, want in [
                ("a12 Read template/x.docx", r_("template/x.docx", a12), ALLOW),
                ("a12 Read RSIA-source (diaudit)", r_("RSIA-source/a.pdf", a12), ALLOW),
                ("a12 Read material", r_("material/9_slide.pdf", a12), DENY),
                ("a10 Read material", r_("material/9_slide.pdf", "a10-qa-structure"), ALLOW),
                ("a12 Read memory", r_("memory/PROJECT_STATE.md", a12), ALLOW),
                ("a12 Write .scratch/x.md", w(".scratch/x.md", a12), ALLOW),
                ("a12 Write .scratch/x.docx", w(".scratch/x.docx", a12), DENY),
                ("a12 Write bab2/x.md", w("bab2/x.md", a12), DENY),
                ("a02 Write .scratch/x.md", w(".scratch/x.md", a02), ALLOW),
                ("a12 cp memory ke .scratch (sesuai kebijakan baca)", bash("cp memory/PROJECT_STATE.md .scratch/ps.md", a12), ALLOW),
                ("a12 pdftotext ke stdout", bash("pdftotext -f 1 -l 1 bab2/x.pdf -", a12), ALLOW),
                ("a02 unzip RSIA ke .scratch/rsia", bash("unzip -o -d .scratch/rsia/raw/ RSIA-source/a.zip", a02), ALLOW),
                ("sesi utama cp tidak berubah (aturan global)", bash("cp bab2/x.md .scratch/x.md"), ALLOW),
                ("sesi utama cp ke RSIA tetap ditolak", bash("cp x.txt RSIA-source/"), DENY)]:
            expect("T-04", f"F5 {name}", actual, want)
        # A13 - git hash-object per D-20
        for cmd, want in [("git hash-object CLAUDE.md", ALLOW), ("git hash-object --stdin-paths", ALLOW),
                          ("git hash-object -w CLAUDE.md", DENY), ("git hash-object -t blob -w CLAUDE.md", DENY),
                          ("git hash-object -tw CLAUDE.md", DENY), ("mkdir .scratch/x", DENY), ("cp x .scratch/x", DENY)]:
            expect("T-04", f"A13 {cmd}", bash(cmd, a13), want)
        expect("T-04", "a12 git hash-object ditolak", bash("git hash-object CLAUDE.md", a12), DENY)
        expect("T-04", "a01 git hash-object ditolak", bash("git hash-object CLAUDE.md", "a01-orchestrator"), DENY)
        expect("T-04", "a12 python -c tetap ditolak", bash('python -c "print(1)"', a12), DENY)
    finally:
        remove_link(fx / "withlink" / "j")
        remove_link(dlink)
        shutil.rmtree(fx, ignore_errors=True)
        expect("T-04", "fixture sintetis dan link-nya terhapus", (not os.path.lexists(dlink)) and not fx.exists(), True)


def test_staged():
    tmp = Path(tempfile.mkdtemp(prefix="_selftest_", dir=ROOT))
    try:
        rel = tmp.relative_to(ROOT).as_posix()
        (tmp / "ok.md").write_text("Naskah biasa tentang klaim pending dan No. RM sebagai istilah.\n", encoding="utf8")
        (tmp / "leak.md").write_text("Kasus V" + "123456" + " dan NIK " + "3201" * 4 + "\n", encoding="utf8")
        (tmp / "data.xlsx").write_bytes(b"PK\x03\x04")

        def run(*paths):
            return subprocess.run([PY, str(HERE / "check_staged.py"), "--paths", *paths], cwd=ROOT,
                                  capture_output=True, text=True, encoding="utf-8")
        r = run(f"{rel}/ok.md")
        expect("T-22", "teks normal lolos check_staged", r.returncode, 0)
        r = run(f"{rel}/leak.md")
        expect("T-22", "pola pengenal sintetis terdeteksi", r.returncode, 1)
        expect("T-22", "laporan tidak menampilkan isi pengenal", ("123456" in r.stdout) or ("3201" in r.stdout), False)
        expect("T-06", "ekstensi xlsx ditolak", run(f"{rel}/data.xlsx").returncode, 1)
        expect("T-06", "path RSIA ditolak", run("RSIA-source/contoh.pdf").returncode, 1)
        expect("T-06", "path .scratch ditolak", run(".scratch/x.txt").returncode, 1)
        expect("T-06", "Penyelarasan ditolak", run("Penyelarasan Pemahaman Capstone.md").returncode, 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cm(*args):
    return subprocess.run([PY, str(HERE / "check_memory.py"), *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


def test_memory():
    base = ROOT / ".scratch" / "selftest"
    shutil.rmtree(base, ignore_errors=True)
    mem = base / "memory"
    shutil.copytree(ROOT / "memory", mem)
    fake = base / "fakeroot"
    (fake / "RSIA-source" / "sub").mkdir(parents=True)
    (fake / "RSIA-source" / "sub" / "a.txt").write_text("sintetis A", encoding="utf8")
    (fake / "RSIA-source" / "b.txt").write_text("sintetis B", encoding="utf8")
    # baseline on the real memory (structure only; artefacts of this checkout)
    r = cm("--memory-dir", str(ROOT / "memory"), "--allow-uncommitted")
    expect("T-13", "memory awal tanpa NOT_READY", "NOT_READY" in r.stdout.splitlines()[0], False)
    # S10 — APPROVED without evidence
    dl = mem / "DECISION_LOG.md"
    t = dl.read_text(encoding="utf8")
    t2 = re.sub(r"(id: D-02\n.*?)approval_evidence:.*?(?=\n```)", r"\1", t, count=1, flags=re.S)
    dl.write_text(t2, encoding="utf8")
    r = cm("--memory-dir", str(mem), "--allow-uncommitted")
    expect("T-13", "S10: APPROVED tanpa bukti → NOT_READY", "S10" in r.stdout and "NOT_READY" in r.stdout, True)
    dl.write_text(t, encoding="utf8")
    # S11 — identifier in memory
    ps = mem / "PROJECT_STATE.md"
    pt = ps.read_text(encoding="utf8")
    ps.write_text(pt + "\nCatatan uji: V" + "654321\n", encoding="utf8")
    r = cm("--memory-dir", str(mem), "--allow-uncommitted")
    expect("T-22", "S11: pola pengenal di memory → NOT_READY", "S11" in r.stdout, True)
    expect("T-22", "S11 tidak menampilkan isi pengenal", "654321" in r.stdout, False)
    ps.write_text(pt, encoding="utf8")
    # S3 — DONE task with missing output
    tt = mem / "TASK_TRACKER.md"
    tx = tt.read_text(encoding="utf8")
    tt.write_text(tx.replace("| TSK-004 | Phase 3: implementasi di worktree setup/orchestration | DOING |",
                             "| TSK-004 | Phase 3: implementasi di worktree setup/orchestration | DONE |")
                    .replace("`.claude/settings.json`, `scripts/guard.py`", "`scripts/tidak_ada.py`"), encoding="utf8")
    r = cm("--memory-dir", str(mem), "--allow-uncommitted")
    expect("T-13", "S3: DONE tanpa keluaran → NOT_READY", "S3" in r.stdout, True)
    tt.write_text(tx, encoding="utf8")
    # S12 — integrity manifest on a synthetic RSIA copy
    r = cm("--root", str(fake), "--init-rsia-manifest")
    expect("T-23", "manifest sintetis dibuat", r.returncode, 0)
    r = cm("--root", str(fake), "--init-rsia-manifest")
    expect("T-23", "manifest tidak ditimpa", r.returncode, 1)
    r = cm("--root", str(fake), "--memory-dir", str(mem), "--allow-uncommitted")
    expect("T-23", "S12 tidak melapor sebelum perubahan", "S12" in r.stdout and "NOT_READY" in r.stdout, False)
    (fake / "RSIA-source" / "b.txt").write_text("diubah", encoding="utf8")
    r = cm("--root", str(fake), "--memory-dir", str(mem), "--allow-uncommitted")
    expect("T-23", "S12 mendeteksi perubahan", "S12" in r.stdout and "1 berubah" in r.stdout, True)
    expect("T-23", "S12 tidak menyebut nama berkas", "b.txt" in r.stdout, False)
    # S1 — CRLF checkout of an unchanged text artefact must not count as a change
    root2 = base / "crlfroot"
    root2.mkdir()
    src = (ROOT / "RULES.md").read_bytes().replace(b"\r\n", b"\n")
    (root2 / "RULES.md").write_bytes(src.replace(b"\n", b"\r\n"))
    from hashlib import sha256
    h = sha256(src).hexdigest()[:12]
    mem2 = base / "memory2"
    shutil.copytree(mem, mem2)
    ps2 = mem2 / "PROJECT_STATE.md"
    ps2.write_text(re.sub(r"\| `RULES.md` \|(.*?)\| `[0-9a-f]{12}` \|", lambda m: f"| `RULES.md` |{m.group(1)}| `{h}` |", ps2.read_text(encoding="utf8")), encoding="utf8")
    r = cm("--root", str(root2), "--memory-dir", str(mem2), "--allow-uncommitted")
    expect("T-13", "S1: perbedaan CRLF/LF saja tidak dilaporkan", "berubah sejak dicatat: RULES.md" in r.stdout, False)
    # hook output is valid JSON
    r = cm("--hook", "--memory-dir", str(ROOT / "memory"))
    try:
        ok = json.loads(r.stdout)["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    except (ValueError, KeyError):
        ok = False
    expect("T-13", "--hook menghasilkan JSON SessionStart", ok, True)
    shutil.rmtree(base, ignore_errors=True)
    shutil.rmtree(_LOG_DIR, ignore_errors=True)


def test_agents():
    r = subprocess.run([PY, str(HERE / "check_agents.py")], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    expect("T-20", "check_agents lolos pada roster aktual", r.returncode, 0)
    extra = ROOT / ".claude" / "agents" / "a14-tambahan.md"
    extra.write_text("---\nname: a14-tambahan\ndescription: uji\n---\n", encoding="utf8")
    try:
        r = subprocess.run([PY, str(HERE / "check_agents.py")], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        expect("T-20", "agent ke-14 terdeteksi", r.returncode == 1 and "a14-tambahan" in r.stdout, True)
    finally:
        extra.unlink()


def main():
    test_guard()
    test_d20()
    test_staged()
    test_memory()
    test_agents()
    failed = [r for r in results if not r[2]]
    for tid, name, ok, actual, expected in results:
        print(f"{'LULUS' if ok else 'GAGAL'}  {tid}  {name}" + ("" if ok else f"  (dapat {actual}, harap {expected})"))
    print(f"\n{len(results) - len(failed)}/{len(results)} lulus")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
