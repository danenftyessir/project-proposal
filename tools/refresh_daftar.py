"""Segarkan nomor halaman daftar isi, daftar lampiran, daftar gambar, dan daftar tabel pada docx.

Nomor halaman dibaca dari ekspor PDF Microsoft Word (nomor tercetak pada kaki halaman), lalu
ditulis ke entri yang sudah ada tanpa mengubah teks atau formatnya. Entri yang tidak ditemukan
pada badan dokumen dan keterangan gambar/tabel yang belum tercantum pada daftar dilaporkan.
Setelah itu PDF dengan nama sama dirender ulang dari docx yang sudah disegarkan.

Pemakaian (dari akar repositori):
    python tools/refresh_daftar.py "modular/TA1 bab 1.docx" "modular/TA1 bab 2.docx" ...
"""
import re
import shutil
import sys
import tempfile
from pathlib import Path

import fitz
from docx import Document
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_bab34_docx as B  # noqa: E402
from build_gabungan import displayed_page, style  # noqa: E402

ptext, norm = B.ptext, B.norm
CAPTION = re.compile(r"^(Gambar|Tabel) [IVX]+\.\d+\. ")
LABEL = re.compile(r"^(Lampiran [A-Z]\.|[A-Z]\.\d*|[IVX]+(?:\.\d+)*\.?)\s*")


def in_table(p):
    return any(a.tag == qn("w:tbl") for a in p.iterancestors())


def entry_paragraphs(front):
    out = []
    for e in front:
        for p in e.iter(qn("w:p")):
            if in_table(p) or p.find(".//" + qn("w:tab")) is None:
                continue
            ts = list(p.iter(qn("w:t")))
            if len(ts) >= 2 and re.fullmatch(r"\d+", (ts[-1].text or "").strip()):
                out.append((p, ts))
    return out


def find_page(texts, shown, start, needle):
    for i in range(start, len(texts)):
        if needle in texts[i] and ".........." not in texts[i]:
            return shown[i] if shown[i] is not None else i + 1
    return None


def refresh(path, tmp):
    doc = Document(str(path))
    els = list(doc.element.body)
    i0 = next(i for i, e in enumerate(els) if style(e) == "Title" and ptext(e).strip() == "DAFTAR ISI")
    i1 = next(i for i, e in enumerate(els) if i > i0 and style(e) == "Heading1")
    front = els[i0:i1]
    entries = entry_paragraphs(front)

    pdf = B.render_pdf_word(path, tmp)
    with fitz.open(str(pdf)) as d:
        texts = [norm(p.get_text()) for p in d]
        shown = [displayed_page(p) for p in d]
    # Badan dokumen dimulai pada halaman bernomor 1 yang didahului halaman bernomor lebih besar
    # (penomoran halaman awal dan penomoran badan dokumen terpisah).
    start = next((i for i in range(1, len(shown))
                  if shown[i] == 1 and shown[i - 1] not in (None, 0)), None)
    if start is None:
        first_needle = norm("".join((t.text or "") for t in entries[0][1][:-1]))[:70]
        start = next(i for i, t in enumerate(texts) if first_needle in t and ".........." not in t)

    changed, missing = [], []
    for p, ts in entries:
        text = norm("".join((t.text or "") for t in ts[:-1]))
        page = find_page(texts, shown, start, text[:70])
        if page is None:
            page = find_page(texts, shown, start, LABEL.sub("", text)[:70])
        if page is None:
            missing.append(text)
            continue
        old = (ts[-1].text or "").strip()
        if old != str(page):
            ts[-1].text = str(page)
            changed.append((text[:60], old, page))

    listed = {norm("".join((t.text or "") for t in ts[:-1])).split(" (")[0] for _, ts in entries}
    body_caps = [norm(ptext(e)).split(" (")[0] for e in els[i1:] if CAPTION.match(norm(ptext(e)))]
    unlisted = [c for c in body_caps if c not in listed and not any(l.startswith(c[:40]) for l in listed)]

    doc.save(str(path))
    final = B.render_pdf_word(path, tmp)
    shutil.copyfile(final, Path(path).with_suffix(".pdf"))
    return len(entries), changed, missing, unlisted


def main():
    for f in sys.argv[1:]:
        with tempfile.TemporaryDirectory() as td:
            n, changed, missing, unlisted = refresh(Path(f), td)
        print(f"== {f}: {n} entri; {len(changed)} nomor diubah")
        for t, o, nw in changed:
            print(f"   {o:>3} -> {nw:<3} {t}")
        if missing:
            print("   TIDAK DITEMUKAN pada badan dokumen:", missing)
        if unlisted:
            print("   keterangan belum ada di daftar:", unlisted)


if __name__ == "__main__":
    main()
