"""Two-pass build of the Bab II draft with cached Daftar Isi / Daftar Tabel page numbers.

Usage: python3 -I tools/build_with_toc.py [editorial|clean ...]   (default: both versions)
1. runs tools/build_docx.py (headings list written to a temp file),
2. renders the .docx to PDF with LibreOffice and reads the printed page label of every heading and table caption,
3. rebuilds with those labels as the cached TOC results and renders again to confirm nothing moved.
The cached numbers come from LibreOffice (Liberation Serif), so Word may differ slightly; Word refreshes
the fields itself (Ctrl+A, F9). Needs the docx skill scripts (DOCX_SKILL_DIR) and poppler (pdftotext).
"""
import json, os, re, subprocess, sys, tempfile

REPO = "/home/user/project-proposal"
SK = os.environ.get("DOCX_SKILL_DIR", "/root/.claude/skills/synced/017185de-19fa-4709-a10a-3db50e5d500d_a2aeaf02-31ea-42d9-a648-645d5f31836f/docx")
tmp = tempfile.mkdtemp(prefix="bab2_toc_")
HEADS, PAGES = tmp + "/headings.json", tmp + "/pages.json"
MODES = sys.argv[1:] or ["editorial", "clean"]
NAME = {"editorial": "Editorial", "clean": "SiapKumpul"}

def build(extra_env, mode):
    env = dict(os.environ, HEADINGS_OUT=HEADS, MODE=mode, **extra_env)
    r = subprocess.run([sys.executable, "-I", REPO + "/tools/build_docx.py"], env=env, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)
    return r.stdout.strip().splitlines()[-1][:160]

def render(mode):
    DOCX = REPO + "/bab2/Proposal-IF4091-Capstone-Individu-2026_Draft-Bab2_" + NAME[mode] + ".docx"
    sys.path.insert(0, SK + "/scripts")
    from office.soffice import run_soffice
    run_soffice(["--headless", "--convert-to", "pdf", "--outdir", tmp, DOCX])
    return tmp + "/" + os.path.basename(DOCX).replace(".docx", ".pdf")

def labels(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    out = []
    for p in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", pdf, "-"], capture_output=True, text=True).stdout.replace("\xa0", " ")
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        lab = lines[-1] if lines and re.fullmatch(r"\d+|[ivxlc]+", lines[-1]) else ""
        out.append((lab, re.sub(r"\s+", " ", t)))
    return out

def measure(pdf):
    pg = labels(pdf)
    first = next(i for i, (lab, _) in enumerate(pg) if lab == "1")      # first page of Bab I
    res, cur = {}, first
    for key in json.load(open(HEADS, encoding="utf8")):
        k = re.sub(r"\s+", " ", key)
        for i in range(first if key.startswith('Tabel') else cur, len(pg)):
            if k in pg[i][1]:
                if not key.startswith('Tabel'): cur = i
                res[key] = pg[i][0]; break
        else:
            sys.exit("heading not found in PDF: " + key)
    return res

for mode in MODES:
    print("==", mode)
    print(build({}, mode))
    first = measure(render(mode))
    json.dump(first, open(PAGES, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(build({"TOC_PAGES": PAGES}, mode))
    second = measure(render(mode))
    print("TOC pages stable between passes:", first == second)
    json.dump(second, open(PAGES, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    for k, v in second.items():
        if k.startswith(("BAB", "Tabel")): print(f"  {v:>3}  {k}")
