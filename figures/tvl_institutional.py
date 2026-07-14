# tvl_institutional.py — 全チェーン TVL 推移とその中の機関系サービス (SL10c)
#
# 生成: uv run --with matplotlib python3 figures/tvl_institutional.py
# 出力: public/images/tvl_institutional.png
#
# 設計:
#   - 左 = DeFi TVL (全チェーン, DefiLlama) の実年推移。単一の青い線 + 淡い面。
#   - 右 = 2026/7 時点でその中にいる機関系サービスの横棒 (ロゴ + 実額)。
#   - 右下に amber の問い「この機関マネー、2026-27 に 10 倍にするには？」
#   - 凡例なし。直接ラベル。RWA は別集計なので注記行で分ける (二重計上しない)。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/tvl_institutional.png"
LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

SURFACE = "#ffffff"
BLUE = "#2563eb"
BLUE_FILL = "#dbeafe"
AMBER = "#d97706"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"
GRID = "#f1f5f9"

fig = plt.figure(figsize=(13.2, 5.4), dpi=200)
fig.patch.set_facecolor(SURFACE)

# ---------------------------------------------------------------- TVL curve (left)
ax = fig.add_axes([0.055, 0.12, 0.52, 0.80])
ax.set_facecolor(SURFACE)

# DefiLlama historicalChainTvl (2026-07-14 取得)
pts = [
    (2020.99, 15.1), (2021.35, 90.0), (2021.86, 177.5), (2021.99, 163.3),
    (2022.45, 75.0), (2022.99, 38.3), (2023.99, 52.8), (2024.99, 115.9),
    (2025.99, 113.4), (2026.53, 73.1),
]
xs = [p[0] for p in pts]
ys = [p[1] for p in pts]
ax.fill_between(xs, ys, color=BLUE_FILL, alpha=0.55, zorder=2)
ax.plot(xs, ys, color=BLUE, linewidth=3.0, zorder=4,
        solid_capstyle="round", solid_joinstyle="round")

for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_xlim(2020.9, 2026.85)
ax.set_ylim(0, 205)
ax.set_yticks([0, 50, 100, 150, 200])
ax.set_yticklabels(["0", r"\$50B", r"\$100B", r"\$150B", r"\$200B"],
                   fontsize=12, fontweight="bold", color=TEXT_MUTED)
ax.set_xticks([2021, 2022, 2023, 2024, 2025, 2026])
ax.set_xticklabels(["2021", "2022", "2023", "2024", "2025", "2026"],
                   fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(length=0, pad=6)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)

ax.text(2021.0, 196, "DeFi TVL (全チェーン合計)", ha="left", va="center",
        fontsize=14.5, fontweight="bold", color=BLUE)

# milestones
ax.scatter([2021.86, 2026.53], [177.5, 73.1], s=80, facecolor=BLUE,
           edgecolor="white", linewidth=2.0, zorder=5)
ax.text(2021.95, 185, r"2021/11 ピーク \$177.5B", ha="left", va="center",
        fontsize=13, fontweight="bold", color=TEXT_PRIMARY)
ax.text(2026.28, 56, r"\$73.1B", ha="center", va="center",
        fontsize=13.5, fontweight="bold", color=TEXT_PRIMARY)
ax.text(2026.28, 44, "(2026/7)", ha="center", va="center",
        fontsize=11.5, fontweight="bold", color=TEXT_MUTED)

# ---------------------------------------------------------------- institutional (right)
axr = fig.add_axes([0.615, 0.05, 0.375, 0.90])
axr.set_facecolor(SURFACE)
axr.axis("off")
axr.set_xlim(0, 100)
axr.set_ylim(0, 100)

axr.text(0, 96, "この中にいる機関系サービス (2026/7)", ha="left", va="center",
         fontsize=14.5, fontweight="bold", color=TEXT_PRIMARY)

TARGET_LOGO_H = 26.0

def logo_zoom(path):
    img = mpimg.imread(path)
    return TARGET_LOGO_H / img.shape[0]

rows = [
    ("hyperliquid.png", "Hyperliquid", 6.24, "perp DEX"),
    ("ondo.png", "Ondo", 3.51, "RWA・国債"),
    ("maple.png", "Maple", 2.28, "機関融資"),
    ("lighter.png", "Lighter", 0.51, "perp DEX"),
]
BAR_X0, BAR_MAX_W = 30, 42
y = 84
for logo, name, val, tag in rows:
    path = f"{LOGO_DIR}/{logo}"
    ab = AnnotationBbox(OffsetImage(mpimg.imread(path), zoom=logo_zoom(path)),
                        (2.6, y), frameon=False, zorder=7)
    axr.add_artist(ab)
    axr.text(6.5, y + 2.2, name, ha="left", va="center", fontsize=13.5,
             fontweight="bold", color=TEXT_PRIMARY)
    axr.text(6.5, y - 3.4, tag, ha="left", va="center", fontsize=10.5,
             fontweight="bold", color=TEXT_FAINT)
    w = BAR_MAX_W * val / 6.24
    axr.add_patch(Rectangle((BAR_X0, y - 2.6), w, 5.2, facecolor=BLUE,
                            edgecolor="none", zorder=5))
    axr.text(BAR_X0 + w + 2, y, rf"\${val:.2f}B", ha="left", va="center",
             fontsize=13, fontweight="bold", color=TEXT_PRIMARY)
    y -= 13.5

axr.text(0, 26, r"+ RWA (トークン化資産) 全体 \$33.5B — rwa.xyz (別集計)", ha="left",
         va="center", fontsize=12, fontweight="bold", color=TEXT_MUTED)
axr.text(0, 18.5, "+ Tempo (Stripe + Paradigm): 2026/3 メインネット稼働", ha="left",
         va="center", fontsize=12, fontweight="bold", color=TEXT_MUTED)

axr.text(0, 5, "この機関マネー、2026-27 に 10 倍にするには？", ha="left", va="center",
         fontsize=16, fontweight="bold", color=AMBER)

plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
