"""Shared helpers for the orchestration scripts (guard, check_staged, check_memory, check_agents).

Policy lives in .claude/policy/write_scopes.json; this module only knows how to read it and how to match
repository paths against its gitignore-style patterns. See docs/ORCHESTRATION_ARCHITECTURE.md §7–§8.
"""
import hashlib, json, os, re, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Windows consoles default to cp1252; hook output and reports contain non-ASCII text.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / ".claude" / "policy" / "write_scopes.json"
SCRATCH = ROOT / ".scratch"
# ORCH_RUNS_LOG lets selftest.py write its synthetic events somewhere else than the real log.
RUNS_LOG = Path(os.environ["ORCH_RUNS_LOG"]) if os.environ.get("ORCH_RUNS_LOG") else SCRATCH / "agent_runs.jsonl"
# Text files are hashed with CRLF folded to LF: core.autocrlf=true checks files out with CRLF, so a raw hash
# would report every text artefact as changed in another checkout (S1/S8). Binary files are hashed raw.
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".html", ".csv", ".tex", ".bib", ".sh", ""}
CASE_INSENSITIVE = os.name == "nt"
WIB = timezone(timedelta(hours=7))
# <SKILL_DIR:name> in the policy resolves to SKILLS_DIR/name (user-level skills; path stays out of Git, Lampiran D).
SKILLS_DIR = os.path.expanduser("~/.claude/skills").replace("\\", "/")

# Patterns for patient/visit identifiers (D-17 R-4). Matching is heuristic; reports name the pattern and
# the count only, never the matched text, so the scan itself does not leak identifiers.
IDENTIFIER_PATTERNS = {
    "kode berkas RSIA (nnnnRnnnnnnnVnnnnnn)": re.compile(r"\d{4}R\d{7}V\d{6}"),
    "nomor kunjungan/SEP berpola V + 6 digit": re.compile(r"(?<![A-Za-z0-9])V\d{6}(?!\d)"),
    "deret 16 digit (NIK/nomor kartu)": re.compile(r"(?<!\d)\d{16}(?!\d)"),
    "label No. RM/SEP/Rawat/SPRI diikuti nomor": re.compile(r"\bNo\.?\s*(?:RM|SEP|Rawat|SPRI)\b\s*[:.]?\s*[A-Z0-9/-]*\d{4,}", re.I),
}


def now_iso():
    return datetime.now(WIB).isoformat(timespec="seconds")


def load_policy(path=POLICY_PATH):
    with open(path, encoding="utf8") as f:
        policy = json.load(f)

    def resolve(x):
        if isinstance(x, str):
            return re.sub(r"<SKILL_DIR:([\w-]+)>", lambda m: f"{SKILLS_DIR}/{m.group(1)}", x)
        if isinstance(x, list):
            return [resolve(v) for v in x]
        if isinstance(x, dict):
            return {k: resolve(v) for k, v in x.items()}
        return x

    return resolve(policy)


def _glob_regex(pattern):
    p, i, out = pattern.strip("/"), 0, ""
    while i < len(p):
        if p.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif p.startswith("**", i):
            out, i = out + ".*", i + 2
        elif p[i] == "*":
            out, i = out + "[^/]*", i + 1
        elif p[i] == "?":
            out, i = out + "[^/]", i + 1
        else:
            out, i = out + re.escape(p[i]), i + 1
    return re.compile("^" + out + "$", re.I if CASE_INSENSITIVE else 0)


def path_matches(rel, pattern):
    """gitignore-style match of a repo-relative POSIX path; 'dir/**' also matches 'dir' itself."""
    if rel is None:
        return False
    if pattern.endswith("/**"):
        base = pattern[:-3].strip("/")
        a, b = (rel.lower(), base.lower()) if CASE_INSENSITIVE else (rel, base)
        if a == b or a.startswith(b + "/"):
            return True
    return bool(_glob_regex(pattern).match(rel))


def any_match(rel, patterns):
    return any(path_matches(rel, p) for p in patterns)


def to_rel(path, cwd=None):
    """Repo-relative POSIX path, or None when the path lies outside the repository."""
    if not path:
        return None
    p = str(path).strip().strip('"').strip("'")
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)          # Git Bash style /c/Users/...
    if m and os.name == "nt":
        p = f"{m.group(1)}:/{m.group(2)}"
    p = p.replace("\\", "/")
    base = Path(cwd) if cwd else ROOT
    absolute = Path(p) if os.path.isabs(p) else base / p
    try:
        rel = os.path.relpath(os.path.normpath(str(absolute)), str(ROOT))
    except ValueError:                                 # different drive on Windows
        return None
    rel = rel.replace("\\", "/")
    if rel == ".":
        return ""
    if rel.startswith("../") or rel == "..":
        return None
    return rel


def sha256_file(path, n=None):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:n] if n else h.hexdigest()


def content_hash(path, n=None):
    """sha256 of a file's content, line endings normalised for text files (Artifact Map, Team Docs Manifest)."""
    p = Path(path)
    if p.suffix.lower() not in TEXT_SUFFIXES:
        return sha256_file(p, n)
    digest = hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return digest[:n] if n else digest


def short_hash(text):
    return hashlib.sha256(text.encode("utf8")).hexdigest()[:12]


def scan_identifiers(text):
    """{pattern name: count} for identifier patterns found in text (no matched content returned)."""
    found = {}
    for name, rx in IDENTIFIER_PATTERNS.items():
        n = len(rx.findall(text))
        if n:
            found[name] = n
    return found


def append_jsonl(path, record):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass
