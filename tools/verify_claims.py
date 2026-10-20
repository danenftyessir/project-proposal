"""Check that each cited phrase occurs on the cited PDF page.
Usage: python3 -I tools/verify_claims.py claims.json   (list of {id, src, p, q}); p may be a list.
Page numbers follow the convention in CONTEXT_TRANSFER.md (per-source offset in PDFS).
"""
import subprocess, re, sys, json

ROOT = "/home/user/project-proposal/"
PDFS = {
 "simbolon": (ROOT+"source/external/faktor-faktor yang mempengaruhi pending rawat inap.pdf", 71),   # printed = pdf + 71
 "rachmawaty": (ROOT+"source/1-s2.0-S0213911121003071-main.pdf", 612),   # printed S6xx = pdf + 612
 "nilasari": (ROOT+"source/1-s2.0-S1877050926029406-main.pdf", 850),      # printed = pdf + 850
 "susilo": (ROOT+"source/1-s2.0-S294985622500090X-main.pdf", 0),
 "dietrich": (ROOT+"source/external/Automated auditing of emergency department documentation using.pdf", 94),  # printed = pdf + 94
 "skrabic":  (ROOT+"source/1-s2.0-S1386505626000560-main.pdf", 0),
 "du":       (ROOT+"source/1-s2.0-S266676492600007X-main.pdf", 0),
 "mwogosi":  (ROOT+"source/1-s2.0-S2211883726000614-main.pdf", 0),
 "lebena":   (ROOT+"source/1-s2.0-S2352914825000255-main.pdf", 0),
 "jaganathan": (ROOT+"source/1-s2.0-S235264832500025X-main.pdf", 0),
 "hou":      (ROOT+"source/1-s2.0-S0957417424003841-main.pdf", 0),
 "wei":      (ROOT+"source/1-s2.0-S1532046426001097-main.pdf", 0),
 "elvas":    (ROOT+"source/1-s2.0-S1386505625002667-main.pdf", 0),
 "woo":      (ROOT+"source/1-s2.0-S0020748925003323-main.pdf", 0),
 "kumar":    (ROOT+"source/1-s2.0-S2667305326000724-main.pdf", 0),
 "luo":      (ROOT+"source/1-s2.0-S0933365724001465-main.pdf", 0),
 "chen":     (ROOT+"source/1-s2.0-S1532046426000298-main.pdf", 0),
 "olex":     (ROOT+"source/1-s2.0-S1532046421001131-main.pdf", 0),
 "jafarpour": (ROOT+"source/1-s2.0-S0933365725002167-main.pdf", 0),
}

def norm(t):
    t = re.sub("­\\s*", "", t).replace("ﬁ", "fi").replace("ﬂ", "fl")
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = re.sub(r"-\s*\n\s*", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.lower()

cache = {}
def pages(key):
    if key in cache: return cache[key]
    path, off = PDFS[key]
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout).group(1))
    out = []
    for p in range(1, n+1):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), path, "-"], capture_output=True, text=True).stdout
        out.append(norm(t))
    cache[key] = out
    return out

def find(key, phrase):
    ph = norm(phrase)
    off = PDFS[key][1]
    return [i+1+off for i, t in enumerate(pages(key)) if ph in t]

claims = json.load(open(sys.argv[1]))
bad = 0
for c in claims:
    found = find(c["src"], c["q"])
    exp = c["p"] if isinstance(c["p"], list) else [c["p"]]
    ok = bool(found) and any(e in found for e in exp)
    if not ok: bad += 1
    print(("OK  " if ok else "FAIL"), c["id"], c["src"], "expected", exp, "found", found, "|", c["q"][:60])
print("FAILED:", bad, "of", len(claims))
