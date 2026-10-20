import re, html, shutil, os, subprocess, tempfile

"""Build the Bab II draft .docx from the Markdown subbab files and the Utama template.

Usage: python3 -I tools/build_docx.py
Needs the docx skill scripts (merge_runs.py); set DOCX_SKILL_DIR if the default path differs.
Add a subbab by pointing its OUTLINE entry to a Markdown file (None = highlighted placeholder).
Validate afterwards with the skill's scripts/office/validate.py and render with soffice.py.
"""
S = tempfile.mkdtemp(prefix="bab2_build_")
SK = os.environ.get("DOCX_SKILL_DIR", "/root/.claude/skills/synced/017185de-19fa-4709-a10a-3db50e5d500d_a2aeaf02-31ea-42d9-a648-645d5f31836f/docx")
REPO = "/home/user/project-proposal"
OUT = REPO + "/bab2/Proposal-IF4091-Capstone-Utama-2026_Draft-Bab2.docx"

# Subbab outline (titles after II.1 and II.2 are the agent's proposal; files override placeholders)
OUTLINE = [
    ("II.1", "Dokumentasi Klinis dan Klaim JKN", REPO + "/bab2/II.1_Dokumentasi_Klinis_dan_Klaim_JKN.md"),
    ("II.2", "NLP dan LLM pada Teks Klinis", REPO + "/bab2/II.2_NLP_dan_LLM_pada_Teks_Klinis.md"),
    ("II.3", "Audit Otomatis Dokumentasi Klinis dan Kode Diagnosis", REPO + "/bab2/II.3_Audit_Otomatis_Dokumentasi_dan_Kode_Diagnosis.md"),
    ("II.4", "Pendekatan Hibrida Berbasis Aturan dan AI/NLP", REPO + "/bab2/II.4_Pendekatan_Hibrida_Berbasis_Aturan_dan_AI-NLP.md"),
    ("II.5", "RAG, Penjangkaran Bukti, dan Halusinasi", REPO + "/bab2/II.5_RAG_Penjangkaran_Bukti_dan_Halusinasi.md"),
    ("II.6", "De-identifikasi untuk Layanan AI Eksternal", REPO + "/bab2/II.6_Deidentifikasi_untuk_Layanan_AI_Eksternal.md"),
]

work = S + "/work"
shutil.rmtree(work, ignore_errors=True)
subprocess.run(["unzip", "-q", REPO + "/Template-Proposal-IF4091-Capstone-Utama-2026.docx", "-d", work], check=True)
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
def heading(level, text): return f'<w:p><w:pPr><w:pStyle w:val="Heading{level}"/></w:pPr><w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'
def placeholder(text): return '<w:p><w:pPr><w:rPr><w:lang w:val="id-ID"/></w:rPr></w:pPr>' + run(text, hl=True) + "</w:p>"
def ref_p(text):
    return ('<w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:left="720" w:hanging="720"/>'
            '<w:rPr><w:noProof/><w:lang w:val="id-ID" w:eastAsia="en-US"/></w:rPr></w:pPr>' + runs(text, noproof=True) + "</w:p>")

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
        if chunk.startswith("### "): new_bab2.append(heading(3, strip_num(chunk[4:])))
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
x = x[:start] + "".join(new_bab2) + x[tail_end:]

# replace example references
b = x.index("Balabanovic"); rs = x.rfind("<w:p ", 0, b)
pz = x.index("Pazzani"); re_ = x.index("</w:p>", pz) + len("</w:p>")
note = placeholder("[Format sitasi sementara (penulis-tahun). Menunggu pedoman program studi. Hapus catatan ini setelah format ditetapkan.]")
x = x[:rs] + note + "".join(ref_p(r) for r in refs) + x[re_:]
open(doc_path, "w", encoding="utf8").write(x)

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
