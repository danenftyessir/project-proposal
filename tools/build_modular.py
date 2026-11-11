"""Build the modular documents: one .docx per bab (I-IV), each in a clean and an editorial version.

Usage: python tools/build_modular.py [--only I II ...] [--clean-only | --editorial-only]
Needs: lxml, LibreOffice (env SOFFICE overrides the default path), pdftotext and pdfinfo on PATH.

Source of truth is the OFFICIAL full document (bab2/13523136-...-Draft-Bab2.docx), not tools/build_docx.py:
the official file carries hand edits (identity pages, glossaries, equations, Lampiran) that the build script
does not know. Each module keeps the front matter (cover, pengesahan, lembar identitas, daftar isi, lampiran,
gambar, tabel, singkatan, istilah), one bab, Daftar Pustaka, and Lampiran of the official file.

What differs from the official file, on purpose:
- Daftar Isi, Daftar Tabel, Daftar Lampiran are rebuilt for the one bab as real Word fields with page numbers
  measured from a LibreOffice render (the official file has them as static text). Word refreshes them on open.
- Heading numbering starts at the bab's own numeral (BAB II stays "BAB II", II.1 stays "II.1").
- Page-number restarts (cover lowerRoman, front matter start 1, body start 1) are restored, as in
  template/Template-Proposal-IF4091-Capstone-Individu-2026.docx; the official file lost them.
- Redundant empty page-break paragraphs (blank pages before bab II and before Lampiran) are dropped.
- Stale w:lastRenderedPageBreak hints (some precede w:rPr, which the schema forbids) are removed; Word re-creates them.
- The invalid attribute w:csTheme (official file, empty list paragraphs) is written as w:cstheme.
- The reference "cl:Yang, R., dkk." (a leaked Markdown prefix in the official file) is corrected and put back in A-Z order.
- Daftar Pustaka lists only what the bab cites (bab II: all entries; other babs cite nothing yet: placeholder).
  Daftar Singkatan and Daftar Istilah stay complete (team glossaries).
- Editorial version: the markers of the Markdown sources ({{...}}, [SESUAIKAN|PERLU VERIFIKASI|DATA BELUM ...])
  are inserted into the paragraphs of bab II and Daftar Pustaka, highlighted yellow, plus the citation-format note.

Modules are derived views: edits made in a module do not flow back into the official file.
"""
import argparse, copy, difflib, glob, hashlib, html, os, re, shutil, subprocess, sys, tempfile, zipfile
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab2.docx")
MD_DIR = os.path.join(ROOT, "bab2")
OUT_DIR = os.path.join(ROOT, "modular")
OUT_PREFIX = "13523136-Proposal-IF4091-Capstone-Individu-2026-Modular-Bab-"
SOFFICE = os.environ.get("SOFFICE", r"C:\Program Files\LibreOffice\program\soffice.exe")
ROMAN = ["I", "II", "III", "IV"]
REFS_IN = {"II"}        # babs whose body cites sources; the others get a placeholder (extend when Bab I/III/IV cite)

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
NS = 'xmlns:w="%s" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"' % W
q = lambda t: "{%s}%s" % (W, t)
esc = lambda s: html.escape(s, quote=False)
squash = lambda s: re.sub(r"\s+", " ", s).strip()

# ---------------------------------------------------------------- helpers on the XML tree
def style_of(p):
    s = p.find(q("pPr") + "/" + q("pStyle")) if etree.QName(p).localname == "p" else None
    return s.get(q("val")) if s is not None else ""

def text_of(el):
    return "".join(t.text or "" for t in el.iter(q("t")))

def has_sect(p):
    return etree.QName(p).localname == "p" and p.find(q("pPr") + "/" + q("sectPr")) is not None

def is_empty_pagebreak(p):
    return (etree.QName(p).localname == "p" and p.find(q("pPr") + "/" + q("pageBreakBefore")) is not None
            and not text_of(p).strip() and not has_sect(p) and p.find(".//" + q("drawing")) is None)

def toc_anchor(p):
    return [b.get(q("name")) for b in p.iter(q("bookmarkStart")) if b.get(q("name")).startswith("_Toc")][-1]

def frag(xml):
    return etree.fromstring("<root %s>%s</root>" % (NS, xml))[0]

# ---------------------------------------------------------------- Markdown editorial layer
def md_render(text, mode):
    """{{ed:X||cl:Y}}, {{ed:X}} and the older {{X||Y}} / {{X}}; clean mode also drops bracket markers."""
    def pick(m):
        body = m.group(1)
        ed, _, cl = body[3:].partition("||cl:") if body.startswith("ed:") else body.partition("||")
        return ed if mode == "editorial" else cl
    text = re.sub(r"\{\{(.*?)\}\}", pick, text, flags=re.S)
    if mode == "clean":
        text = re.sub(r"\s*\[(?:SESUAIKAN|PERLU VERIFIKASI|DATA BELUM)[^\]]*\]", "", text)
    return text

def plain(s):
    return squash(s.replace("*", ""))

def editorial_pairs():
    """{clean text: editorial text} for every paragraph / reference line of the Markdown sources that differs."""
    pairs = {}
    files = [os.path.join(MD_DIR, "Pembuka_Bab_II.md")] + sorted(glob.glob(os.path.join(MD_DIR, "II.[0-9]_*.md")))
    for f in files:
        md = open(f, encoding="utf8").read()
        if os.path.basename(f).startswith("Pembuka"):
            prose, refs = md.split("## Naskah")[1], ""
        else:
            prose = md.split("## Naskah")[1].split("## Daftar Pustaka")[0]
            refs = md.split("## Daftar Pustaka (sementara)")[1].split("## Lampiran kerja")[0]
        units = [" ".join(b.split("\n")) for b in re.split(r"\n\s*\n", prose.strip())] + refs.split("\n")
        for u in units:
            u = u.strip()
            if not u or u == "---" or u.startswith(("|", ">", "#", "$$")):
                continue
            cl, ed = plain(md_render(u, "clean")), plain(md_render(u, "editorial"))
            if cl != ed:
                pairs[cl] = ed
    return pairs

MARK = re.compile(r"(\[[A-Z][A-Z ]+[^\]]*\])")

def run_text(r):
    return "".join(t.text or "" for t in r.findall(q("t")))

def text_runs(p):
    """[(run, start, end)] for the runs of p that carry text."""
    out, pos = [], 0
    for r in p.iter(q("r")):
        if r.find(q("t")) is None:
            continue
        assert all(c.tag in (q("rPr"), q("t"), q("lastRenderedPageBreak")) for c in r), "unsupported run content"
        n = len(run_text(r)); out.append((r, pos, pos + n)); pos += n
    return out

def set_text(r, text):
    ts = r.findall(q("t"))
    for t in ts[1:]:
        r.remove(t)
    ts[0].text = text; ts[0].set(XML_SPACE, "preserve")

def split_at(p, i):
    """Make offset i a run boundary of p."""
    for r, s, e in text_runs(p):
        if s < i < e:
            txt, tail = run_text(r), copy.deepcopy(r)
            for x in tail.findall(q("lastRenderedPageBreak")):
                tail.remove(x)
            set_text(r, txt[:i - s]); set_text(tail, txt[i - s:]); r.addnext(tail)
            return

def marker_run(text, rpr, highlight):
    r = etree.Element(q("r"))
    rpr = copy.deepcopy(rpr)
    for tag in ("i", "iCs", "highlight"):
        for e in rpr.findall(q(tag)):
            rpr.remove(e)
    if highlight:
        hl = etree.Element(q("highlight")); hl.set(q("val"), "yellow")
        later = {q(t) for t in ("u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath")}
        at = next((k for k, e in enumerate(rpr) if e.tag in later), len(rpr))
        rpr.insert(at, hl)
    r.append(rpr)
    t = etree.SubElement(r, q("t")); t.text = text; t.set(XML_SPACE, "preserve")
    return r

def insert_editorial(p, clean, editorial):
    """Turn paragraph p (whose text is `clean`) into `editorial` by inserting runs; other formatting stays."""
    assert "".join(run_text(r) for r, _, _ in text_runs(p)) == clean, "paragraph text differs from Markdown: " + clean[:60]
    # diff on tokens with every [bracket marker] as one token, so a marker is never split across operations
    tok = lambda s: re.findall(r"\[[^\]]*\]|\s+|\w+|[^\w\s]", s)
    a, b = tok(clean), tok(editorial)
    ca = [0]; [ca.append(ca[-1] + len(t)) for t in a]
    cb = [0]; [cb.append(cb[-1] + len(t)) for t in b]
    ops = [(t, ca[i1], ca[i2], cb[j1], cb[j2]) for t, i1, i2, j1, j2 in
           difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if t != "equal"]
    for _, i1, i2, j1, j2 in reversed(ops):
        split_at(p, i1); split_at(p, i2)
        for r, s, e in text_runs(p):                               # drop clean[i1:i2] (replace)
            if i1 <= s and e <= i2 and e > s:
                r.getparent().remove(r)
        runs = text_runs(p)
        prev = next((r for r, s, e in runs if e == i1 and e > s), None)
        base = prev if prev is not None else runs[0][0]
        rpr = base.find(q("rPr"))
        rpr = rpr if rpr is not None else etree.Element(q("rPr"))
        new = [marker_run(s, rpr, bool(MARK.fullmatch(s))) for s in MARK.split(editorial[j1:j2]) if s]
        if prev is not None:
            anchor = prev
            for n in new:
                anchor.addnext(n); anchor = n
        else:
            for n in new:
                base.addprevious(n)
    assert "".join(run_text(r) for r, _, _ in text_runs(p)) == editorial, "editorial text mismatch"
    lit = {run_text(r) for r, _, _ in text_runs(p) if r.find(q("rPr") + "/" + q("highlight")) is not None}
    assert set(MARK.findall(editorial)) <= lit, "a marker was not highlighted: " + editorial[:60]

# ---------------------------------------------------------------- TOC / lists
NP = '<w:rPr><w:noProof/><w:webHidden/></w:rPr>'
MINOR = '<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>'
TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>'
TAB_DOT = '<w:tab w:val="right" w:leader="dot" w:pos="7927"/>'
TABS = {"TOC1": TAB_DOT, "TOC2": '<w:tab w:val="left" w:pos="800"/>' + TAB_DOT,
        "TOC3": '<w:tab w:val="left" w:pos="1200"/>' + TAB_DOT, "TableofFigures": TAB_DOT}

def pageref(anchor, page):
    return (f'<w:r>{NP}<w:tab/></w:r><w:r>{NP}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{NP}<w:instrText xml:space="preserve"> PAGEREF {anchor} \\h </w:instrText></w:r>'
            f'<w:r>{NP}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{NP}<w:t>{esc(str(page))}</w:t></w:r>'
            f'<w:r>{NP}<w:fldChar w:fldCharType="end"/></w:r>')

def entry(style, texts, anchor, page, bold=False):
    """One list entry: hyperlinked text runs separated by tabs, then a PAGEREF."""
    hl = f'<w:rPr><w:rStyle w:val="Hyperlink"/>{TNR}{"<w:b/><w:bCs/>" if bold else ""}<w:noProof/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>'
    body = f'<w:r>{hl}<w:t xml:space="preserve">{esc(texts[0])}</w:t></w:r>'
    for t in texts[1:]:
        body += (f'<w:r><w:rPr>{MINOR}<w:noProof/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:tab/></w:r>'
                 f'<w:r>{hl}<w:t xml:space="preserve">{esc(t)}</w:t></w:r>')
    nobold = '<w:b w:val="0"/>' if style == "TOC1" else ""
    ppr = (f'<w:pPr><w:pStyle w:val="{style}"/><w:tabs>{TABS[style]}</w:tabs><w:jc w:val="both"/>'
           f'<w:rPr>{MINOR}{nobold}<w:noProof/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:pPr>')
    return frag(f'<w:p>{ppr}<w:hyperlink w:anchor="{anchor}" w:history="1">{body}{pageref(anchor, page)}</w:hyperlink></w:p>')

def wrap_field(paras, instr):
    """Open a field in the first paragraph and close it at the end of the last one."""
    runs = [frag('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'),
            frag(f'<w:r><w:instrText xml:space="preserve"> {instr} </w:instrText></w:r>'),
            frag('<w:r><w:fldChar w:fldCharType="separate"/></w:r>')]
    ppr = paras[0].find(q("pPr"))
    at = list(paras[0]).index(ppr) + 1
    for k, el in enumerate(runs):
        paras[0].insert(at + k, el)
    paras[-1].append(frag('<w:r><w:fldChar w:fldCharType="end"/></w:r>'))

def number_headings(chunk, numeral):
    """[(level, number, title, anchor)] for the Heading1-3 paragraphs of a bab chunk."""
    out, cnt = [], [0, 0]
    for p in chunk:
        m = re.fullmatch(r"Heading([123])", style_of(p))
        if not m:
            continue
        lv = int(m.group(1))
        if lv == 1:
            cnt = [0, 0]; num = "BAB " + numeral
        elif lv == 2:
            cnt[0] += 1; cnt[1] = 0; num = f"{numeral}.{cnt[0]}"
        else:
            cnt[1] += 1; num = f"{numeral}.{cnt[0]}.{cnt[1]}"
        out.append((lv, num, squash(text_of(p)), toc_anchor(p)))
    return out

# ---------------------------------------------------------------- one module
def read_master():
    z = zipfile.ZipFile(MASTER)
    return [(i.filename, z.read(i.filename)) for i in z.infolist()]

def add_pgnum(sect, **attrs):
    for e in sect.findall(q("pgNumType")):
        sect.remove(e)
    pg = etree.Element(q("pgNumType"))
    for k, v in attrs.items():
        pg.set(q(k), v)
    sect.find(q("pgMar")).addnext(pg)

def placeholder(text, center=True, mark=False):
    if mark:
        return frag(f'<w:p><w:pPr><w:rPr><w:lang w:val="id-ID"/></w:rPr></w:pPr><w:r><w:rPr><w:highlight w:val="yellow"/><w:lang w:val="id-ID"/></w:rPr><w:t>{esc(text)}</w:t></w:r></w:p>')
    return frag(f'<w:p><w:pPr><w:jc w:val="{"center" if center else "both"}"/></w:pPr><w:r><w:rPr>{TNR}<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><w:t>{esc(text)}</w:t></w:r></w:p>')

def repair_refs(refs):
    """The official file shows the Markdown prefix "cl:" on one reference (and so sorts it under C): strip it, restore A-Z order."""
    for p in refs:
        r = text_runs(p)[0][0]
        set_text(r, re.sub(r"^(?:cl|ed):", "", run_text(r)))
    return sorted(refs, key=lambda p: re.sub(r"[^a-z0-9 ]", "", text_of(p).lower()))

BAB1_MD = os.path.join(ROOT, "bab1", "Bab_I_Draft.md")
BAB1_SHA12 = "71e7683087e6"          # DRAF 24; brief A01 2026-11-10. Ganti hanya bila brief baru menyebut hash baru.
BAB1_MARKS = {True: 60, False: 54}   # editorial: semua penanda; bersih: tanpa 6 penanda BENTUK BAKU
BODY_STRIP = ("b", "bCs", "i", "iCs", "u", "highlight", "vertAlign")
# Bab I cites exactly these entries (bab1/Bab_I_Draft.md, Catatan kerja "Sumber yang dirujuk"); prefixes of the official entries
BAB1_REFS = ("Dietrich, N.", "Jaganathan, G. S.", "Kementerian Kesehatan Republik Indonesia. (2021)",
             "Kementerian Kesehatan Republik Indonesia. (2022b)", "Kementerian Kesehatan Republik Indonesia. (2024)",
             "Li, Y., Lv, M.", "Simbolon, F.", "Skrabic, R.", "Susilo, D.", "Zeba, M.", "Zhang, H., Vithanage")
BAB1_DROP_CLEAN = re.compile(r"\s*\[PERLU VERIFIKASI BENTUK BAKU:[^\]]*\]")

def bab1_blocks():
    """[(kind, text)] of the "## Naskah" part of bab1/Bab_I_Draft.md: ("h1", ...), ("h2", title), ("p", text)."""
    raw = open(BAB1_MD, "rb").read()
    got = hashlib.sha256(raw).hexdigest()[:12]
    if got != BAB1_SHA12:
        sys.exit(f"bab1/Bab_I_Draft.md: sha256 {got} != {BAB1_SHA12} (draft changed since the brief); stop")
    md = raw.decode("utf8").replace("\r\n", "\n")
    if "\n## Naskah\n" not in md or "\n## Catatan kerja" not in md:
        sys.exit("bab1/Bab_I_Draft.md: '## Naskah' or '## Catatan kerja' heading not found")
    naskah = md.split("\n## Naskah\n", 1)[1].split("\n## Catatan kerja", 1)[0].strip()
    if naskah.endswith("---"):
        naskah = naskah[:-3].strip()
    out = []
    for b in re.split(r"\n\s*\n", naskah):
        b = " ".join(l.strip() for l in b.strip().split("\n"))
        if not b:
            continue
        if b.startswith("#"):
            m = re.fullmatch(r"## (?:BAB I PENDAHULUAN|I\.\d (.+))", b)
            assert m, "unexpected heading in Bab I Naskah: " + b
            out.append(("h1", "PENDAHULUAN") if m.group(1) is None else ("h2", m.group(1)))
        else:
            assert not b.startswith(("|", "- ", ">", "$$", "1. ")), "unsupported block in Bab I Naskah: " + b[:60]
            out.append(("p", b))
    assert [k for k, _ in out].count("h1") == 1 and out[0][0] == "h1" and [k for k, _ in out].count("h2") == 5
    return out

def bab1_run(text, base_rpr, italic=False, highlight=False, strip=BODY_STRIP):
    rpr = copy.deepcopy(base_rpr) if base_rpr is not None else etree.Element(q("rPr"))
    for tag in strip:
        for e in rpr.findall(q(tag)):
            rpr.remove(e)
    if italic:
        early = {q(t) for t in ("rStyle", "rFonts", "b", "bCs")}
        at = next((k for k, e in enumerate(rpr) if e.tag not in early), len(rpr))
        rpr.insert(at, etree.Element(q("i"))); rpr.insert(at + 1, etree.Element(q("iCs")))
    if highlight:
        later = {q(t) for t in ("u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath")}
        at = next((k for k, e in enumerate(rpr) if e.tag in later), len(rpr))
        hl = etree.Element(q("highlight")); hl.set(q("val"), "yellow"); rpr.insert(at, hl)
    r = etree.Element(q("r")); r.append(rpr)
    t = etree.SubElement(r, q("t")); t.text = text; t.set(XML_SPACE, "preserve")
    return r

def bab1_chunk(old, editorial, root):
    """New bab I chunk: official Heading1 kept; Heading2/body paragraphs cloned from the official bab I paragraphs."""
    assert style_of(old[0]) == "Heading1" and squash(text_of(old[0])) == "PENDAHULUAN"
    blocks = bab1_blocks()                          # hash check happens here, before anything is built
    h2 = next((p for p in old if style_of(p) == "Heading2"), None)
    body = next((p for p in old if etree.QName(p).localname == "p" and not style_of(p).startswith(("Heading", "Caption", "Title", "TOC"))
                 and len(text_of(p)) > 80 and p.find(q("pPr") + "/" + q("numPr")) is None and not has_sect(p)), None)
    if h2 is None or body is None:
        sys.exit("Bab I: no Heading2 or no body paragraph (>80 chars, not a list) in the official bab I to copy the format from; stop")
    first_run = lambda p: next((r for r in p.iter(q("r")) if r.find(q("t")) is not None), None)
    if first_run(body) is None or first_run(h2) is None:
        sys.exit("Bab I: template paragraph has no text run; stop")
    body_ppr, body_rpr = body.find(q("pPr")), first_run(body).find(q("rPr"))
    h2_ppr, h2_rpr = h2.find(q("pPr")), first_run(h2).find(q("rPr"))
    nid = max(int(b.get(q("id"))) for b in root.iter(q("bookmarkStart"))) + 1
    names = {b.get(q("name")) for b in root.iter(q("bookmarkStart"))}
    out, n_mark = [old[0]], 0
    for kind, text in blocks[1:]:
        p = etree.Element(q("p"))
        if kind == "h2":
            p.append(copy.deepcopy(h2_ppr))
            name = f"_Toc9{nid:08d}"
            assert name not in names, "bookmark name clash: " + name
            names.add(name)
            bs = etree.SubElement(p, q("bookmarkStart")); bs.set(q("id"), str(nid)); bs.set(q("name"), name)
            p.append(bab1_run(text, h2_rpr, strip=("highlight",)))   # heading keeps its own bold/caps formatting
            be = etree.SubElement(p, q("bookmarkEnd")); be.set(q("id"), str(nid)); nid += 1
        else:
            if not editorial:
                text = BAB1_DROP_CLEAN.sub("", text)
            p.append(copy.deepcopy(body_ppr))
            for seg in MARK.split(text):
                if not seg:
                    continue
                hl = editorial and bool(MARK.fullmatch(seg)); n_mark += bool(MARK.fullmatch(seg))
                for k, s in enumerate(re.split(r"\*([^*]+)\*", seg)):
                    if s:
                        assert "*" not in s, "stray asterisk in Bab I: " + s[:60]
                        p.append(bab1_run(s, body_rpr, italic=k % 2 == 1, highlight=hl))
        out.append(p)
    kept = [p for p in old[1:] if has_sect(p)]      # keep any section break of the official bab I
    if any(text_of(p).strip() for p in kept):
        sys.exit("Bab I: a section-break paragraph of the official bab I carries text; stop (would leak old content)")
    out += kept
    if n_mark != BAB1_MARKS[editorial]:
        sys.exit(f"Bab I ({'editorial' if editorial else 'clean'}): {n_mark} markers, expected {BAB1_MARKS[editorial]}; stop")
    print(f"Bab I ({'editorial' if editorial else 'clean'}): {len(out) - 1} paragraphs, {n_mark} markers")
    return out

def bab1_refs(refs):
    """The official Daftar Pustaka entries that Bab I cites; stop (do not guess) if any is missing or ambiguous."""
    out = []
    for key in BAB1_REFS:
        hit = [p for p in refs if squash(text_of(p)).startswith(key)]
        if len(hit) != 1:
            sys.exit(f"Bab I reference '{key}': {len(hit)} matches in the official Daftar Pustaka")
        out.append(hit[0])
    return sorted(out, key=lambda p: re.sub(r"[^a-z0-9 ]", "", text_of(p).lower()))

def build_module(parts, ci, editorial, pages, pairs):
    """Bytes of the module .docx for bab ROMAN[ci]; `pages` maps list keys to measured page labels."""
    numeral = ROMAN[ci]
    files = dict(parts)
    root = etree.fromstring(files["word/document.xml"])
    body = root.find(q("body"))
    kids = list(body)

    h1 = [i for i, k in enumerate(kids) if style_of(k) == "Heading1"]
    assert [squash(text_of(kids[i])) for i in h1] == ["PENDAHULUAN", "KAJIAN PUSTAKA", "ANALISIS MASALAH DAN RANCANGAN SOLUSI",
                                                      "RENCANA PELAKSANAAN"], "unexpected bab layout"
    pus = next(i for i, k in enumerate(kids) if i > h1[-1] and style_of(k) == "Title" and squash(text_of(k)) == "DAFTAR PUSTAKA")
    lamp = next(i for i, k in enumerate(kids) if style_of(k) == "Lampiran1")
    assert is_empty_pagebreak(kids[pus - 1]) and is_empty_pagebreak(kids[lamp - 1])
    front = kids[:h1[0]]
    chunk = kids[h1[ci]:(h1[ci + 1] if ci < 3 else pus - 1)]
    while is_empty_pagebreak(chunk[-1]):
        chunk.pop()
    refs, lamp_tail, final_sect = repair_refs(kids[pus + 2:lamp - 1]), kids[lamp:-1], kids[-1]
    assert has_sect(front[-1])
    if numeral == "I":
        chunk = bab1_chunk(chunk, editorial, root)

    # --- editorial layer (bab II text and its references)
    if editorial and numeral in REFS_IN:
        placed = set()
        for p in chunk + refs:
            key = text_of(p)
            if etree.QName(p).localname == "p" and not list(p.iter("{%s}oMath" % M)) and key in pairs:
                insert_editorial(p, key, pairs[key]); placed.add(key)
        assert placed == set(pairs), "editorial paragraphs not found in the document: " + "; ".join(k[:50] for k in set(pairs) - placed)

    # --- Daftar Pustaka entries
    if numeral in REFS_IN:
        ref_paras = list(refs)
        if editorial:
            ref_paras.insert(0, placeholder("[Format sitasi sementara (penulis-tahun). Menunggu pedoman program studi. "
                                            "Hapus catatan ini setelah format ditetapkan.]", mark=True))
    elif numeral == "I":
        ref_paras = bab1_refs(refs)
        if editorial:
            ref_paras.insert(0, placeholder("[Format sitasi sementara (penulis-tahun). Menunggu pedoman program studi. "
                                            "Hapus catatan ini setelah format ditetapkan.]", mark=True))
    else:
        ref_paras = [placeholder("<diisi sesuai sumber yang dirujuk pada bab ini>")]
        if editorial:
            ref_paras.append(placeholder(f"[DATA BELUM TERSEDIA: Bab {numeral} belum merujuk sumber. Format sitasi sementara "
                                         "penulis-tahun; menunggu pedoman program studi.]", mark=True))

    # --- Daftar Isi (the sdt keeps its heading paragraph and its closing paragraph)
    heads = number_headings(chunk, numeral)
    content = next(k for k in front if etree.QName(k).localname == "sdt").find(q("sdtContent"))
    for p in list(content)[1:-1]:
        content.remove(p)
    entries = [entry(f"TOC{lv}", [num + " " + title] if lv == 1 else [num, title], anchor, pages.get(f"{num} {title}", "1"), bold=(lv == 1))
               for lv, num, title, anchor in heads]
    wrap_field(entries, 'TOC \\o "1-3" \\h \\z \\u')
    for e in entries:
        content.insert(len(content) - 1, e)

    # --- Daftar Lampiran (the two template entries are replaced by entries for the Lampiran headings of the tail)
    lamps = [(squash(text_of(p)), style_of(p), toc_anchor(p)) for p in lamp_tail if style_of(p) in ("Lampiran1", "Lampiran2")]
    li = next(i for i, k in enumerate(front) if style_of(k) == "TOC1" and "Lampiran" in text_of(k))
    new = []
    for title, st, anchor in lamps:
        label = "Lampiran A." if st == "Lampiran1" else "A.1"
        top = st == "Lampiran1"
        new.append(entry("TOC1" if top else "TOC2", [f"{label} {title}"] if top else [label, title], anchor, pages.get(f"{label} {title}", "1"), bold=top))
    wrap_field(new, 'TOC \\h \\z \\t "Lampiran1;1;Lampiran2;2;Lampiran3;3"')
    assert style_of(front[li + 1]) == "TOC2"
    front[li:li + 2] = new

    # --- Daftar Tabel
    caps = [(squash(text_of(p)), toc_anchor(p)) for p in chunk if style_of(p) == "Caption" and text_of(p).startswith("Tabel")]
    ti = next(i for i, k in enumerate(front) if style_of(k) == "TableofFigures" and text_of(k).startswith("Tabel"))
    if caps:
        ents = [entry("TableofFigures", [cap], anchor, pages.get(cap, "1")) for cap, anchor in caps]
        wrap_field(ents, 'TOC \\h \\z \\c "Tabel"')
        front[ti:ti + 1] = ents
    else:
        front[ti] = placeholder("<jika diperlukan>")

    # --- sections: restore the page-number restarts the official file lost
    for k in front:
        if has_sect(k):
            sp = k.find(q("pPr") + "/" + q("sectPr"))
            cover = [r.get(q("type")) for r in sp.findall(q("footerReference"))] == ["even"]
            add_pgnum(sp, fmt="lowerRoman") if cover else add_pgnum(sp, start="1")
    add_pgnum(final_sect, start="1")

    for e in list(root.iter(q("lastRenderedPageBreak"))):   # stale render hints, some placed before w:rPr (schema-invalid)
        e.getparent().remove(e)
    for e in root.iter(q("rFonts")):                  # the official file has the invalid attribute w:csTheme (schema: w:cstheme)
        if q("csTheme") in e.attrib:
            e.set(q("cstheme"), e.attrib.pop(q("csTheme")))

    for k in list(body):
        body.remove(k)
    for k in front + chunk + [kids[pus - 1], kids[pus], kids[pus + 1]] + ref_paras + lamp_tail + [final_sect]:
        body.append(k)
    files["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    # --- heading numbering starts at the bab's own numeral
    num = files["word/numbering.xml"].decode("utf8")
    m = re.search(r'(<w:abstractNum w:abstractNumId="3".*?<w:lvl w:ilvl="0"><w:start w:val=")1("/>)', num, flags=re.S)
    assert m, "heading abstractNum not found"
    files["word/numbering.xml"] = (num[:m.start()] + m.group(1) + str(ci + 1) + m.group(2) + num[m.end():]).encode("utf8")

    # --- document properties
    core = files["docProps/core.xml"].decode("utf8")
    suffix = f" (Bab {numeral}, modular" + (", versi editorial)" if editorial else ")")
    files["docProps/core.xml"] = re.sub(r"</dc:title>", esc(suffix) + "</dc:title>", core, count=1).encode("utf8")

    out = tempfile.NamedTemporaryFile(delete=False, suffix=".docx"); out.close()
    with zipfile.ZipFile(out.name, "w", zipfile.ZIP_DEFLATED) as z:
        for name, _ in parts:
            z.writestr(name, files[name])
    data = open(out.name, "rb").read(); os.remove(out.name)
    # (list key, text to find in the render): the render numbers the child Lampiran "A." where Word shows "A.1"
    return data, heads, [(c, c) for c, _ in caps], [(f"{'Lampiran A.' if st == 'Lampiran1' else 'A.1'} {t}", f"{'Lampiran A. ' if st == 'Lampiran1' else ''}{t}") for t, st, _ in lamps]

# ---------------------------------------------------------------- page measurement
def render(docx, outdir):
    prof = "file:///" + os.path.join(outdir, "lo-profile").replace("\\", "/")
    subprocess.run([SOFFICE, "-env:UserInstallation=" + prof, "--headless", "--convert-to", "pdf", "--outdir", outdir, docx],
                   check=True, capture_output=True)
    return docx[:-5] + ".pdf"

def page_texts(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    out = []
    for p in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-enc", "UTF-8", "-f", str(p), "-l", str(p), "-layout", pdf, "-"], capture_output=True,
                           text=True, encoding="utf8", errors="replace").stdout.replace("\xa0", " ")
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        out.append((lines[-1] if lines and re.fullmatch(r"\d+|[ivxlc]+", lines[-1]) else "", squash(t)))
    return out

def measure(pdf, heads, caps, lamps):
    """{list key: printed page label}; headings are searched in order, starting at the first body page."""
    pg = page_texts(pdf)
    first = next(i for i, (lab, _) in enumerate(pg) if lab == "1")
    def find(key, start):
        for i in range(start, len(pg)):
            if squash(key) in pg[i][1]:
                return i
        sys.exit("not found in PDF: " + key)
    res, cur = {}, first
    for _, num, title, _ in heads:
        cur = find(f"{num} {title}", cur); res[f"{num} {title}"] = pg[cur][0]
    cur = first
    for key, needle in caps + lamps:
        i = find(needle, first if key.startswith("Tabel") else cur)
        res[key] = pg[i][0]
        if not key.startswith("Tabel"):
            cur = i
    return res, len(pg)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", choices=ROMAN, default=ROMAN)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--clean-only", action="store_true")
    g.add_argument("--editorial-only", action="store_true")
    a = ap.parse_args()
    versions = [False] if a.clean_only else [True] if a.editorial_only else [False, True]
    parts, pairs = read_master(), editorial_pairs()
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="modular_")
    for numeral in a.only:
        for editorial in versions:
            name = OUT_PREFIX + numeral + ("_Editorial" if editorial else "") + ".docx"
            pages = {}
            for attempt in range(4):
                data, heads, caps, lamps = build_module(parts, ROMAN.index(numeral), editorial, pages, pairs)
                path = os.path.join(tmp, name)
                open(path, "wb").write(data)
                measured, npages = measure(render(path, tmp), heads, caps, lamps)
                if measured == pages:
                    break
                pages = measured
            else:
                print("WARNING: page numbers did not settle for", name)
            dst = os.path.join(OUT_DIR, name)
            if numeral == "I" and os.path.exists(dst):          # backup before overwrite (brief A01 2026-11-10)
                bak_dir = os.path.join(ROOT, ".scratch", "backup_modular_bab1")
                os.makedirs(bak_dir, exist_ok=True)
                bak = os.path.join(bak_dir, name)
                if not os.path.exists(bak):                     # never overwrite the first backup
                    shutil.copy2(dst, bak)
            open(dst, "wb").write(data)
            print(f"{name}: {npages} halaman, nomor halaman daftar stabil setelah {attempt + 1} putaran")
    shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
