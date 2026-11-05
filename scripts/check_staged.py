"""Refuse a commit that would publish sensitive or unapproved files (§A-8.3, §A-15.4; D-11, D-17 R-5).

Usage:
  python scripts/check_staged.py                 check the Git index (A13 before commit; pre-commit hook)
  python scripts/check_staged.py --paths A B ... check the given working-tree files instead (tests)

Checks: deny_stage_paths from the policy, files over 50 MB, archive/spreadsheet/photo extensions, and
identifier patterns inside staged text files. Findings name the file and the pattern, never the match.
Exit 1 when anything is refused.
"""
import subprocess, sys
from pathlib import Path
from _common import ROOT, any_match, load_policy, scan_identifiers

MAX_BYTES = 50 * 1024 * 1024
DENY_EXT = {".zip", ".7z", ".rar", ".xlsx", ".xls", ".csv", ".jpeg", ".jpg"}
TEXT_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".html", ".tex", ".bib", ".csv", ""}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True).stdout


def staged():
    out = git("diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR")
    return [p for p in out.decode("utf8").split("\0") if p]


def content(path, from_index):
    if from_index:
        return git("show", f":{path}")
    p = ROOT / path
    return p.read_bytes() if p.is_file() else b""


def check(paths, from_index):
    policy = load_policy()
    problems = []
    for rel in paths:
        rel = rel.replace("\\", "/")
        ext = Path(rel).suffix.lower()
        if any_match(rel, policy["global"]["deny_stage_paths"]):
            problems.append(f"{rel}: path ini tidak boleh di-commit (R-5/D-11)")
            continue
        if ext in DENY_EXT:
            problems.append(f"{rel}: ekstensi {ext} ditolak (data mentah/arsip/foto)")
        data = content(rel, from_index)
        if len(data) > MAX_BYTES:
            problems.append(f"{rel}: {len(data) // (1024 * 1024)} MB melebihi batas 50 MB")
        if ext in TEXT_EXT and data:
            hits = scan_identifiers(data.decode("utf8", errors="replace"))
            for name, n in hits.items():
                problems.append(f"{rel}: {n} kecocokan pola pengenal '{name}' (R-4)")
    return problems


def main(argv):
    if "--paths" in argv:
        paths, from_index = argv[argv.index("--paths") + 1:], False
    else:
        paths, from_index = staged(), True
    problems = check(paths, from_index)
    if problems:
        print("check_staged: DITOLAK")
        for p in problems:
            print("  - " + p)
        print("Keluarkan berkas tersebut dari staging (git restore --staged <path>) atau minta keputusan pengguna.")
        return 1
    print(f"check_staged: OK ({len(paths)} berkas diperiksa)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
