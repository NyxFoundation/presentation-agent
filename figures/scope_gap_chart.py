import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import numpy as np

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

JPY_RATE = 150  # $1 = ¥150 (概算換算レート、注記あり)

years = ["2021", "2022", "2023", "2024", "2025"]
totals_usd_b = [3.2, 3.8, 1.7, 2.2, 3.4]  # $B, Chainalysis annual totals
# 1 $B = 10^9 USD -> yen = 10^9 * JPY_RATE -> 億円(1億=10^8) = *JPY_RATE*10
totals = [round(t * JPY_RATE * 10) for t in totals_usd_b]  # 億円

# 2-category share of total, per year (see slide footnote for sources/methodology)
in_scope_pct = [0.470, 0.470, 0.182, 0.150, 0.121]   # コード脆弱性 (audit-scope)
out_scope_pct = [1 - p for p in in_scope_pct]         # 監査対象外

in_scope = [t * p for t, p in zip(totals, in_scope_pct)]
out_scope = [t - i for t, i in zip(totals, in_scope)]

GRAY = "#475569"
RED = "#dc2626"
SURFACE = "#ffffff"   # match slide background exactly
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
GRID = "#e5e7eb"

fig, (ax, ax_strip) = plt.subplots(
    2, 1, figsize=(13.2, 6.9), dpi=200,
    gridspec_kw={"height_ratios": [5.6, 1]}
)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax_strip.set_facecolor(SURFACE)

x = np.arange(len(years))
bar_w = 0.52
gap = 37.5

ax.bar(x, [v - gap for v in in_scope], width=bar_w, bottom=0, color=GRAY,
       zorder=3, label="コード脆弱性（監査対象内）")
ax.bar(x, out_scope, width=bar_w, bottom=[v + gap for v in in_scope], color=RED,
       zorder=3, label="監査対象外（秘密鍵・アクセス侵害／ガバナンス・社会工学等）")

for xi, i_val, o_val in zip(x, in_scope, out_scope):
    top = i_val + gap + o_val
    ax.add_patch(FancyBboxPatch(
        (xi - bar_w / 2, top - 105), bar_w, 105,
        boxstyle="round,pad=0,rounding_size=0.02",
        linewidth=0, facecolor=RED, zorder=4, mutation_aspect=1500
    ))

for i, xi in enumerate(x):
    mid_y = in_scope[i] + gap + out_scope[i] / 2
    ax.text(xi, mid_y, f"{out_scope_pct[i]*100:.0f}%", ha="center", va="center",
             fontsize=15, fontweight="bold", color="white", zorder=5)

for xi, t in zip(x, totals):
    ax.text(xi, t + 180, f"{t:,.0f}億円", ha="center", va="bottom",
             fontsize=14, fontweight="bold", color=TEXT_PRIMARY, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=15, color=TEXT_PRIMARY, fontweight="bold")
ax.set_ylim(0, 6750)
ax.set_xlim(-0.6, 4.6)
ax.set_yticks([0, 1500, 3000, 4500, 6000])
ax.set_yticklabels(["0", "1,500億円", "3,000億円", "4,500億円", "6,000億円"], fontsize=12, color=TEXT_MUTED)

ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)

legend = ax.legend(
    loc="lower left", bbox_to_anchor=(0.0, 1.02), ncol=1,
    frameon=False, fontsize=12.5,
    handlelength=1.1, handleheight=1.1, borderpad=0.3, labelspacing=0.5,
)
for text in legend.get_texts():
    text.set_color(TEXT_PRIMARY)


def draw_building_icon(ax_, cx, cy, scale=0.6, color="#475569"):
    w, h = scale * 1.6, scale * 1.1
    roof = Polygon([(cx - w / 2 - scale * 0.15, cy), (cx, cy + h * 0.9),
                     (cx + w / 2 + scale * 0.15, cy)], closed=True, facecolor=color, zorder=8)
    body = Rectangle((cx - w / 2, cy - h), w, h, facecolor=color, zorder=8)
    ax_.add_patch(roof)
    ax_.add_patch(body)
    col_w = w * 0.12
    for i in range(4):
        cxp = cx - w / 2 + w * (0.15 + i * 0.24)
        ax_.add_patch(Rectangle((cxp, cy - h * 0.82), col_w, h * 0.62, facecolor=SURFACE, zorder=9))


def add_logo(ax_, path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, zorder=7, box_alignment=box_alignment)
    ax_.add_artist(ab)


# ---- Footer strip: logo + one-line label, evenly spaced ----
ax_strip.set_xlim(0, 4)
ax_strip.set_ylim(0, 1)
ax_strip.axis("off")

# zoom はロゴの実寸から逆算して統一する (実寸×固定 zoom はロゴ差し替えでサイズが
# 化けるので禁止)。基準: openai 128px × 0.34 の見た目 (高さ ~44)。ワードマーク
# (DMM/Bybit) は幅上限で抑えて正方形アイコンより支配的に見えないようにする
TARGET_H = 43.5
MAX_W = 120

def logo_zoom(logo_file):
    img = mpimg.imread(f"{LOGO_DIR}/{logo_file}")
    h, w = img.shape[0], img.shape[1]
    return min(TARGET_H / h, MAX_W / w)

icon_y = 0.68
items = [
    {"cx": 0.5, "parts": ["openai.png"], "label": "GPT-4 リリース"},
    {"cx": 1.5, "parts": ["dmmbitcoin.png"], "label": "DMM Bitcoin　458億円 ハッキング"},
    {"cx": 2.5, "parts": ["bybit.png"], "label": "Bybit　2,250億円 ハッキング"},
    {"cx": 3.5, "parts": ["kelpdao.png", "layerzero.png"], "label": "KelpDAO×LayerZero　438億円 ハッキング"},
]

for it in items:
    cx = it["cx"]
    if it["parts"] is None:
        draw_building_icon(ax_strip, cx, icon_y + 0.06, scale=0.16)
    elif len(it["parts"]) == 1:
        logo_file = it["parts"][0]
        add_logo(ax_strip, f"{LOGO_DIR}/{logo_file}", (cx, icon_y), zoom=logo_zoom(logo_file))
    else:
        offsets = [-0.15, 0.15]
        for logo_file, dx in zip(it["parts"], offsets):
            add_logo(ax_strip, f"{LOGO_DIR}/{logo_file}", (cx + dx, icon_y), zoom=logo_zoom(logo_file))
    ax_strip.text(cx, 0.12, it["label"], ha="center", va="center",
                   fontsize=11.5, fontweight="bold", color=TEXT_PRIMARY, zorder=7)

plt.tight_layout(pad=1.0, h_pad=0.6)
plt.savefig("/home/gohan/workspace/presentation-agent/public/images/scope_gap_chart.png",
            facecolor=SURFACE, bbox_inches="tight")
print("saved. font used:", font_family)
