"""Render Gambar IV.1 (Gantt chart pelaksanaan TA 2, minggu 1-20) untuk Bab IV.

Sumber yang dapat disunting: berkas ini dan blok teks jadwal pada
`bab4/Bab_IV_Draft.md`. Keduanya harus memuat tahap, minggu, gerbang, dan
ketergantungan yang sama; berkas ini hanya menambah tata letak.

Satuan sumbu x adalah minggu: minggu w menempati selang [w-1, w].

Pemakaian:
    python tools/render_gambar_IV_1.py bab4/gambar/gambar-IV-1.png
Berkas .svg dengan nama yang sama ikut ditulis.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Polygon

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["hatch.linewidth"] = 0.5

FS, FS_S = 8.0, 7.0
LW = 0.7
WEEKS = 20
LABEL_W = 7.0          # lebar kolom nama tahap, dalam satuan minggu
ROW_H, BAR_H = 1.0, 0.56

# (kode, nama, mulai, selesai, jenis data) - jenis: "dua", "dev", "uji"
TASKS = [
    ("T1", "Penyiapan data dan\nkontrak antarblok", 1, 3, "dua"),
    ("T2", "Pembangunan M1", 3, 5, "dev"),
    ("T3", "Pembangunan M2a dan M2b", 5, 10, "dev"),
    ("T4", "Pembangunan M3 dan M4", 10, 11, "dev"),
    ("T5", "Pelabelan oleh tenaga ahli", 6, 12, "uji"),
    ("T6", "Pengujian deteksi", 13, 15, "uji"),
    ("T7", "Penilaian kejelasan dan\npenyusunan jawaban", 15, 20, "uji"),
]
PREP = {"T5": (4, 5), "T7": (13, 14)}          # persiapan (garis titik-titik)
DEPS = [("T1", "T2", 3), ("T2", "T3", 5), ("T3", "T4", 10), ("T6", "T7", 15)]
GATE_WEEK = 13
RESERVE_WEEK = 12

n = len(TASKS)
fig = plt.figure(figsize=(14.6 / 2.54, 7.8 / 2.54))
ax = fig.add_axes([0, 0, 1, 1])
x0 = -LABEL_W
ax.set_xlim(x0 - 0.1, WEEKS + 0.15)
ax.set_ylim(-n * ROW_H - 2.05, 1.55)
ax.axis("off")
row_y = {t[0]: -(i + 0.5) * ROW_H for i, t in enumerate(TASKS)}

# --- kisi minggu, minggu cadangan, dan kepala tabel --------------------------
ax.add_patch(Rectangle((RESERVE_WEEK - 1, -n * ROW_H), 1, n * ROW_H,
                       fc="#e6e6e6", ec="none", zorder=0))
ax.text(RESERVE_WEEK - 0.5, -1.5 * ROW_H, "minggu cadangan", ha="center", va="center",
        fontsize=FS_S, style="italic", rotation=90, zorder=2)
for w in range(WEEKS + 1):
    ax.plot([w, w], [-n * ROW_H, 0.0], color="#bdbdbd", lw=0.35, zorder=1)
for i in range(n + 1):
    ax.plot([x0, WEEKS], [-i * ROW_H, -i * ROW_H], color="#bdbdbd", lw=0.35, zorder=1)
ax.plot([x0, WEEKS], [0, 0], color="black", lw=LW, zorder=2)
ax.plot([x0, WEEKS], [-n * ROW_H, -n * ROW_H], color="black", lw=LW, zorder=2)
for w in range(1, WEEKS + 1):
    ax.text(w - 0.5, 0.3, str(w), ha="center", va="center", fontsize=FS_S)
ax.text(WEEKS / 2, 0.85, "Minggu ke-", ha="center", va="center", fontsize=FS)
ax.text(x0 + 0.15, 0.3, "Tahap", ha="left", va="center", fontsize=FS, fontweight="bold")

# --- batang tahap ------------------------------------------------------------
STYLE = {
    "dua": dict(fc="white", hatch=None),
    "dev": dict(fc="#8c8c8c", hatch=None),
    "uji": dict(fc="white", hatch="////"),
}
for code, name, s, e, kind in TASKS:
    y = row_y[code]
    ax.text(x0 + 0.15, y, code, ha="left", va="center", fontsize=FS)
    ax.text(x0 + 1.2, y, name, ha="left", va="center", fontsize=FS, linespacing=1.0)
    st = STYLE[kind]
    ax.add_patch(Rectangle((s - 1, y - BAR_H / 2), e - s + 1, BAR_H, fc=st["fc"], ec="black",
                           hatch=st["hatch"], lw=LW, zorder=3))
    if code in PREP:
        ps, pe = PREP[code]
        ax.add_patch(Rectangle((ps - 1, y - BAR_H / 2), pe - ps + 1, BAR_H, fc="white",
                               ec="black", lw=LW, ls=(0, (1, 1.5)), zorder=3))

# --- gerbang pembekuan konfigurasi (awal minggu 13) --------------------------
gx = GATE_WEEK - 1
ax.plot([gx, gx], [-n * ROW_H, 0], color="black", lw=1.1, ls=(0, (4, 2)), zorder=4)
d = 0.24
yb = -n * ROW_H - 0.05
ax.add_patch(Polygon([(gx, yb), (gx + d, yb - d), (gx, yb - 2 * d), (gx - d, yb - d)],
                     closed=True, fc="black", ec="black", zorder=5))

# --- ketergantungan ------------------------------------------------------------
for a, b, wk in DEPS:
    ax.add_patch(FancyArrowPatch((wk - 1, row_y[a] - BAR_H / 2), (wk - 1, row_y[b] + BAR_H / 2),
                                 arrowstyle="-|>", mutation_scale=6, lw=0.6, color="black",
                                 zorder=6, shrinkA=0, shrinkB=0.5))

# --- keterangan ----------------------------------------------------------------
ly1 = -n * ROW_H - 0.95
ly2 = ly1 - 0.62
lx = x0 + 0.15


def legend_box(x, y, kind=None, dotted=False):
    if dotted:
        ax.add_patch(Rectangle((x, y - 0.2), 0.9, 0.4, fc="white", ec="black", lw=LW,
                               ls=(0, (1, 1.5)), zorder=3))
    else:
        st = STYLE[kind]
        ax.add_patch(Rectangle((x, y - 0.2), 0.9, 0.4, fc=st["fc"], ec="black",
                               hatch=st["hatch"], lw=LW, zorder=3))


ax.text(lx, ly1, "Keterangan:", va="center", fontsize=FS_S)
legend_box(lx + 4.0, ly1, "dua")
ax.text(lx + 5.1, ly1, "pembagian data (T1)", va="center", fontsize=FS_S)
legend_box(lx + 11.0, ly1, "dev")
ax.text(lx + 12.1, ly1, "memakai data pengembangan", va="center", fontsize=FS_S)
legend_box(lx + 19.8, ly1, "uji")
ax.text(lx + 20.9, ly1, "memakai data uji", va="center", fontsize=FS_S)
legend_box(lx + 4.0, ly2, dotted=True)
ax.text(lx + 5.1, ly2, "persiapan", va="center", fontsize=FS_S)
ax.add_patch(FancyArrowPatch((lx + 11.0, ly2), (lx + 11.9, ly2), arrowstyle="-|>",
                             mutation_scale=6, lw=0.6, color="black"))
ax.text(lx + 12.1, ly2, "ketergantungan", va="center", fontsize=FS_S)
ax.add_patch(Polygon([(lx + 20.35, ly2 + 0.22), (lx + 20.55, ly2), (lx + 20.35, ly2 - 0.22),
                      (lx + 20.15, ly2)], closed=True, fc="black"))
ax.text(lx + 20.9, ly2, "gerbang pembekuan konfigurasi", va="center", fontsize=FS_S)

out = Path(sys.argv[1])
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=400, facecolor="white")
fig.savefig(out.with_suffix(".svg"), facecolor="white")
print("saved", out, out.with_suffix(".svg"))
