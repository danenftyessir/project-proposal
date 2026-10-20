import re, html, shutil, os, subprocess, tempfile, json

"""Build the Bab II draft .docx from the Markdown subbab files and the Individu template
(template/Template-Proposal-IF4091-Capstone-Individu-2026.docx, byte-identical to the user's "... - Copy.docx").
The Utama template (three-person team) is NOT used for this draft.

Usage: python3 -I tools/build_docx.py
Needs the docx skill scripts (merge_runs.py); set DOCX_SKILL_DIR if the default path differs.
Add a subbab by pointing its OUTLINE entry to a Markdown file (None = highlighted placeholder).
Validate afterwards with the skill's scripts/office/validate.py and render with soffice.py.
"""
S = tempfile.mkdtemp(prefix="bab2_build_")
SK = os.environ.get("DOCX_SKILL_DIR", "/root/.claude/skills/synced/017185de-19fa-4709-a10a-3db50e5d500d_a2aeaf02-31ea-42d9-a648-645d5f31836f/docx")
REPO = "/home/user/project-proposal"
TEMPLATE = REPO + "/template/Template-Proposal-IF4091-Capstone-Individu-2026.docx"
OUT = REPO + "/bab2/Proposal-IF4091-Capstone-Individu-2026_Draft-Bab2.docx"
OPEN = REPO + "/bab2/Pembuka_Bab_II.md"   # replaces the template guidance text at the start of Bab II; set to None to keep it

# Identity (given by the user in chat; do not invent other names, dates, supervisors or teammates)
NAMA = "Danendra Shafi Athallah"
NIM = "13523136"
JUDUL_CAPSTONE = "Perancangan Antarmuka User-Centered untuk Sistem Pemeriksaan Resume Medis dalam Mendukung Kesiapan Klaim BPJS"
JUDUL_INDIVIDU = "Pengembangan dan Evaluasi Komponen Analisis Semantik untuk Pemeriksaan Konsistensi Dokumentasi Klinis dalam Mendukung Kesiapan Klaim BPJS"
PERAN = "AI/NLP Semantic Claim Intelligence"   # from the Breakdown (bagian 14), as recorded in CONTEXT_TRANSFER.md

# Optional two-pass TOC support (see tools/build_with_toc.py): TOC_PAGES = JSON {heading key: page label};
# HEADINGS_OUT = path where the ordered list of heading keys is written.
TOC_PAGES = os.environ.get("TOC_PAGES")
HEADINGS_OUT = os.environ.get("HEADINGS_OUT")

# Subbab outline (titles after II.1 and II.2 are the agent's proposal; files override placeholders)
OUTLINE = [
    ("II.1", "Dokumentasi Klinis dan Klaim JKN", REPO + "/bab2/II.1_Dokumentasi_Klinis_dan_Klaim_JKN.md"),
    ("II.2", "NLP dan LLM pada Teks Klinis", REPO + "/bab2/II.2_NLP_dan_LLM_pada_Teks_Klinis.md"),
    ("II.3", "Audit Otomatis Dokumentasi Klinis dan Kode Diagnosis", REPO + "/bab2/II.3_Audit_Otomatis_Dokumentasi_dan_Kode_Diagnosis.md"),
    ("II.4", "Pendekatan Hibrida Berbasis Aturan dan AI/NLP", REPO + "/bab2/II.4_Pendekatan_Hibrida_Berbasis_Aturan_dan_AI-NLP.md"),
    ("II.5", "RAG, Penjangkaran Bukti, dan Halusinasi", REPO + "/bab2/II.5_RAG_Penjangkaran_Bukti_dan_Halusinasi.md"),
    ("II.6", "De-identifikasi untuk Layanan AI Eksternal", REPO + "/bab2/II.6_Deidentifikasi_untuk_Layanan_AI_Eksternal.md"),
    ("II.7", "Evaluasi Sistem NLP Klinis", REPO + "/bab2/II.7_Evaluasi_Sistem_NLP_Klinis.md"),
    ("II.8", "Perbandingan Karya Terdahulu dan Celah Penelitian", REPO + "/bab2/II.8_Perbandingan_Karya_Terdahulu_dan_Celah_Penelitian.md"),
]

work = S + "/work"
shutil.rmtree(work, ignore_errors=True)
subprocess.run(["unzip", "-q", TEMPLATE, "-d", work], check=True)
subprocess.run(["find", work, "-type", "l", "-delete"], check=True)
subprocess.run(["python3", SK + "/scripts/merge_runs.py", work + "/"], check=True, capture_output=True)
doc_path = work + "/word/document.xml"
x = open(doc_path, encoding="utf8").read()

esc = lambda s: html.escape(s, quote=False)

def run(text, italic=False, hl=False, noproof=False):
    rpr = "<w:rPr>" + ("<w:i/>" if italic else "") + ("<w:noProof/>" if noproof else "") + ("<w:highlight w:val=\"yellow\"/>" if hl else "") + "<w:lang w:val=\"id-ID\"/></w:rPr>"
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'

TOK = re.compile(r"(\*[^*]+\*|\[[A-Z][A-Z ]+[^\]]*\])")
def runs(text, noproof=False):
    out = []
    for part in TOK.split(text):
        if not part: continue
        if part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append(run(part[1:-1], italic=True, noproof=noproof))
        elif part.startswith("[") and part.endswith("]"):
            out.append(run(part, hl=True))
        else:
            out.append(run(part, noproof=noproof))
    return "".join(out)

def body_p(text):  return '<w:p><w:pPr><w:rPr><w:lang w:val="id-ID"/></w:rPr></w:pPr>' + runs(text) + "</w:p>"
BM = [9000]
def bookmark_name():
    BM[0] += 1
    return BM[0], "_Toc9%06d" % BM[0]
def heading(level, text):
    n, name = bookmark_name()
    return (f'<w:p><w:pPr><w:pStyle w:val="Heading{level}"/></w:pPr><w:bookmarkStart w:id="{n}" w:name="{name}"/>'
            f'<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r><w:bookmarkEnd w:id="{n}"/></w:p>')
def placeholder(text): return '<w:p><w:pPr><w:rPr><w:lang w:val="id-ID"/></w:rPr></w:pPr>' + run(text, hl=True) + "</w:p>"
def ref_p(text):
    return ('<w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:left="720" w:hanging="720"/>'
            '<w:rPr><w:noProof/><w:lang w:val="id-ID" w:eastAsia="en-US"/></w:rPr></w:pPr>' + runs(text, noproof=True) + "</w:p>")


def cell_runs(text, bold=False):
    out = []
    for part in TOK.split(text):
        if not part: continue
        it = part.startswith("*") and part.endswith("*") and len(part) > 2
        t = part[1:-1] if it else part
        rpr = "<w:rPr>" + ("<w:b/>" if bold else "") + ("<w:i/>" if it else "") + "<w:sz w:val=\"20\"/><w:szCs w:val=\"20\"/><w:lang w:val=\"id-ID\"/></w:rPr>"
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(t)}</w:t></w:r>')
    return "".join(out)

TABLE_CAPTIONS = []   # (key, anchor) for the Daftar Tabel
def _fld(instr, cached):
    return ('<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> %s </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:noProof/></w:rPr><w:t>%s</w:t></w:r>'
            '<w:r><w:rPr><w:noProof/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>') % (instr, cached)
def caption_p(text):
    # chapter number typed (not STYLEREF): LibreOffice renders STYLEREF 1 \\s as the heading text; Word's SEQ \\s 1 still restarts per chapter
    m = re.match(r"^Tabel (II)\.(\d+)\.\s+(.*)$", text.strip())
    chap, num, title = m.group(1), m.group(2), m.group(3)
    n, name = bookmark_name()
    TABLE_CAPTIONS.append((f"Tabel {chap}.{num}. {title}", name))
    return ('<w:p><w:pPr><w:pStyle w:val="Caption"/><w:keepNext/><w:spacing w:before="120" w:after="80"/><w:ind w:left="0" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
            f'<w:bookmarkStart w:id="{n}" w:name="{name}"/><w:r><w:t xml:space="preserve">Tabel </w:t></w:r>'
            + f'<w:r><w:t>{chap}</w:t></w:r>' + '<w:r><w:t>.</w:t></w:r>' + _fld("SEQ Tabel \\* ARABIC \\s 1", num)
            + '<w:r><w:t>.</w:t></w:r><w:r><w:t xml:space="preserve"> </w:t></w:r>'
            + runs(title) + f'<w:bookmarkEnd w:id="{n}"/></w:p>')

def table_xml(lines, widths=(1750, 2300, 2150, 2106)):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines if not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln)]
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    tbl = ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/>'
           '<w:tblCellMar><w:left w:w="70" w:type="dxa"/><w:right w:w="70" w:type="dxa"/></w:tblCellMar>'
           '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr><w:tblGrid>%s</w:tblGrid>') % (sum(widths), grid)
    for i, r in enumerate(rows):
        hdr = i == 0
        tbl += "<w:tr><w:trPr><w:cantSplit/>" + ("<w:tblHeader/>" if hdr else "") + "</w:trPr>"
        for w, c in zip(widths, r):
            shade = '<w:shd w:val="clear" w:color="auto" w:fill="D9D9D9"/>' if hdr else ""
            tbl += (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{shade}</w:tcPr>'
                    '<w:p><w:pPr><w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>'
                    + cell_runs(c, bold=hdr) + "</w:p></w:tc>")
        tbl += "</w:tr>"
    return tbl + "</w:tbl>" + '<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="120" w:lineRule="exact"/></w:pPr></w:p>'

strip_num = lambda s: re.sub(r"^II\.\d+(\.\d+)?\s+", "", s)
new_bab2, refs, status = [], [], []
for num, title, path in OUTLINE:
    if path is None:
        new_bab2 += [heading(2, title), placeholder("[SUBBAB BELUM DITULIS. Judul ini usulan dan belum dikonfirmasi.]")]
        status.append((num, "placeholder")); continue
    md = open(path, encoding="utf8").read()
    naskah = md.split("## Naskah")[1].split("## Daftar Pustaka")[0]
    pustaka = md.split("## Daftar Pustaka (sementara)")[1].split("## Lampiran kerja")[0]
    nb = 0
    for chunk in re.split(r"\n\s*\n", naskah.strip()):
        chunk = chunk.strip()
        if not chunk or chunk == "---": continue
        if chunk.startswith("|"): new_bab2.append(table_xml(chunk.split("\n")))
        elif chunk.startswith("Tabel II."): new_bab2.append(caption_p(chunk))
        elif chunk.startswith("### "): new_bab2.append(heading(3, strip_num(chunk[4:])))
        elif chunk.startswith("## "): new_bab2.append(heading(2, strip_num(chunk[3:])))
        else: new_bab2.append(body_p(" ".join(chunk.split("\n")))); nb += 1
    for line in pustaka.split("\n"):
        line = line.strip()
        if line and not line.startswith(">") and line != "---": refs.append(line)
    status.append((num, f"{nb} paragraf"))
refs = sorted(set(refs), key=lambda r: re.sub(r"[^a-z0-9 ]", "", r.lower()))

# replace example content in Bab II (from first Heading 2 to the Heading 1 of Bab III)
kp = [m.start() for m in re.finditer(r"KAJIAN PUSTAKA", x)][-1]
h2 = x.index('<w:pStyle w:val="Heading2"/>', kp)
start = x.rfind("<w:p ", 0, h2)
end = x.index('<w:p w14:paraId="1E7576B4"')
tail_end = x.index('<w:p w14:paraId="08EFFE65"')            # Heading 1 'ANALISIS MASALAH ...'
assert x[end:tail_end].count("<w:p ") == 2                   # redundant empty + page-break paragraphs: dropped
open_xml = ""
intro_start = start
if OPEN and os.path.exists(OPEN):
    g = x.index("Bab Kajian Pustaka digunakan", kp)
    intro_start = x.rfind("<w:p ", 0, g)
    assert intro_start < start
    om = open(OPEN, encoding="utf8").read().split("## Naskah")[1]
    open_xml = "".join(body_p(" ".join(c.split("\n"))) for c in re.split(r"\n\s*\n", om.strip()) if c.strip() and c.strip() != "---")
x = x[:intro_start] + open_xml + "".join(new_bab2) + x[tail_end:]

# replace example references
b = x.index("Balabanovic"); rs = x.rfind("<w:p ", 0, b)
pz = x.index("Pazzani"); re_ = x.index("</w:p>", pz) + len("</w:p>")
note = placeholder("[Format sitasi sementara (penulis-tahun). Menunggu pedoman program studi. Hapus catatan ini setelah format ditetapkan.]")
x = x[:rs] + note + "".join(ref_p(r) for r in refs) + x[re_:]

# ---------- identity pages (cover, two approval pages, identity sheet) ----------
def para_span(xml, pid):
    m = re.search(r'<w:p w14:paraId="%s"[^>]*>.*?</w:p>' % pid, xml, flags=re.S)
    assert m, pid
    return m

def rebuild_para(xml, pid, ppr_fn, body):
    m = para_span(xml, pid); old = m.group(0)
    openp = re.match(r"<w:p [^>]*>", old).group(0)
    ppr = ppr_fn(re.search(r"<w:pPr>.*?</w:pPr>", old, flags=re.S).group(0))
    bms = "".join(re.findall(r"<w:bookmarkStart [^>]*/>", old))
    return xml[:m.start()] + openp + ppr + bms + body + "</w:p>" + xml[m.end():]

def title_runs(text, caps=False):
    out = ""
    for part in re.split(r"(User-Centered)", text):
        if not part: continue
        it = "<w:i/>" if part == "User-Centered" else ""
        t = part.upper() if caps else part
        out += ('<w:r><w:rPr><w:b/>%s<w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="id-ID"/></w:rPr>'
                '<w:t xml:space="preserve">%s</w:t></w:r>') % (it, esc(t))
    return out

no_color = lambda ppr: re.sub(r"<w:color [^>]*/>", "", ppr)
for pid in ("0869CB1C", "21135F97", "165A821F"):                  # individual title (caps), cover + 2 approval pages
    x = rebuild_para(x, pid, no_color, title_runs(JUDUL_INDIVIDU, caps=True))
for pid in ("62456833", "09CBFD9C", "5C7E98D9"):                  # capstone title
    x = rebuild_para(x, pid, no_color, title_runs(JUDUL_CAPSTONE))
assert x.count("&lt;NAMA MAHASISWA&gt;") == 3 and x.count("&lt;NIM MAHASISWA&gt;") == 3
x = x.replace("&lt;NAMA MAHASISWA&gt;", esc(NAMA)).replace("&lt;NIM MAHASISWA&gt;", esc(NIM))

judul_runs = runs(JUDUL_CAPSTONE.replace("User-Centered", "*User-Centered*"))
x = rebuild_para(x, "5EDC73B6", lambda ppr: '<w:pPr><w:tabs><w:tab w:val="left" w:pos="1800"/><w:tab w:val="left" w:pos="2000"/></w:tabs>'
                 '<w:spacing w:before="0" w:after="0"/><w:ind w:left="2000" w:hanging="2000"/><w:jc w:val="left"/></w:pPr>',
                 '<w:r><w:t>Judul Proyek TA</w:t></w:r><w:r><w:tab/><w:t>:</w:t></w:r><w:r><w:tab/></w:r>' + judul_runs)
cell_ppr = lambda ppr: '<w:pPr><w:spacing w:before="0" w:after="0"/><w:jc w:val="left"/></w:pPr>'
for pid, txt in (("44F2F985", "1"), ("00E65D00", NIM), ("208A84B8", NAMA), ("7D1257C4", PERAN)):
    x = rebuild_para(x, pid, cell_ppr, '<w:r><w:t xml:space="preserve">%s</w:t></w:r>' % esc(txt))

# The filled-in title and role wrap onto extra lines and push the supervisor names of the identity sheet to a new page:
# drop three of the four empty spacer paragraphs between the team table and the date line.
for pid in ("769366F5", "65D34022", "4D05B401"):
    m = para_span(x, pid)
    assert "<w:t" not in m.group(0)
    x = x[:m.start()] + x[m.end():]

# ---------- Daftar Isi, Daftar Gambar, Daftar Tabel (cached results; Word refreshes them on open) ----------
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
heads, cnt = [], [0, 0, 0]
for m in re.finditer(r"<w:p>.*?</w:p>|<w:p [^>]*>.*?</w:p>", x, flags=re.S):
    para = m.group(0)
    lv = re.search(r'<w:pStyle w:val="Heading([123])"/>', para)
    if not lv: continue
    lv = int(lv.group(1))
    title = html.unescape("".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", para))).strip()
    cnt[lv - 1] += 1
    for k in range(lv, 3): cnt[k] = 0
    num = ("BAB " + ROMAN[cnt[0] - 1]) if lv == 1 else ".".join([ROMAN[cnt[0] - 1]] + [str(c) for c in cnt[1:lv]])
    anchor = re.findall(r'<w:bookmarkStart [^>]*w:name="(_Toc[^"]+)"', para)[-1]
    heads.append(dict(level=lv, num=num, title=title, anchor=anchor, key=f"{num} {title}"))
pages = json.load(open(TOC_PAGES, encoding="utf8")) if TOC_PAGES and os.path.exists(TOC_PAGES) else {}
if HEADINGS_OUT:
    json.dump([h["key"] for h in heads] + [k for k, _ in TABLE_CAPTIONS], open(HEADINGS_OUT, "w", encoding="utf8"), ensure_ascii=False, indent=1)

NP = '<w:rPr><w:noProof/><w:webHidden/></w:rPr>'
MINOR = ('<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>')
def pageref(anchor, page):
    return (f'<w:r>{NP}<w:tab/></w:r><w:r>{NP}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{NP}<w:instrText xml:space="preserve"> PAGEREF {anchor} \\h </w:instrText></w:r><w:r>{NP}</w:r>'
            f'<w:r>{NP}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{NP}<w:t>{esc(str(page))}</w:t></w:r>'
            f'<w:r>{NP}<w:fldChar w:fldCharType="end"/></w:r>')
def toc_entry(h, first=False):
    lv = h["level"]; pg = pages.get(h["key"], "1")
    tabs = {1: '<w:tab w:val="right" w:leader="dot" w:pos="7927"/>',
            2: '<w:tab w:val="left" w:pos="800"/><w:tab w:val="right" w:leader="dot" w:pos="7927"/>',
            3: '<w:tab w:val="left" w:pos="1200"/><w:tab w:val="right" w:leader="dot" w:pos="7927"/>'}[lv]
    bold = '<w:b w:val="0"/>' if lv == 1 else ""
    ppr = (f'<w:pPr><w:pStyle w:val="TOC{lv}"/><w:tabs>{tabs}</w:tabs><w:rPr>{MINOR}{bold}<w:noProof/><w:sz w:val="22"/><w:szCs w:val="22"/>'
           '<w:lang w:val="en-US" w:eastAsia="en-US"/></w:rPr></w:pPr>')
    hl = '<w:rPr><w:rStyle w:val="Hyperlink"/><w:noProof/></w:rPr>'
    if lv == 1:
        body = f'<w:r>{hl}<w:t xml:space="preserve">{esc(h["num"] + " " + h["title"])}</w:t></w:r>'
    else:
        body = (f'<w:r>{hl}<w:t>{esc(h["num"])}</w:t></w:r><w:r><w:rPr>{MINOR}<w:noProof/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:tab/></w:r>'
                f'<w:r>{hl}<w:t xml:space="preserve">{esc(h["title"])}</w:t></w:r>')
    fld = ('<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
           '<w:r><w:fldChar w:fldCharType="separate"/></w:r>') if first else ""
    return f'<w:p>{ppr}{fld}<w:hyperlink w:anchor="{h["anchor"]}" w:history="1">{body}{pageref(h["anchor"], pg)}</w:hyperlink></w:p>'
t0 = x.index('<w:p w14:paraId="6CFCC5B2"'); t1 = x.index('<w:p w14:paraId="618E56B6"')
x = x[:t0] + "".join(toc_entry(h, first=(i == 0)) for i, h in enumerate(heads)) + x[t1:]

# Daftar Gambar: the template's example figure is gone (no figures yet); the placeholder line stays
m = para_span(x, "03A0E360")
x = x[:m.start()] + re.sub(r"<w:hyperlink .*?</w:hyperlink>", '', m.group(0), flags=re.S) + x[m.end():]
# Daftar Tabel now has a real entry, so its "<jika diperlukan>" placeholder goes
m = para_span(x, "648B1B13"); assert "jika diperlukan" in m.group(0)
x = x[:m.start()] + x[m.end():]
# Daftar Tabel: replace the template's example entry with the real table caption(s)
assert len(TABLE_CAPTIONS) == 1
key, anc = TABLE_CAPTIONS[0]
m = [mm for mm in re.finditer(r'<w:p w14:paraId="1290D30E"[^>]*>.*?</w:p>', x, flags=re.S)][0]
hl_t = (f'<w:hyperlink w:anchor="{anc}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/><w:noProof/></w:rPr><w:t xml:space="preserve">{esc(key)}</w:t></w:r>'
        + pageref(anc, pages.get(key, "1")) + "</w:hyperlink>")
x = x[:m.start()] + re.sub(r"<w:hyperlink .*?</w:hyperlink>", lambda _: hl_t, m.group(0), flags=re.S) + x[m.end():]

open(doc_path, "w", encoding="utf8").write(x)

cp = work + "/docProps/core.xml"
c = open(cp, encoding="utf8").read()
c = c.replace("<dc:title>DRAFT BUKU LAPORAN</dc:title>", "<dc:title>%s</dc:title>" % esc(JUDUL_INDIVIDU)).replace("<dc:creator>Shaggy</dc:creator>", "<dc:creator>%s</dc:creator>" % esc(NAMA))
open(cp, "w", encoding="utf8").write(c)

sp = work + "/word/settings.xml"
s = open(sp, encoding="utf8").read()
if "w:updateFields" not in s:
    for anchor in ["<w:hdrShapeDefaults", "<w:footnotePr", "<w:endnotePr", "<w:compat"]:
        if anchor in s:
            s = s.replace(anchor, '<w:updateFields w:val="true"/>' + anchor, 1); break
    open(sp, "w", encoding="utf8").write(s)

if os.path.exists(OUT): os.remove(OUT)
subprocess.run("cd %s && zip -Xqr %s ." % (work, OUT), shell=True, check=True)
print("written", OUT, os.path.getsize(OUT), "bytes;", status, "|", len(refs), "refs")
