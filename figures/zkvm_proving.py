# zkvm_proving.py — Ethereum ブロック証明時間の年次推移 (SL10b)
#
# 生成: uv run --with matplotlib python3 figures/zkvm_proving.py
# 出力: public/images/zkvm_proving_time.png
#
# 設計:
#   - 縦軸 = 1 ブロックの証明時間 (秒, log)。下ほど速い。
#   - 12 秒 (Ethereum の 1 スロット) に閾値線。下側の淡い緑帯 = real-time 域。
#   - 各点は公表実測値のみ (最速公表値の推移)。ロゴ = どの企業の製品か。
#   - 凡例なし。直接ラベル + ロゴで読ませる。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/zkvm_proving_time.png"
LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

SURFACE = "#ffffff"
AMBER = "#d97706"
GREEN = "#059669"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"
BAND_FC = "#ecfdf5"
AXIS = "#d1d5db"

TARGET_LOGO_H = 34.0
MAX_LOGO_W = 100.0


def logo_zoom(path):
    img = mpimg.imread(path)
    h, w = img.shape[0], img.shape[1]
    return min(TARGET_LOGO_H / h, MAX_LOGO_W / w)


fig, ax = plt.subplots(figsize=(13.2, 5.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(2022.0, 2026.85)
ax.set_yscale("log")
ax.set_ylim(2.2, 90000)   # 下 = 速い。曲線が real-time 帯へ降りていく

for sp in ax.spines.values():
    sp.set_visible(False)

# real-time 域 (12 秒未満)
ax.axhspan(2.2, 12, facecolor=BAND_FC, zorder=0)
ax.axhline(12, color=GREEN, linewidth=1.5, linestyle=(0, (5, 4)), zorder=2)
ax.text(2022.12, 9.0, "12s = 1 slot", ha="left",
        va="center", fontsize=13.5, fontweight="bold", color=GREEN, zorder=6)

# y 軸目盛 (時間の直感単位)
yticks = [10, 60, 600, 3600, 14400]
ylabels = ["10 秒", "1 分", "10 分", "1 時間", "4 時間"]
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels, fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="y", length=0, pad=6)
ax.grid(axis="y", color="#f1f5f9", linewidth=1, zorder=0)
ax.set_axisbelow(True)

xticks = [2022, 2023, 2024, 2025, 2026]
ax.set_xticks(xticks)
ax.set_xticklabels([str(t) for t in xticks], fontsize=13, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="x", length=0, pad=8)

ax.text(2022.05, 60000, "zkVM によるブロック証明の生成時間の推移 (log)", ha="left", va="center",
        fontsize=13, fontweight="bold", color=TEXT_FAINT)

# ---------------------------------------------------------------- data
# 最速公表値の推移 (出典はスライド footer)。cluster = logo / label / sub の縦積み
pts = [
    {"x": 2022.5, "y": 21600, "label": "数時間 (zkVM 以前)", "sub": None, "logo": None,
     "lx": 2022.68, "ly": 21600, "ha": "left"},
    {"x": 2024.15, "y": 3100, "label": "SP1 Reth 約 52 分", "sub": "Succinct ｜ CPU 64 vCPU",
     "logo": "succinct.png", "lx": 2023.7, "ly": 1400, "sx": 2023.7, "sy": 850,
     "gx": 2023.7, "gy": 400},
    {"x": 2025.38, "y": 10.3, "label": "SP1 Hypercube 10.3 秒", "sub": "Succinct ｜ RTX 4090 クラスタ",
     "logo": "succinct.png", "lx": 2024.45, "ly": 110, "sx": 2024.45, "sy": 66,
     "gx": 2024.45, "gy": 230},
    {"x": 2025.8, "y": 6.9, "label": "Pico Prism 6.9 秒", "sub": "Brevis ｜ RTX 5090 × 64",
     "logo": "brevis.png", "lx": 2025.68, "ly": 230, "sx": 2025.68, "sy": 145,
     "gx": 2025.68, "gy": 420},
    {"x": 2026.38, "y": 6.1, "label": "Pico Prism 2.0 6.1 秒", "sub": "Brevis ｜ RTX 5090 × 16",
     "logo": "brevis.png", "lx": 2026.42, "ly": 58, "sx": 2026.42, "sy": 36,
     "gx": 2026.42, "gy": 120},
]

xs = [p["x"] for p in pts]
ys = [p["y"] for p in pts]
ax.plot(xs, ys, color=AMBER, linewidth=3.2, zorder=4,
        solid_capstyle="round", solid_joinstyle="round")
ax.scatter(xs, ys, s=95, facecolor=AMBER, edgecolor="white", linewidth=2.2, zorder=5)

for p in pts:
    ax.text(p["lx"], p["ly"], p["label"], ha=p.get("ha", "center"), va="center", fontsize=14,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    if p.get("sub"):
        ax.text(p["sx"], p["sy"], p["sub"], ha="center", va="center", fontsize=12,
                fontweight="bold", color=TEXT_MUTED, zorder=6)
    if p.get("logo"):
        path = f"{LOGO_DIR}/{p['logo']}"
        ab = AnnotationBbox(OffsetImage(mpimg.imread(path), zoom=logo_zoom(path)),
                            (p["gx"], p["gy"]), frameon=False, zorder=7)
        ax.add_artist(ab)

# EF の総括 (客観的事実のアンカー)
ax.text(2023.35, 130, "EF: 「証明レイテンシは 9 ヶ月で 16 分 → 16 秒に、\nコストは 1/45 に」 (2025/12)", ha="center",
        va="center", fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
