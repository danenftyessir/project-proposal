"""Extract text from .docx, .pdf, or .xlsx into .scratch/ for agents that may not edit the source (§A-13).

Usage: python scripts/extract_text.py <input> <output.txt> [--pages A-B]
The output path must lie under .scratch/ (RSIA-derived output under .scratch/rsia/raw/, D-17 R-3).
The input is only read; it is never modified.
"""
import subprocess, sys
from pathlib import Path
from _common import ROOT, path_matches, to_rel


def docx_text(path):
    import docx
    d = docx.Document(str(path))
    lines = [p.text for p in d.paragraphs]
    for ti, table in enumerate(d.tables, 1):
        lines.append(f"\n[Tabel {ti}]")
        for row in table.rows:
            lines.append("\t".join(c.text.strip() for c in row.cells))
    return "\n".join(lines)


def pdf_text(path, pages):
    args = ["pdftotext", "-layout"]
    if pages:
        a, _, b = pages.partition("-")
        args += ["-f", a, "-l", b or a]
    r = subprocess.run(args + [str(path), "-"], capture_output=True)
    if r.returncode == 0:
        return r.stdout.decode("utf8", errors="replace")
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    idx = range(len(reader.pages))
    if pages:
        a, _, b = pages.partition("-")
        idx = range(int(a) - 1, int(b or a))
    return "\n\f".join(reader.pages[i].extract_text() or "" for i in idx)


def xlsx_text(path):
    import openpyxl
    wb = openpyxl.load_workbook(str(path), read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"[Sheet {ws.title}]")
        for row in ws.iter_rows(values_only=True):
            out.append("\t".join("" if v is None else str(v) for v in row))
    return "\n".join(out)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src, dst = Path(argv[0]), argv[1]
    pages = argv[argv.index("--pages") + 1] if "--pages" in argv else None
    rel = to_rel(dst)
    if rel is None or not path_matches(rel, ".scratch/**"):
        print("extract_text: keluaran harus berada di .scratch/", file=sys.stderr)
        return 2
    ext = src.suffix.lower()
    if ext == ".docx":
        text = docx_text(src)
    elif ext == ".pdf":
        text = pdf_text(src, pages)
    elif ext in {".xlsx", ".xlsm"}:
        text = xlsx_text(src)
    else:
        print(f"extract_text: ekstensi {ext} tidak didukung", file=sys.stderr)
        return 2
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf8")
    print(f"extract_text: {len(text)} karakter → {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
