"""Deterministic prose/structure linter for proposal Markdown (bab1..bab4). No LLM, no network.

Replaces the mechanical part of a09 (spelling lists, AI-slop phrases, punctuation) and a10/a12 (heading
hierarchy, tables, fences, leaked editorial markers). It only REPORTS; it never edits. Heuristic hits are
"periksa", not verdicts: RULES.md §6 and §8.5 still decide, and one or two slop hits are not a finding.

Usage:
  python scripts/lint_prose.py bab1/Bab_I_Draft.md [more.md ...] [--final] [--max-examples N] [--from-heading "## I.1"]
Skipped on purpose: fenced code, blockquotes (status/changelog block), and text inside quotation marks
(direct quotes and examples are never normalised, CLAUDE.md §2).
Exit code 1 only when a MEDIUM hit exists (or, with --final, when editorial markers remain); LOW/INFO never fail.
"""
import re, sys
from collections import defaultdict
from _common import ROOT  # noqa: F401  (also reconfigures stdout to UTF-8)

# (regex, severity, category, note) ------------------------------------------------------------------------
WORD_RULES = [
    (r"\banalisa\b", "MEDIUM", "ejaan", "baku: analisis"),
    (r"\bresiko\b", "MEDIUM", "ejaan", "baku: risiko"),
    (r"\baktifitas\b", "MEDIUM", "ejaan", "baku: aktivitas"),
    (r"\bkwalitas\b", "MEDIUM", "ejaan", "baku: kualitas"),
    (r"\bsistim\b", "MEDIUM", "ejaan", "baku: sistem"),
    (r"\b(?:me)?rubah\w*\b", "MEDIUM", "ejaan", "baku: ubah/mengubah (periksa 'rubah' = hewan)"),
    (r"\bijin\b", "MEDIUM", "ejaan", "baku: izin"),
    (r"\bsekedar\b", "MEDIUM", "ejaan", "baku: sekadar"),
    (r"\bobyek\w*\b", "MEDIUM", "ejaan", "baku: objek"),
    (r"\bfrekwensi\b", "MEDIUM", "ejaan", "baku: frekuensi"),
    (r"\bhakekat\b", "MEDIUM", "ejaan", "baku: hakikat"),
    (r"\bjaman\b", "MEDIUM", "ejaan", "baku: zaman"),
    (r"\bnampak\b", "LOW", "ejaan", "baku: tampak"),
    (r"\bpraktek\b", "LOW", "ejaan", "baku: praktik"),
    (r"\b(?:diatas|dibawah|didalam|diluar|disini|disana|kedalam|keatas|kebawah|diantara)\b",
     "MEDIUM", "kata depan", "kata depan ditulis terpisah: di atas, di bawah, di dalam, di luar, di sini, di sana, ke dalam, di antara (§6.10)"),
    (r"\bdimana\b", "LOW", "kalimat", "'dimana' sebagai penghubung: interferensi (§6.6); ganti 'yang' atau susun ulang"),
    (r"\badalah merupakan\b|\bmerupakan adalah\b", "LOW", "kalimat", "kopula ganda (§6.7)"),
    (r"\bsupaya agar\b|\bagar supaya\b", "LOW", "kalimat", "pleonasme (§6.7)"),
    (r"\bdaripada pada\b|\bnamun tetapi\b|\bsehingga oleh karena itu\b", "LOW", "kalimat", "pleonasme/konjungsi ganda (§6.7)"),
]

SLOP_RULES = [  # §8.5; INFO only, counted per document, a finding only when pervasive.
    (r"\bbukan (?:hanya|sekadar|semata)\b.{0,120}?\b(?:tetapi|melainkan)\b", "ai-slop 01-02", "'bukan hanya... tetapi/melainkan'"),
    (r"\btidak sekadar\b.{0,120}?\bmelainkan\b", "ai-slop 02", "'tidak sekadar... melainkan'"),
    (r"\bdalam dunia yang semakin\b|\bdi era (?:digital|modern)\b", "ai-slop 09", "'dalam dunia yang semakin'"),
    (r"\b(?:penting untuk dicatat bahwa|perlu dicatat bahwa|lebih jauh lagi|pada akhirnya|dalam konteks ini|tidak dapat dipungkiri)\b",
     "ai-slop 08", "transisi formulaik"),
    (r"\b(?:merevolusi|revolusioner|transformatif|paradigma baru|mengubah lanskap|lanskap|sinergi|ekosistem|holistik|komprehensif|inovatif|krusial|esensial|menjembatani kesenjangan|memainkan peran (?:penting|kunci|vital))\b",
     "ai-slop 06-07,10", "kata bombastis/abstrak/evaluatif tanpa ukuran"),
]

MARKERS = [r"\[MENUNGGU KEPUTUSAN[^\]]*\]", r"\[PERLU VERIFIKASI[^\]]*\]", r"\[DATA BELUM[^\]]*\]", r"\[SESUAIKAN[^\]]*\]",
           r"\{\{.*?\}\}", r"\[TODO[^\]]*\]", r"\bTBD\b"]

QUOTE = re.compile(r"“[^”]*”|\"[^\"\n]*\"|`[^`\n]*`")
SEV_ORDER = {"MEDIUM": 0, "LOW": 1, "INFO": 2}


def mask(s):
    """Blank out quotations and inline code so examples and direct quotes are not linted (placeholder keeps punctuation context)."""
    return QUOTE.sub(lambda m: "_" * len(m.group(0)), s)


def sentences(par):
    return [x for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý“\"(])", par) if x.strip()]


def lint(path, start_heading):
    hits = []  # (sev, cat, line, note, snippet)
    markers = defaultdict(int)
    lines = path.read_text(encoding="utf8").splitlines()
    in_fence, started = False, start_heading is None
    last_level, par, par_start = 0, [], 0
    table_cols = None
    fence_open_line = 0

    def flush():
        nonlocal par
        if par:
            text = " ".join(par)
            masked = mask(text)
            for s in sentences(masked):
                n = len(s.split())
                if n > 45:
                    hits.append(("INFO", "kalimat", par_start, f"kalimat {n} kata; periksa kalimat efektif (§6.7)", s[:70]))
            if masked.count("(") != masked.count(")"):
                hits.append(("LOW", "tanda baca", par_start, "tanda kurung tidak berpasangan", masked[:70]))
            if len(re.findall(r"“", text)) != len(re.findall(r"”", text)):
                hits.append(("LOW", "tanda baca", par_start, "tanda kutip “ ” tidak berpasangan", text[:70]))
        par = []

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if line.strip().startswith("```"):
            if not in_fence:
                fence_open_line = i
            in_fence = not in_fence
            flush()
            continue
        if in_fence:
            continue
        if not started:
            if line.strip().startswith(start_heading):
                started = True
            else:
                continue
        if line.lstrip().startswith(">"):
            flush()
            continue  # status/changelog blockquote
        m = re.match(r"^(#{1,6})\s+(\S.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            if last_level and level > last_level + 1:
                hits.append(("MEDIUM", "struktur", i, f"loncat heading H{last_level} ke H{level}", line[:70]))
            last_level = level
            table_cols = None
            continue
        if line.strip().startswith("|"):
            flush()
            cols = line.strip().strip("|").count("|") + 1
            if table_cols is None:
                table_cols = cols
            elif cols != table_cols:
                hits.append(("MEDIUM", "struktur", i, f"baris tabel {cols} kolom, header {table_cols}", line[:70]))
            continue
        table_cols = None
        if not line.strip():
            flush()
            continue
        if not par:
            par_start = i
        par.append(line.strip())
        for pat in MARKERS:
            for _ in re.finditer(pat, line):
                markers[re.sub(r"[\s\d].*", "", pat.replace("\\", ""))[:24]] += 1
        m_line = mask(line)
        for pat, sev, cat, note in WORD_RULES:
            for mm in re.finditer(pat, m_line, re.I):
                hits.append((sev, cat, i, note, mm.group(0)))
        for pat, cat, note in SLOP_RULES:
            for mm in re.finditer(pat, m_line, re.I):
                hits.append(("INFO", cat, i, note, mm.group(0)[:60]))
        for mm in re.finditer(r"\b(\w{3,})\s+\1\b", m_line, re.I):
            hits.append(("LOW", "ejaan", i, "kata berulang berurutan (kata ulang harus berhubung: kata-kata)", mm.group(0)))
        if re.search(r"\s[,.;:?!](?!\.)(?=\s|$)", m_line):
            hits.append(("LOW", "tanda baca", i, "spasi sebelum tanda baca", m_line.strip()[:70]))
        if re.search(r"[a-z][,;][A-Za-z]", m_line):
            hits.append(("LOW", "tanda baca", i, "tidak ada spasi setelah koma/titik koma", m_line.strip()[:70]))
        if "  " in line.strip():
            hits.append(("INFO", "tanda baca", i, "spasi ganda", ""))
        n_dash = m_line.count("—")
        if n_dash >= 2:
            hits.append(("INFO", "ai-slop 03", i, f"{n_dash} tanda pisah panjang dalam satu baris", ""))
    flush()
    if in_fence:
        hits.append(("MEDIUM", "struktur", fence_open_line, "blok kode/Mermaid tidak ditutup", ""))
    return hits, markers


def main(argv):
    final = "--final" in argv
    max_ex, start = 4, None
    args = []
    it = iter(argv)
    for a in it:
        if a == "--max-examples":
            max_ex = int(next(it))
        elif a == "--from-heading":
            start = next(it)
        elif not a.startswith("--"):
            args.append(a)
    if not args:
        print(__doc__)
        return 2
    rc = 0
    for a in args:
        p = (ROOT / a) if not re.match(r"^[A-Za-z]:|^/", a) else __import__("pathlib").Path(a)
        if not p.exists():
            print(f"lint_prose: {a} tidak ditemukan")
            rc = 2
            continue
        hits, markers = lint(p, start)
        by = defaultdict(list)
        for h in hits:
            by[(h[0], h[1])].append(h)
        print(f"== {a} ==")
        counts = {s: sum(1 for h in hits if h[0] == s) for s in SEV_ORDER}
        print(f"MEDIUM {counts['MEDIUM']} | LOW {counts['LOW']} | INFO {counts['INFO']}")
        for (sev, cat) in sorted(by, key=lambda k: (SEV_ORDER[k[0]], k[1])):
            group = by[(sev, cat)]
            print(f"[{sev}] {cat}: {len(group)}")
            for sv, c, ln, note, snip in group[:max_ex]:
                print(f"  L{ln}: {note}" + (f" — «{snip}»" if snip else ""))
            if len(group) > max_ex:
                print(f"  ... +{len(group) - max_ex} lagi")
        if markers:
            tot = sum(markers.values())
            print(f"Penanda editorial tersisa: {tot} ({', '.join(f'{k} {v}' for k, v in markers.items())})"
                  + (" -> GAGAL untuk versi final" if final else " (wajar untuk draf)"))
        if counts["MEDIUM"] or (final and markers):
            rc = max(rc, 1)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
