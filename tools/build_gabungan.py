"""Bangun docx gabungan proposal: Bab I-II (berkas resmi) + Bab III dan/atau Bab IV.

Kerangka: `13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2.docx`
(sampul, daftar isi, Bab I-II, daftar pustaka). Isi Bab III dan Bab IV diambil dari
`modular/TA1 bab 3.docx` dan `modular/TA1 bab 4.docx` (hasil `build_bab34_docx.py`)
sebagai pengganti teks panduan templat pada kerangka. Lalu:
  * entri Ijadi Maghsoodi dkk. (2026) ditambahkan ke daftar pustaka bila belum ada;
  * daftar isi (entri Bab III-IV), daftar gambar, dan daftar tabel disusun ulang;
  * nomor halaman dibaca dari ekspor PDF Microsoft Word (dua tahap), termasuk
    pembaruan nomor halaman entri Bab I-II.

Pemakaian (dari akar repositori):
    python tools/build_gabungan.py 3 --figure bab3/gambar/gambar-III-1.png
    python tools/build_gabungan.py 4 --figure bab3/gambar/gambar-III-1.png --figure4 bab4/gambar/gambar-IV-1.png
Hasil: docx dan PDF `...-Draft-Bab1-Bab2-Bab3` atau `...-Draft-Bab1-Bab2-Bab3-Bab4` di akar repositori.
"""
import argparse
import copy
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
import build_bab34_docx as B  # noqa: E402  (utilitas XML, parser Markdown, render Word)

PREFIX = "13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2"
BASE = ROOT / f"{PREFIX}.docx"
OUT = {3: ROOT / f"{PREFIX}-Bab3.docx", 4: ROOT / f"{PREFIX}-Bab3-Bab4.docx"}
SRC = {3: ROOT / "modular" / "TA1 bab 3.docx", 4: ROOT / "modular" / "TA1 bab 4.docx"}
MD = {3: ROOT / "bab3" / "Bab_III_Draft.md", 4: ROOT / "bab4" / "Bab_IV_Draft.md"}
TITLE = {3: "ANALISIS MASALAH DAN RANCANGAN SOLUSI", 4: "RENCANA PELAKSANAAN"}
ROMAN = {3: "III", 4: "IV"}
ptext, norm = B.ptext, B.norm
CAPTION = re.compile(r"^(Gambar|Tabel) [IVX]+\.\d+\. ")
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def style(e):
    s = e.find(".//" + qn("w:pStyle"))
    return s.get(qn("w:val")) if s is not None else ""


def find(els, pred, start=0):
    return next(i for i in range(start, len(els)) if pred(els[i]))


def is_chapter_title(e, chap):
    return style(e) == "Heading1" and ptext(e).strip() == TITLE[chap]


def heading_like(tpl, text):
    """Heading baru dari templat heading kerangka (numbering ikut daftar bertingkat kerangka)."""
    h = copy.deepcopy(tpl)
    for b in list(h):
        if b.tag in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
            h.remove(b)
    runs = h.findall(qn("w:r"))
    for r in runs[1:]:
        h.remove(r)
    ts = list(runs[0].iter(qn("w:t")))
    ts[0].text = text
    for t in ts[1:]:
        t.text = ""
    return h


def chapter_block(chap, tpl_h2, tpl_h3):
    """Elemen isi bab dari docx modular: setelah judul bab sampai sebelum daftar pustaka/lampiran.
    Heading subbab dibuat ulang dari templat kerangka agar penomorannya mengikuti kerangka."""
    els = list(Document(str(SRC[chap])).element.body)
    i_t = find(els, lambda e: is_chapter_title(e, chap))
    i_e = find(els, lambda e: ptext(e).strip() in ("DAFTAR PUSTAKA", "Contoh Judul Lampiran"), i_t)
    out = []
    for e in els[i_t + 1:i_e]:
        if e.tag in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
            continue
        s = style(e)
        if s in ("Heading2", "Heading3"):
            out.append(heading_like(tpl_h2 if s == "Heading2" else tpl_h3, ptext(e).strip()))
        else:
            out.append(copy.deepcopy(e))
    return out


def put_figure(block, doc, figure, docpr_id):
    """Daftarkan gambar pada dokumen gabungan dan arahkan blip blok bab ke sana."""
    blips = [b for e in block for b in e.iter(qn("a:blip"))]
    if figure is None:
        assert not blips, "blok bab memuat gambar, tetapi berkas gambarnya tidak diberikan"
        return
    rid, _ = doc.part.get_or_add_image(str(figure))
    assert len(blips) == 1, f"jumlah gambar pada blok bab: {len(blips)}"
    blips[0].set(qn("r:embed"), rid)
    for e in block:
        for dp in e.iter("{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr"):
            dp.set("id", str(docpr_id))


def add_bibliography(els):
    """Tambahkan entri pustaka yang belum ada, berurutan abjad (sebelum 'Kementerian ... (2021)')."""
    i_dp = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR PUSTAKA")
    key = "Ijadi Maghsoodi, A."
    if any(ptext(e).startswith(key) for e in els[i_dp:]):
        return
    ref = els[find(els, lambda e: ptext(e).startswith("HHS Office for Civil Rights. (2012)"), i_dp)]
    new = B.para(ref.find(qn("w:pPr")), B.inline_runs(B.md_bib_entry(key)))
    ref.addnext(new)


def clean_bookmarks(body):
    starts = {b.get(qn("w:id")) for b in body.iter(qn("w:bookmarkStart"))}
    for b in list(body.iter(qn("w:bookmarkEnd"))):
        if b.get(qn("w:id")) not in starts:
            b.getparent().remove(b)


def unwrap_hyperlinks(p):
    for h in list(p.iter(qn("w:hyperlink"))):
        parent = h.getparent()
        idx = parent.index(h)
        for k, child in enumerate(list(h)):
            parent.insert(idx + k, child)
        parent.remove(h)


def entry_paragraph(tpl, text, page):
    """Salin entri daftar isi templat: [teks][tab][nomor]; tautan dilepas (anchor tidak tersedia)."""
    el = copy.deepcopy(tpl)
    unwrap_hyperlinks(el)
    ts = [t for t in el.iter(qn("w:t"))]
    ts[0].text = text
    for t in ts[1:-1]:
        t.text = ""
    ts[-1].text = str(page)
    return el


def list_paragraph(ppr_src, text, page):
    p = B.make_el("w:p")
    ppr = copy.deepcopy(ppr_src)
    ind = ppr.find(qn("w:ind"))
    if ind is not None:
        ind.set(qn("w:right"), "720")  # teks panjang dipenggal sebelum nomor halaman
    p.append(ppr)
    r = B.make_el("w:r")
    rpr = B.make_el("w:rPr")
    rpr.append(B.make_el("w:rFonts", **{"w:ascii": "Times New Roman", "w:hAnsi": "Times New Roman",
                                        "w:cs": "Times New Roman", "w:eastAsia": "Times New Roman"}))
    rpr.append(B.make_el("w:sz", **{"w:val": 24}))
    r.append(rpr)
    t1 = B.make_el("w:t")
    t1.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t1.text = text
    r.append(t1)
    r.append(B.make_el("w:tab"))
    t2 = B.make_el("w:t")
    t2.text = str(page)
    r.append(t2)
    p.append(r)
    return p


def entry_text(p):
    ts = [t.text or "" for t in p.iter(qn("w:t"))]
    return norm("".join(ts[:-1]))


def build(chap_max, figure, pages, out_path, figure4=None):
    doc = Document(str(BASE))
    body = doc.element.body
    els = list(body)

    # --- isi Bab III dan (bila diminta) Bab IV ---------------------------------
    i3 = find(els, lambda e: is_chapter_title(e, 3))
    i4 = find(els, lambda e: is_chapter_title(e, 4), i3)
    i_dp = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR PUSTAKA", i4)
    tpl_h2 = next(e for e in els if style(e) == "Heading2" and ptext(e).startswith("Rekam Medis dan"))
    tpl_h3 = next(e for e in els if style(e) == "Heading3" and ptext(e).startswith("Kewajiban dan Isi"))
    new3 = chapter_block(3, tpl_h2, tpl_h3)
    put_figure(new3, doc, figure, 9001)
    new4 = chapter_block(4, tpl_h2, tpl_h3) if chap_max >= 4 else None
    if new4:
        put_figure(new4, doc, figure4, 9002)
    for e in els[i3 + 1:i4] + (els[i4 + 1:i_dp] if new4 else els[i4 + 1:i4 + 1]):
        body.remove(e)
    a = els[i3]
    for e in new3:
        a.addnext(e)
        a = e
    if new4:
        a = els[i4]
        for e in new4:
            a.addnext(e)
            a = e
    add_bibliography(list(body))
    clean_bookmarks(body)
    # Daftar pustaka dimulai di halaman baru agar tidak menempel pada akhir bab terakhir.
    dp = next(e for e in body if style(e) == "Title" and ptext(e).strip() == "DAFTAR PUSTAKA")
    dp_ppr = dp.find(qn("w:pPr"))
    old = dp_ppr.find(qn("w:pageBreakBefore"))
    if old is not None:
        old.set(qn("w:val"), "1")
    else:
        pos = 1 if dp_ppr.find(qn("w:pStyle")) is not None else 0
        dp_ppr.insert(pos, B.make_el("w:pageBreakBefore", **{"w:val": 1}))

    # --- daftar isi ------------------------------------------------------------
    els = list(body)
    sdt = next(e for e in els if e.tag == qn("w:sdt"))
    cont = sdt.find(qn("w:sdtContent"))
    paras = cont.findall(qn("w:p"))
    tpl0 = next(p for p in paras if ptext(p).startswith("BAB III"))
    tpl1 = next(p for p in paras if re.match(r"^III\.1 ", ptext(p)))
    tpl2 = next(p for p in paras if re.match(r"^II\.1\.1 ", ptext(p)))
    end_run = None
    for p in paras:
        for r in p.findall(qn("w:r")):
            f = r.find(qn("w:fldChar"))
            if f is not None and f.get(qn("w:fldCharType")) == "end":
                end_run = r
    old_keep = [p for p in paras if not (ptext(p).startswith(("BAB III", "BAB IV"))
                                          or re.match(r"^(III|IV)\.", ptext(p)))]
    for p in paras:
        cont.remove(p)
    for p in old_keep:
        t = entry_text(p)
        # nomor halaman entri lama diperbarui dari render; teks tidak diubah
        ts = [x for x in p.iter(qn("w:t"))]
        ts[-1].text = str(pages.get(t, ts[-1].text))
        cont.append(p)
    spec = []  # (templat, teks)
    for c in (3, 4):
        spec.append((tpl0, f"BAB {ROMAN[c]} {TITLE[c]}"))
        if c <= chap_max:
            for kind, key, val in B.parse_md(MD[c]):
                if kind == "h2":
                    spec.append((tpl1, f"{key} {val}"))
                elif kind == "h3":
                    spec.append((tpl2, f"{key} {val}"))
    last = None
    for tpl, text in spec:
        last = entry_paragraph(tpl, text, pages.get(norm(text), 0))
        cont.append(last)
    if end_run is not None:
        last.append(end_run)
    # Jarak antarentri dirapatkan (60 -> 20 twip) agar daftar isi tidak menyisakan beberapa baris
    # di halaman tersendiri setelah entri Bab III-IV bertambah.
    for p in cont.findall(qn("w:p")):
        sp = p.find(qn("w:pPr") + "/" + qn("w:spacing"))
        if sp is not None:
            sp.set(qn("w:before"), "20")

    # --- daftar gambar dan daftar tabel ----------------------------------------
    els = list(body)
    i_front = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR ISTILAH")
    i_body = find(els, lambda e: ptext(e).strip() == "BAB I", i_front)
    caps = [norm(ptext(e)) for e in els[i_body:] if CAPTION.match(norm(ptext(e)))]
    figs = [c.split(" (")[0] for c in caps if c.startswith("Gambar")]
    tabs = [c for c in caps if c.startswith("Tabel")]
    i_g = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR GAMBAR")
    i_t = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR TABEL", i_g)
    i_s = find(els, lambda e: style(e) == "Title" and ptext(e).strip() == "DAFTAR SINGKATAN", i_t)
    ppr_src = next(e for e in els[i_t:i_s] if ptext(e).startswith("Tabel II.1")).find(qn("w:pPr"))
    ppr_src = copy.deepcopy(ppr_src)
    for seg_start, seg_end, items in ((i_g, i_t, figs), (i_t, i_s, tabs)):
        seg = els[seg_start + 1:seg_end]
        for e in seg:
            if ptext(e).strip() and e.tag == qn("w:p"):
                body.remove(e)
        a = els[seg_start]
        for text in items:
            p = list_paragraph(ppr_src, text, pages.get(text, 0))
            a.addnext(p)
            a = p
    doc.save(str(out_path))
    return [t for _, t in spec], figs, tabs, [entry_text(p) for p in old_keep]


def displayed_page(page):
    """Nomor halaman tercetak: blok numerik terbawah pada halaman."""
    nums = [b for b in page.get_text("blocks") if re.fullmatch(r"\s*\d+\s*", b[4])]
    return int(nums[-1][4]) if nums else None


def locate_pages(pdf, keys):
    with fitz.open(str(pdf)) as d:
        texts = [norm(p.get_text()) for p in d]
        shown = [displayed_page(p) for p in d]
    start = next(i for i, t in enumerate(texts) if "BAB I PENDAHULUAN" in t and "DAFTAR ISI" not in t)
    out = {}
    for k in keys:
        needle = norm(k)[:70]
        for i in range(start, len(texts)):
            if needle in texts[i]:
                out[norm(k)] = shown[i] if shown[i] is not None else i + 1
                break
        else:
            raise RuntimeError(f"Tidak ditemukan di PDF: {k}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("upto", type=int, choices=[3, 4], help="bab terakhir yang disertakan")
    ap.add_argument("--figure", type=Path, required=True, help="gambar Bab III")
    ap.add_argument("--figure4", type=Path, help="gambar Bab IV (Gantt chart)")
    a = ap.parse_args()
    out = OUT[a.upto]
    with tempfile.TemporaryDirectory() as td:
        heads, figs, tabs, old = build(a.upto, a.figure, {}, out, a.figure4)
        pdf = B.render_pdf_word(out, td)
        pages = locate_pages(pdf, heads + figs + tabs + old)
        build(a.upto, a.figure, pages, out, a.figure4)
        pdf = B.render_pdf_word(out, td)
        shutil.copyfile(pdf, out.with_suffix(".pdf"))
    for k in heads + figs + tabs:
        print(f"{pages[norm(k)]:>4}  {k[:90]}")
    print("Tersimpan:", out, "dan", out.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
