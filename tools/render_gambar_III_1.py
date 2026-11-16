"""Render Gambar III.1 (diagram blok capstone) untuk Bab III.

Sumber yang dapat disunting: berkas ini dan blok Mermaid pada
`bab3/Bab_III_Draft.md`. Keduanya harus memuat node, panah, dan label yang
sama; berkas ini hanya menambah tata letak.

Satuan koordinat adalah sentimeter pada ukuran cetak (14,6 cm x 6,8 cm),
sehingga ukuran huruf di bawah adalah ukuran huruf pada halaman.

Pemakaian:
    python tools/render_gambar_III_1.py bab3/gambar/gambar-III-1.png
Berkas .svg dengan nama yang sama ikut ditulis (dapat disunting di Inkscape).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["svg.fonttype"] = "none"

W, Y0, Y1 = 14.6, 0.85, 7.65        # cm
FS, FS_E = 7.5, 7.0                 # pt: node/klaster, label panah
LW = 0.7
DASH = (0, (4, 3))

fig = plt.figure(figsize=(W / 2.54, (Y1 - Y0) / 2.54))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(Y0, Y1)
ax.axis("off")
fig.canvas.draw()
R = fig.canvas.get_renderer()
inv = ax.transData.inverted()
nodes = {}


def text_size(t, fs, **kw):
    tmp = ax.text(0, 0, t, fontsize=fs, linespacing=1.15, **kw)
    bb = tmp.get_window_extent(renderer=R)
    tmp.remove()
    (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
    return x1 - x0, y1 - y0


def node(key, x, y, text, w=None):
    tw, th = text_size(text, FS)
    w, h = (w or tw + 0.3), th + 0.26
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=0.12",
                                lw=LW, ec="black", fc="white", zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=FS, zorder=4,
            linespacing=1.15)
    nodes[key] = (x, y, w, h)


def cluster(x0, y0, x1, y1, title, tx, ty):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0,rounding_size=0.15",
                                lw=LW, ec="black", fc="#f2f2f2", zorder=1))
    ax.text(tx, ty, title, ha="center", va="center", fontsize=FS,
            zorder=4, linespacing=1.15)


def N(key, side, d=0.0):
    """Titik pada sisi node; d menggeser sepanjang sisi itu."""
    x, y, w, h = nodes[key]
    return {"t": (x + d, y + h / 2), "b": (x + d, y - h / 2),
            "l": (x - w / 2, y + d), "r": (x + w / 2, y + d)}[side]


def arrow(p, q, dashed=False):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=6,
                                 lw=LW, color="black", zorder=2,
                                 linestyle=DASH if dashed else "-",
                                 shrinkA=0, shrinkB=0))


def poly(points, dashed=False):
    xs, ys = zip(*points[:-1])
    ax.plot(xs, ys, color="black", lw=LW, linestyle=DASH if dashed else "-",
            zorder=2, solid_capstyle="butt")
    arrow(points[-2], points[-1], dashed=dashed)


def label(x, y, text, ha="center"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=FS_E, zorder=5,
            linespacing=1.1, bbox=dict(fc="white", ec="none", pad=0.6))


# --- Lajur kiri: sumber dokumen dan bagian Health Data ----------------------
node("SIMRS", 1.75, 6.97, "SIMRS RSIA mitra\n(CPPT dan dokumen\nringkasan pelayanan)", w=3.1)
cluster(0.05, 2.95, 3.45, 6.02,
        "Health Data & Cross-Episode\nReconciliation\n(Muhammad Raihaan Perdana)",
        tx=1.75, ty=3.72)
node("HD1", 1.75, 5.2, "Dokumen terdeidentifikasi,\ndisatukan per episode,\ndan berversi", w=3.1)
node("EXT", 1.75, 1.5, "Dari luar sistem:\nlabel acuan tenaga ahli dan\nskor penilaian kejelasan", w=3.3)

# --- Lajur tengah: sistem analisis semantik (penelitian ini) ----------------
cluster(3.85, 0.92, 11.05, 7.6,
        "AI/NLP Semantic Claim Intelligence (Danendra Shafi Athallah):\n"
        "sistem analisis semantik (penelitian ini)",
        tx=7.45, ty=7.2)
node("M1", 7.6, 6.2, "M1 Penyiapan dan Segmentasi\n(aturan pemecahan kalimat dan LLM)")
node("M2a", 5.6, 4.65, "M2a Pemeriksa Rule-based*\n(leksikon, pola, dan aturan;\ntanpa LLM)", w=3.2)
node("M2b", 9.15, 4.65, "M2b Pembentuk Temuan RAG\n(retrieval atas proposisi\nkedua dokumen dan LLM)", w=3.5)
node("M3", 7.45, 3.05, "M3 Penggabung Union\ndan Deduplikasi", w=2.6)
node("M4", 7.45, 1.5, "M4 Perangkat Evaluasi\n(ketiga konfigurasi)", w=2.8)

# --- Lajur kanan: bagian Claim Review, keterangan, dan hasil ----------------
cluster(11.45, 2.3, 14.55, 5.0,
        "Claim Review &\nResolution Engineering\n(M. Abizzar Gamadrian)",
        tx=13.0, ty=4.32)
node("CR1", 13.0, 3.05, "Konsumen temuan:\nrekonsiliasi, penilaian,\ndan tindak lanjut", w=2.8)
node("OUT", 13.0, 1.5, "Hasil evaluasi untuk\npertanyaan penelitian\n1 dan 2", w=2.8)

ax.text(11.5, 7.42, "Keterangan:", ha="left", va="center", fontsize=FS_E)
ax.plot([11.5, 12.1], [7.08, 7.08], color="black", lw=LW, linestyle=DASH)
ax.text(12.2, 6.94, "temuan tiap komponen\nyang diukur M4", ha="left", va="center",
        fontsize=FS_E, linespacing=1.15)
ax.text(11.5, 5.92, "* dibangun penulis\n"
                   "  (subbab I.5); pemiliknya\n"
                   "  dalam pembagian bidang\n"
                   "  tim belum ditetapkan",
        ha="left", va="center", fontsize=FS_E, linespacing=1.15)

# --- Panah ------------------------------------------------------------------
arrow(N("SIMRS", "b"), N("HD1", "t"))

# HD1 -> M1 (berkas per episode)
xc = 3.65
poly([N("HD1", "r", 0.2), (xc, N("HD1", "r", 0.2)[1]), (xc, 6.2), N("M1", "l")])
label(4.5, 6.58, "berkas per\nepisode")

# M1 -> M2a, M1 -> M2b (proposisi)
arrow((5.9, N("M1", "b")[1]), (5.9, N("M2a", "t")[1]))
arrow((9.0, N("M1", "b")[1]), (9.0, N("M2b", "t")[1]))
mid = (N("M1", "b")[1] + N("M2a", "t")[1]) / 2
label(7.45, mid, "proposisi yang sama")

# M2a -> M3, M2b -> M3 (temuan)
arrow((6.6, N("M2a", "b")[1]), (6.6, N("M3", "t")[1]))
arrow((8.3, N("M2b", "b")[1]), (8.3, N("M3", "t")[1]))
mid = (N("M2a", "b")[1] + N("M3", "t")[1]) / 2
label(7.45, mid, "temuan")

# M3 -> M4 (konfigurasi kombinasi)
arrow(N("M3", "b"), N("M4", "t"))
label(7.45, (N("M3", "b")[1] + N("M4", "t")[1]) / 2, "temuan kombinasi")

# M2a -> M4 dan M2b -> M4 (putus-putus: temuan tiap komponen)
poly([(4.5, N("M2a", "b")[1]), (4.5, N("M4", "l", 0.2)[1]), N("M4", "l", 0.2)], dashed=True)
poly([(10.4, N("M2b", "b")[1]), (10.4, N("M4", "r", 0.2)[1]), N("M4", "r", 0.2)], dashed=True)
label(5.3, 2.3, "temuan\nrule-based")
label(9.55, 2.28, "temuan AI/NLP\nberbasis RAG")

# M3 -> CR1 (temuan unik)
arrow(N("M3", "r"), N("CR1", "l"))
label(9.65, 3.27, "temuan unik")

# Dari luar sistem -> M4 -> hasil evaluasi
arrow(N("EXT", "r", -0.2), N("M4", "l", -0.2))
arrow(N("M4", "r", -0.2), N("OUT", "l", -0.2))

out = Path(sys.argv[1])
fig.savefig(out, dpi=400, facecolor="white")
fig.savefig(out.with_suffix(".svg"), facecolor="white")
print("saved", out, out.with_suffix(".svg"))
