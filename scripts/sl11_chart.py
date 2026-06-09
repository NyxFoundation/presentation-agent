#!/usr/bin/env python3
"""Generate the population-vs-finance vertical bar chart for SL11."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm

# CJK fonts on this NixOS system live inside .ttc collections that are not
# auto-registered. Add them explicitly so the title/labels render properly.
for ttc in (
    "/nix/store/mn5jnlnx2hrazncjqq363izg2azginfh-noto-fonts-cjk-serif-2.003"
    "/share/fonts/opentype/noto-cjk/NotoSerifCJK-VF.otf.ttc",
    "/nix/store/nsnh5rygpcmfcnflfk8rdd7r94b5hv45-noto-fonts-cjk-sans-2.004"
    "/share/fonts/opentype/noto-cjk/NotoSansCJK-VF.otf.ttc",
):
    try:
        fm.fontManager.addfont(ttc)
    except Exception:
        pass

plt.rcParams["font.family"] = ["Noto Sans CJK JP", "Noto Serif CJK JP",
                               "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

BG = "#faf9f5"
INK = "#18181a"
INK_DIM = "#55524c"
INK_FAINT = "#9a958c"
ACCENT = "#1f3a52"
ACCENT_SOFT = "#e8edf2"
SEVERE = "#a25434"
LINE = "#cfcdc6"

fig, ax = plt.subplots(figsize=(13.5, 5.5), dpi=200, facecolor=BG)
ax.set_facecolor(BG)

Y_2016 = 500
Y_2060_REMAIN = 172
Y_2060_LOST = 328
Y_SAVE = 9.8

X_2016 = 0.0
X_2060 = 1.5
X_SAVE = 3.2

WIDTH = 0.55

# 2016 ── full bar
ax.bar(X_2016, Y_2016, WIDTH, color=INK, zorder=3)

# 2060 ── remaining (ink) + lost (severe hatched)
ax.bar(X_2060, Y_2060_REMAIN, WIDTH, color=INK, zorder=3)
ax.bar(
    X_2060,
    Y_2060_LOST,
    WIDTH,
    bottom=Y_2060_REMAIN,
    facecolor=SEVERE,
    alpha=0.18,
    edgecolor="none",
    zorder=3,
)
ax.add_patch(
    mpatches.Rectangle(
        (X_2060 - WIDTH / 2, Y_2060_REMAIN),
        WIDTH,
        Y_2060_LOST,
        fill=False,
        edgecolor=SEVERE,
        linewidth=1.4,
        linestyle=(0, (4, 3)),
        zorder=4,
    )
)

# 3% saved bar (accent) — sits on top of the ¥172億 remaining level
ax.bar(X_SAVE, Y_SAVE, WIDTH, bottom=Y_2060_REMAIN, color=ACCENT, zorder=3)

# Top numeric labels
ax.text(X_2016, Y_2016 + 70, "年間商品販売額", ha="center", fontsize=11,
        color=INK_DIM)
ax.text(X_2016, Y_2016 + 26, "¥ 500 億", ha="center", fontsize=20,
        color=INK, weight="bold")
ax.text(X_2060, Y_2060_REMAIN + Y_2060_LOST + 22, "¥ 328 億 失われる",
        ha="center", fontsize=17, color=SEVERE, weight="bold")
ax.text(X_2060, Y_2060_REMAIN / 2, "¥ 172 億", ha="center",
        va="center", fontsize=13, color="#faf9f5")
ax.text(X_SAVE, Y_2060_REMAIN + Y_SAVE + 60, "3 %", ha="center",
        fontsize=13, color=ACCENT, style="italic")
ax.text(X_SAVE, Y_2060_REMAIN + Y_SAVE + 26, "¥ 9.8 億", ha="center",
        fontsize=20, color=ACCENT, weight="bold")

# X-axis labels
ax.text(X_2016, -42, "2016 年", ha="center", fontsize=13, color=INK_DIM)
ax.text(X_2060, -42, "2060 年", ha="center", fontsize=13, color=INK_DIM)
ax.text(X_SAVE, Y_2060_REMAIN - 30, "私たちが守る規模", ha="center",
        fontsize=13, color=ACCENT, weight="bold")

# ── Callout pointing to the ¥9.8億 bar ──────────────────────────────
CX = 4.4
CY = 240
CW = 2.3
CH = 270

box = mpatches.FancyBboxPatch(
    (CX, CY - CH / 2),
    CW,
    CH,
    boxstyle="round,pad=0.02,rounding_size=0.05",
    linewidth=1.4,
    edgecolor=ACCENT,
    facecolor=ACCENT_SOFT,
    zorder=5,
)
ax.add_patch(box)

# Pointer from callout to the 9.8億 bar
ax.annotate(
    "",
    xy=(X_SAVE + WIDTH / 2 + 0.02, Y_2060_REMAIN + Y_SAVE / 2),
    xytext=(CX, CY),
    arrowprops=dict(arrowstyle="-", color=ACCENT, lw=1.2),
    zorder=6,
)

# 3 KPI items inside the callout
ITEM_Y = CY + CH / 2 - 50
LH = 70
items = [
    ("01", "事業承継",  "20 社"),
    ("02", "政策判断",  "30 件"),
    ("03", "観光データ", "1,000 件"),
]
for i, (num, head, val) in enumerate(items):
    y = ITEM_Y - i * LH
    ax.text(CX + 0.12, y, num, ha="left", va="center",
            fontsize=22, color=ACCENT, style="italic", zorder=7)
    ax.text(CX + 0.45, y + 12, head, ha="left", va="center",
            fontsize=12, color=INK_DIM, zorder=7)
    ax.text(CX + 0.45, y - 14, val, ha="left", va="center",
            fontsize=16, color=ACCENT, weight="bold", zorder=7)

# Style
ax.set_ylim(-70, 600)
ax.set_xlim(-0.6, 7.0)
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color(LINE)
ax.spines["bottom"].set_linewidth(1)
ax.set_xticks([])
ax.set_yticks([])
ax.tick_params(left=False, bottom=False)
ax.axhline(y=0, color=LINE, lw=1, zorder=1)

plt.tight_layout()
out = "/home/gohan/workspace/presentation-agent/public/images/sl11_chart.png"
plt.savefig(out, facecolor=BG, dpi=200, bbox_inches="tight", pad_inches=0.15)
print(f"saved → {out}")
