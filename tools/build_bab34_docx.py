"""Bangun docx modular Bab III dan Bab IV dari naskah Markdown.

Kerangka diambil dari `modular/TA1 bab 2.docx` (halaman judul, lembar
pengesahan, gaya, penomoran heading otomatis "BAB %1"), lalu:
  * isi Bab II diganti isi Markdown (`## Naskah` ke bawah);
  * daftar isi, daftar gambar, dan daftar tabel disusun ulang;
  * daftar pustaka hanya memuat sumber yang dikutip bab tersebut
    (entri diambil dari docx Bab II; yang belum ada diambil dari
    `bab2/Daftar_Pustaka.md`).

Nomor halaman daftar isi/gambar/tabel diisi lewat dua tahap: docx dibuat,
dirender ke PDF dengan LibreOffice, lalu nomor halaman dibaca dari PDF.

Pemakaian:
    python tools/build_bab34_docx.py 3 --figure path/ke/gambar-III-1.png
    python tools/build_bab34_docx.py 4
"""
import argparse
import copy
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from docx.shared import Cm
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "modular" / "TA1 bab 2.docx"
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

CHAPTERS = {
    3: dict(md=ROOT / "bab3" / "Bab_III_Draft.md", roman="III",
            title="ANALISIS MASALAH DAN RANCANGAN SOLUSI",
            out=ROOT / "modular" / "TA1 bab 3.docx"),
    4: dict(md=ROOT / "bab4" / "Bab_IV_Draft.md", roman="IV",
            title="RENCANA PELAKSANAAN",
            out=ROOT / "modular" / "TA1 bab 4.docx"),
}

# Lebar kolom (dxa, total 8325) dan ukuran huruf (half-point) per tabel.
TABLE_LAYOUT = {
    "III.1": ([1450, 2150, 1500, 3225], 20),
    "III.2": ([1450, 3550, 1700, 1625], 20),
    "III.3": ([2100, 6225], 20),
    "IV.1": ([2725] + [280] * 20, 16),
    "IV.2": ([560, 1900, 860, 1950, 3055], 20),
}

# Sumber yang dikutip Bab III -> awalan entri daftar pustaka (APA).
BIB_KEYS = {
    3: [
        "Dietrich, N., & Stubbert, B. (2026)",
        "Gao, Y., Dligach, D., Miller, T., Churpek",
        "Gao, Y., Dligach, D., Miller, T., Tesch",
        "Gao, Y., Xiong, Y.",
        "HHS Office for Civil Rights. (2012)",
        "Ijadi Maghsoodi, A.",
        "Kementerian Kesehatan Republik Indonesia. (2021)",
        "Kementerian Kesehatan Republik Indonesia. (2022b)",
        "Kementerian Kesehatan Republik Indonesia. (2024)",
        "Li, Y., Lv, M.",
        "Murali, L.",
        "Nadi, D. T., & Fortunandha",
        "Oktavia Az, I. S., & Sonia",
        "Republik Indonesia. (2022)",
        "Wong, E. Y. T.",
        "Xiao, G.",
        "Zeba, M.",
        "Zhang, H., Vithanage",
    ],
    4: [],
}


# ---------------------------------------------------------------------------
# Utilitas XML
# ---------------------------------------------------------------------------
def ptext(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def strip_bookmarks(el):
    for tag in ("w:bookmarkStart", "w:bookmarkEnd"):
        for b in list(el.iter(qn(tag))):
            b.getparent().remove(b)
    return el


def make_el(tag, **attrs):
    from docx.oxml import OxmlElement
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn(k), str(v))
    return e


def run(text, italic=False, bold=False, size=None, font=None):
    r = make_el("w:r")
    rpr = make_el("w:rPr")
    if font:
        rpr.append(make_el("w:rFonts", **{"w:ascii": font, "w:cs": font,
                                         "w:eastAsia": font, "w:hAnsi": font}))
    if bold:
        rpr.append(make_el("w:b", **{"w:val": 1}))
        rpr.append(make_el("w:bCs", **{"w:val": 1}))
    if italic:
        rpr.append(make_el("w:i", **{"w:val": 1}))
        rpr.append(make_el("w:iCs", **{"w:val": 1}))
    if size:
        rpr.append(make_el("w:sz", **{"w:val": size}))
        rpr.append(make_el("w:szCs", **{"w:val": size}))
    r.append(rpr)
    t = make_el("w:t")
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    r.append(t)
    return r


def inline_runs(text, **kw):
    """Markdown *miring* -> run bergantian tegak/miring."""
    out = []
    for i, part in enumerate(re.split(r"\*([^*]+)\*", text)):
        if part:
            out.append(run(part, italic=(i % 2 == 1) or kw.get("italic", False),
                           bold=kw.get("bold", False), size=kw.get("size"),
                           font=kw.get("font")))
    return out


def para(ppr_xml_from=None, runs=()):
    p = make_el("w:p")
    if ppr_xml_from is not None:
        p.append(copy.deepcopy(ppr_xml_from))
    for r in runs:
        p.append(r)
    return p


def ppr(**spec):
    """pPr sederhana: spacing, ind, jc, keepNext, numPr."""
    pp = make_el("w:pPr")
    if spec.get("keepNext"):
        pp.append(make_el("w:keepNext", **{"w:val": 1}))
    if "num" in spec:
        numpr = make_el("w:numPr")
        numpr.append(make_el("w:ilvl", **{"w:val": 0}))
        numpr.append(make_el("w:numId", **{"w:val": spec["num"]}))
        pp.append(numpr)
    if "spacing" in spec:
        a, b, line = spec["spacing"]
        attrs = {"w:after": a, "w:before": b, "w:lineRule": "auto"}
        if line:
            attrs["w:line"] = line
        pp.append(make_el("w:spacing", **attrs))
    if "ind" in spec:
        pp.append(make_el("w:ind", **spec["ind"]))
    if "jc" in spec:
        pp.append(make_el("w:jc", **{"w:val": spec["jc"]}))
    return pp


# ---------------------------------------------------------------------------
# Parser Markdown naskah
# ---------------------------------------------------------------------------
def parse_md(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "## Naskah")
    lines = lines[start + 1:]
    blocks, i = [], 0
    while i < len(lines):
        l = lines[i].rstrip()
        if not l.strip():
            i += 1
            continue
        if l.startswith("## BAB "):
            i += 1
            continue
        m = re.match(r"^(#{2,3}) ([IVX]+(?:\.\d+)+) (.+)$", l)
        if m:
            blocks.append(("h2" if len(m.group(1)) == 2 else "h3", m.group(2), m.group(3)))
            i += 1
            continue
        if l.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            blocks.append(("figure", None, None))
            i = j + 1
            continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"-{3,}", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", None, rows))
            continue
        m = re.match(r"^(\d+)\. (.+)$", l)
        if m:
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i]).strip())
                i += 1
            blocks.append(("ol", None, items))
            continue
        m = re.match(r"^(Tabel|Gambar) ([IVX]+\.\d+)\. (.+)$", l)
        if m:
            blocks.append(("tcap" if m.group(1) == "Tabel" else "fcap", m.group(2), l))
            i += 1
            continue
        if l.startswith("Keterangan:"):
            blocks.append(("note", None, l))
            i += 1
            continue
        blocks.append(("p", None, l.strip()))
        i += 1
    return blocks


# ---------------------------------------------------------------------------
# Tabel
# ---------------------------------------------------------------------------
def build_table(rows, tblpr_tpl, widths, size, allow_split=False):
    tbl = make_el("w:tbl")
    tblpr = copy.deepcopy(tblpr_tpl)
    tblw = tblpr.find(qn("w:tblW"))
    tblw.set(qn("w:w"), str(sum(widths)))
    tbl.append(tblpr)
    grid = make_el("w:tblGrid")
    for w in widths:
        grid.append(make_el("w:gridCol", **{"w:w": w}))
    tbl.append(grid)
    narrow = len(widths) > 6  # tabel jadwal mingguan
    for ri, row in enumerate(rows):
        tr = make_el("w:tr")
        trpr = make_el("w:trPr")
        trpr.append(make_el("w:cantSplit", **{"w:val": 0 if allow_split else 1}))
        if ri == 0:
            trpr.append(make_el("w:tblHeader", **{"w:val": 1}))
        tr.append(trpr)
        for ci, cell in enumerate(row):
            tc = make_el("w:tc")
            tcpr = make_el("w:tcPr")
            tcpr.append(make_el("w:tcW", **{"w:w": widths[ci], "w:type": "dxa"}))
            if narrow:
                mar = make_el("w:tcMar")
                for side in ("left", "right"):
                    mar.append(make_el(f"w:{side}", **{"w:w": 15, "w:type": "dxa"}))
                tcpr.append(mar)
            tcpr.append(make_el("w:vAlign", **{"w:val": "center" if (ri == 0 or narrow) else "top"}))
            tc.append(tcpr)
            center = ri == 0 or (narrow and ci > 0)
            spec = dict(spacing=(20, 20, 240), jc="center" if center else "left")
            if narrow and ri < len(rows) - 1:
                spec["keepNext"] = True  # tabel jadwal tidak dipotong halaman
            p = para(ppr(**spec),
                     inline_runs(cell, bold=(ri == 0), size=size, font="Times New Roman"))
            if not cell:
                p.append(run("", size=size))
            tc.append(p)
            tr.append(tc)
        tbl.append(tr)
    return tbl


# ---------------------------------------------------------------------------
# Daftar pustaka
# ---------------------------------------------------------------------------
def md_bib_entry(prefix):
    for l in (ROOT / "bab2" / "Daftar_Pustaka.md").read_text(encoding="utf-8").splitlines():
        if l.startswith(prefix):
            return l.strip()
    raise KeyError(prefix)


def bib_paragraph_from_md(text, ppr_tpl):
    """Entri APA dari Markdown; *x* menjadi miring, URL tetap teks biasa."""
    return para(ppr_tpl, inline_runs(text))


# ---------------------------------------------------------------------------
# Pembangunan dokumen
# ---------------------------------------------------------------------------
def build(chap, figure, pages=None):
    cfg = CHAPTERS[chap]
    R = cfg["roman"]
    doc = Document(str(BASE))
    body = doc.element.body
    els = list(body)

    def find(pred, start=0):
        return next(i for i in range(start, len(els)) if pred(els[i]))

    # --- penanda bagian pada kerangka -------------------------------------
    i_toc = find(lambda e: ptext(e).strip() == "DAFTAR ISI")
    i_lamp = find(lambda e: ptext(e).strip() == "DAFTAR LAMPIRAN")
    i_gbr = find(lambda e: ptext(e).strip() == "DAFTAR GAMBAR")
    i_tbl = find(lambda e: ptext(e).strip() == "DAFTAR TABEL")
    i_sing = find(lambda e: ptext(e).strip() == "DAFTAR SINGKATAN")
    i_title = find(lambda e: ptext(e).strip() == "KAJIAN PUSTAKA" and e.find(".//" + qn("w:pStyle")) is not None
                   and e.find(".//" + qn("w:pStyle")).get(qn("w:val")) == "Heading1")
    i_dp = find(lambda e: ptext(e).strip() == "DAFTAR PUSTAKA", i_title)
    i_lampiran = find(lambda e: ptext(e).strip() == "Contoh Judul Lampiran", i_dp)

    # templat dari Bab II
    toc_tpl = {
        0: copy.deepcopy(els[find(lambda e: ptext(e).startswith("BAB II KAJIAN PUSTAKA"), i_toc)]),
        1: copy.deepcopy(els[find(lambda e: re.match(r"II\.1 ", ptext(e)) is not None, i_toc)]),
        2: copy.deepcopy(els[find(lambda e: re.match(r"II\.1\.1 ", ptext(e)) is not None, i_toc)]),
    }
    gbr_tpl = copy.deepcopy(els[find(lambda e: ptext(e).startswith("Gambar II.1."), i_gbr)])
    tbl_list_tpl = copy.deepcopy(els[find(lambda e: ptext(e).startswith("Tabel II.1."), i_tbl)])
    h2_tpl = strip_bookmarks(copy.deepcopy(els[find(
        lambda e: e.find(".//" + qn("w:pStyle")) is not None
        and e.find(".//" + qn("w:pStyle")).get(qn("w:val")) == "Heading2", i_title)]))
    h3_tpl = strip_bookmarks(copy.deepcopy(els[find(
        lambda e: e.find(".//" + qn("w:pStyle")) is not None
        and e.find(".//" + qn("w:pStyle")).get(qn("w:val")) == "Heading3", i_title)]))
    body_ppr = copy.deepcopy(els[find(lambda e: ptext(e).startswith("Keputusan Menteri Kesehatan (KMK) Nomor HK.01.07/MENKES/1596/2024 merinci"), i_title)].find(qn("w:pPr")))
    i_tcap = find(lambda e: ptext(e).startswith("Tabel II.1."), i_title)
    tcap_ppr = copy.deepcopy(els[i_tcap].find(qn("w:pPr")))
    tblpr_tpl = copy.deepcopy(els[i_tcap + 1].find(qn("w:tblPr")))
    i_fcap = find(lambda e: ptext(e).startswith("Gambar II.1."), i_title)
    fcap_ppr = copy.deepcopy(els[i_fcap].find(qn("w:pPr")))
    fimg_ppr = copy.deepcopy(els[i_fcap - 1].find(qn("w:pPr")))
    bib_old = {ptext(e): copy.deepcopy(e) for e in els[i_dp + 1:i_lampiran] if ptext(e).strip()}
    bib_ppr = copy.deepcopy(next(iter(bib_old.values())).find(qn("w:pPr")))

    # --- penomoran: BAB %1 mulai dari bab ini; daftar bernomor baru -------
    numbering = doc.part.numbering_part.element
    for an in numbering.findall(qn("w:abstractNum")):
        if an.get(qn("w:abstractNumId")) == "1":
            lvl0 = an.find(qn("w:lvl"))
            lvl0.find(qn("w:start")).set(qn("w:val"), str(chap))
    num_ids = [int(n.get(qn("w:numId"))) for n in numbering.findall(qn("w:num"))]
    list_num = max(num_ids) + 1
    num = make_el("w:num", **{"w:numId": list_num})
    num.append(make_el("w:abstractNumId", **{"w:val": 3}))
    ov = make_el("w:lvlOverride", **{"w:ilvl": 0})
    ov.append(make_el("w:startOverride", **{"w:val": 1}))
    num.append(ov)
    numbering.append(num)

    # --- judul bab ---------------------------------------------------------
    title_el = els[i_title]
    ts = list(title_el.iter(qn("w:t")))
    ts[0].text = cfg["title"]

    # --- isi bab -------------------------------------------------------------
    for e in els[i_title + 1:i_dp]:
        body.remove(e)
    anchor = title_el
    blocks = parse_md(cfg["md"])
    toc_entries = [(0, f"BAB {R} {cfg['title']}")]
    figs, tabs = [], []
    pending_table = None

    def put(el):
        nonlocal anchor
        anchor.addnext(el)
        anchor = el

    for kind, key, val in blocks:
        if kind in ("h2", "h3"):
            h = copy.deepcopy(h2_tpl if kind == "h2" else h3_tpl)
            rs = h.findall(qn("w:r"))
            for r in rs[1:]:
                h.remove(r)
            rs[0].find(qn("w:t")).text = val
            put(h)
            toc_entries.append((1 if kind == "h2" else 2, f"{key} {val}"))
        elif kind == "p":
            put(para(body_ppr, inline_runs(val)))
        elif kind == "note":
            put(para(ppr(spacing=(240, 60, 240), jc="left"),
                     inline_runs(val, size=20)))
        elif kind == "tcap":
            p = para(tcap_ppr, inline_runs(val))
            pp = p.find(qn("w:pPr"))
            pp.insert(0, make_el("w:keepNext", **{"w:val": 1}))
            put(p)
            pending_table = key
            tabs.append(val)
        elif kind == "table":
            widths, size = TABLE_LAYOUT[pending_table]
            put(build_table(val, tblpr_tpl, widths, size,
                            allow_split=(pending_table == "IV.2")))
            pending_table = None
        elif kind == "ol":
            for item in val:
                put(para(ppr(num=list_num, spacing=(60, 60, None),
                             ind={"w:left": 720, "w:hanging": 360}, jc="both"),
                         inline_runs(item)))
        elif kind == "figure":
            tmp = doc.add_paragraph()
            tmp.add_run().add_picture(str(figure), width=Cm(13.5))
            r_el = tmp._p.find(qn("w:r"))
            body.remove(tmp._p)
            put(para(fimg_ppr, [r_el]))
        elif kind == "fcap":
            put(para(fcap_ppr, inline_runs(val)))
            figs.append(val)

    # --- daftar pustaka ------------------------------------------------------
    for e in els[i_dp + 1:i_lampiran]:
        body.remove(e)
    dp_title = els[i_dp]
    if BIB_KEYS[chap]:
        entries = []
        for k in BIB_KEYS[chap]:
            hit = [t for t in bib_old if t.startswith(k)]
            if len(hit) == 1:
                entries.append((hit[0], bib_old[hit[0]]))
            elif not hit:
                txt = md_bib_entry(k)
                entries.append((re.sub(r"\*", "", txt), bib_paragraph_from_md(txt, bib_ppr)))
            else:
                raise RuntimeError(f"Kunci pustaka ganda: {k}")
        entries.sort(key=lambda x: x[0].lower())
        a = dp_title
        for _, el in entries:
            a.addnext(el)
            a = el
    else:
        body.remove(dp_title)

    # --- daftar isi / gambar / tabel ----------------------------------------
    def set_entry(tpl, text, page):
        el = copy.deepcopy(tpl)
        ts = list(el.iter(qn("w:t")))
        ts[0].text = text
        ts[-1].text = str(page)
        return el

    def replace_entries(i_head, i_next, pattern, new_els):
        seg = els[i_head + 1:i_next]
        olds = [e for e in seg if re.match(pattern, ptext(e))]
        if olds:
            a = olds[0].getprevious()
            for e in olds:
                body.remove(e)
        else:
            a = els[i_head]
        for el in new_els:
            a.addnext(el)
            a = el

    pg = pages or {}
    replace_entries(i_toc, i_lamp, r"^(BAB II |II\.)",
                    [set_entry(toc_tpl[lv], t, pg.get(t, 0)) for lv, t in toc_entries])
    replace_entries(i_gbr, i_tbl, r"^Gambar II\.",
                    [set_entry(gbr_tpl, f.split(" (")[0], pg.get(f, 0)) for f in figs])
    replace_entries(i_tbl, i_sing, r"^Tabel II\.",
                    [set_entry(tbl_list_tpl, t, pg.get(t, 0)) for t in tabs])

    doc.save(str(cfg["out"]))
    return toc_entries, figs, tabs


# ---------------------------------------------------------------------------
# Nomor halaman dari render PDF
# ---------------------------------------------------------------------------
def render_pdf(docx_path, outdir):
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir",
                    str(outdir), str(docx_path)], check=True, capture_output=True)
    return Path(outdir) / (docx_path.stem + ".pdf")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def page_map(pdf, chap, toc_entries, figs, tabs):
    cfg = CHAPTERS[chap]
    with fitz.open(str(pdf)) as d:
        texts = [norm(p.get_text()) for p in d]
    first_heading = toc_entries[1][1]
    # Halaman 1 bab = halaman tempat subbab pertama muncul di luar daftar isi.
    # (LibreOffice mengabaikan pageBreakBefore=0 pada heading judul bab sehingga
    # "BAB N" terpisah satu halaman; Word menaruhnya pada halaman yang sama.)
    start = next(i for i, t in enumerate(texts)
                 if first_heading in t and "DAFTAR ISI" not in t
                 and not re.search(re.escape(first_heading) + r"\.{3,}", t))
    pages = {toc_entries[0][1]: 1}

    def locate(needle):
        for i in range(start, len(texts)):
            if needle in texts[i]:
                return i - start + 1
        raise RuntimeError(f"Tidak ditemukan di PDF: {needle}")

    for lv, t in toc_entries[1:]:
        pages[t] = locate(t)
    for c in figs + tabs:
        pages[c] = locate(norm(c)[:60])
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", type=int, choices=[3, 4])
    ap.add_argument("--figure", type=Path, help="PNG untuk blok ```mermaid (Bab III)")
    a = ap.parse_args()
    cfg = CHAPTERS[a.chapter]
    toc, figs, tabs = build(a.chapter, a.figure)
    with tempfile.TemporaryDirectory() as td:
        pdf = render_pdf(cfg["out"], td)
        pages = page_map(pdf, a.chapter, toc, figs, tabs)
    build(a.chapter, a.figure, pages)
    for k, v in pages.items():
        print(f"{v:>3}  {k[:90]}")
    print("Tersimpan:", cfg["out"])


if __name__ == "__main__":
    main()
