"""Render Gambar III.1 (diagram blok capstone) dari diagram Mermaid di bab3/Bab_III_Draft.md.

Gaya mengikuti gambar Bab II: hitam-putih, huruf serif, kotak bersudut bulat,
klaster berbingkai. Isi node/label sama dengan sumber Mermaid; hanya
pemenggalan baris yang disesuaikan.
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Serif"
FS, FS_E, FS_C = 8.0, 7.0, 8.0

fig, ax = plt.subplots(figsize=(7.5, 9.25))
ax.set_xlim(-0.3, 15.45)
ax.set_ylim(-2.3, 16.9)
ax.axis("off")
fig.canvas.draw()
R = fig.canvas.get_renderer()
inv = ax.transData.inverted()

nodes = {}
DASH = (0, (4, 3))


def text_size(t, fs):
    tmp = ax.text(0, 0, t, fontsize=fs, linespacing=1.25)
    bb = tmp.get_window_extent(renderer=R)
    tmp.remove()
    (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
    return x1 - x0, y1 - y0


def node(key, x, y, text):
    tw, th = text_size(text, FS)
    w, h = tw + 0.7, th + 0.55
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=0.3",
                                lw=0.9, ec="black", fc="white", zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=FS, zorder=4,
            linespacing=1.25)
    nodes[key] = (x, y, w, h)


def cluster(x0, y0, x1, y1, title, tx, ty, ha="center"):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0,rounding_size=0.4",
                                lw=0.9, ec="black", fc="none", zorder=1))
    ax.text(tx, ty, title, ha=ha, va="center", fontsize=FS_C, zorder=4,
            linespacing=1.2)


def N(key, s):
    x, y, w, h = nodes[key]
    return {"t": (x, y + h / 2), "b": (x, y - h / 2),
            "l": (x - w / 2, y), "r": (x + w / 2, y)}[s]


def arrow(p, q, dashed=False):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=9,
                                 lw=0.9, color="black", zorder=2,
                                 linestyle=DASH if dashed else "-",
                                 shrinkA=0, shrinkB=0))


def poly(points, dashed=False):
    xs, ys = zip(*points[:-1])
    ax.plot(xs, ys, color="black", lw=0.9, linestyle=DASH if dashed else "-",
            zorder=2, solid_capstyle="butt")
    arrow(points[-2], points[-1], dashed=dashed)


def label(x, y, text, ha="center"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=FS_E, zorder=5,
            linespacing=1.15, bbox=dict(fc="white", ec="none", pad=0.8))


# --- Node dan klaster -------------------------------------------------------
node("SIMRS", 3.7, 15.9, "SIMRS RSIA mitra\nCPPT dan dokumen ringkasan pelayanan")

cluster(0.0, 12.3, 10.85, 14.45, "Bagian Health Data &\nCross-Episode\nReconciliation",
        tx=8.9, ty=13.35)
node("HD1", 3.7, 13.35, "Dokumen terdeidentifikasi,\ndisatukan per episode, dan berversi")

cluster(0.0, 0.35, 10.85, 10.75, "Sistem analisis semantik\n(penelitian ini)",
        tx=10.55, ty=10.1, ha="right")
node("M1", 5.15, 8.85, "M1 Penyiapan dan Segmentasi\n(aturan pemecahan kalimat dan LLM)")
node("M2a", 2.55, 6.3, "M2a Pemeriksa Rule-based\n(leksikon, pola, dan aturan;\ntanpa LLM)")
node("M2b", 7.95, 6.3, "M2b Pembentuk Temuan RAG\n(indeks retrieval dari\nproposisi kedua dokumen)")
node("M3", 5.15, 3.85, "M3 Penggabung Union\ndan Deduplikasi")
node("M4", 5.15, 1.25, "M4 Perangkat Evaluasi")

cluster(11.3, 2.55, 15.1, 5.6, "Bagian Claim Review &\nResolution Engineering",
        tx=13.2, ty=5.05)
node("CR1", 13.2, 3.55, "Konsumen temuan\n(rekonsiliasi dan\nantarmuka)")

node("EXT", 13.2, 0.6, "Dari luar sistem:\nlabel acuan tenaga ahli\ndan skor penilaian\nkejelasan")
node("OUT", 5.15, -1.4, "Hasil evaluasi\npertanyaan penelitian 1–3")

# --- Panah ------------------------------------------------------------------
arrow(N("SIMRS", "b"), N("HD1", "t"))

arrow(N("HD1", "b"), (3.7, N("M1", "t")[1]))
label(3.7, 11.55, "berkas per episode")

xa, xb = 3.3, 7.0
arrow((xa, N("M1", "b")[1]), (xa, N("M2a", "t")[1]))
arrow((xb, N("M1", "b")[1]), (xb, N("M2b", "t")[1]))
mid = (N("M1", "b")[1] + N("M2a", "t")[1]) / 2
label(xa, mid, "proposisi")
label(xb, mid, "proposisi")

arrow((3.6, N("M2a", "b")[1]), (4.1, N("M3", "t")[1]))
arrow((6.7, N("M2b", "b")[1]), (6.2, N("M3", "t")[1]))
mid = (N("M2a", "b")[1] + N("M3", "t")[1]) / 2
label(3.85, mid, "temuan")
label(6.45, mid, "temuan")

# M3 -> CR1 (temuan unik)
arrow(N("M3", "r"), (N("CR1", "l")[0], N("M3", "r")[1]))
label(8.35, N("M3", "r")[1] + 0.62, "temuan unik\n(skema\ntemuan)")

# M3 -> M4 (konfigurasi kombinasi)
arrow(N("M3", "b"), N("M4", "t"))
label(5.15, 2.55, "temuan konfigurasi\nkombinasi")

# M2a -> M4 dan M2b -> M4 (putus-putus)
xl, xr = 0.75, 10.0
poly([(xl, N("M2a", "b")[1]), (xl, 1.25), N("M4", "l")], dashed=True)
poly([(xr, N("M2b", "b")[1]), (xr, 1.25), N("M4", "r")], dashed=True)
label(2.1, 2.55, "temuan\nkonfigurasi\nrule-based")
label(8.3, 2.55, "temuan\nkonfigurasi\nAI/NLP\nberbasis RAG")

# Dari luar sistem -> M4
arrow(N("EXT", "l"), (N("M4", "r")[0], 1.0))

# M4 -> hasil
arrow(N("M4", "b"), N("OUT", "t"))

out = sys.argv[1]
fig.savefig(out, dpi=300, bbox_inches="tight", pad_inches=0.05, facecolor="white")
print("saved", out)
