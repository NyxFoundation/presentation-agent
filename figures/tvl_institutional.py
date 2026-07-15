# tvl_institutional.py — DeFi TVL 月次 bar と機関系サービスの内訳 + 未来の爆伸び (SL10c)
#
# 生成: uv run --with matplotlib python3 figures/tvl_institutional.py
# 出力: public/images/tvl_institutional.png
#
# 設計:
#   - 2025/07-2026/07 の月次積み上げ bar。下から機関系 4 サービス (色分け)、上に その他 DeFi (グレー)。
#     データは DefiLlama API (historicalChainTvl / protocol) の各月 1 日値 (2026-07-15 取得)。
#   - 2026/09 以降はゴースト bar (ハッチ + 半透明): 機関系が 10 倍に爆伸びするシナリオ。
#     実績とシナリオを隔てる破線 = 「壁」。壁には 3 つの吹き出し
#     (プライバシー / コンプライアンス / セキュリティ) を直接付ける。
#   - 凡例は上部のチップ行 (色 + 名前 + 最新値) で代替。固定順・色は entity に固定。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/tvl_institutional.png"

SURFACE = "#ffffff"
AMBER = "#d97706"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
GRID = "#f1f5f9"

# 色は entity に固定 (機関系 4 つ + その他)
C_HL = "#2563eb"     # Hyperliquid
C_ONDO = "#7c3aed"   # Ondo
C_MAPLE = "#0891b2"  # Maple
C_LIGHT = "#f59e0b"  # Lighter
C_OTHER = "#e5e7eb"  # その他 DeFi

months = ["2025/7", "8", "9", "10", "11", "12", "2026/1", "2", "3", "4", "5", "6", "7"]
total = [110.35, 135.73, 150.70, 155.29, 147.13, 115.33, 114.49, 106.26, 91.37, 94.01, 83.14, 79.91, 69.24]
hl    = [3.71, 4.89, 5.74, 5.83, 4.88, 4.35, 4.13, 4.49, 4.25, 4.93, 4.73, 5.61, 5.70]
ondo  = [1.39, 1.38, 1.40, 1.69, 1.78, 1.82, 1.93, 2.70, 2.72, 3.21, 3.53, 3.89, 3.56]
maple = [1.66, 1.84, 2.07, 2.51, 3.15, 2.64, 2.36, 2.59, 2.00, 2.47, 1.93, 2.03, 2.45]
light = [0.18, 0.20, 0.34, 0.74, 1.15, 1.23, 1.35, 0.97, 0.88, 0.51, 0.48, 0.51, 0.51]

inst_last = hl[-1] + ondo[-1] + maple[-1] + light[-1]   # 12.22
other = [t - (a + b + c + d) for t, a, b, c, d in zip(total, hl, ondo, maple, light)]

# 未来 (仮想シナリオ): 機関系が 2027 前半に向けて ~10 倍へ
ghost_months = ["2026/10", "2027/1", "2027/4"]
ghost_inst = [30, 65, 122]           # 12.2 → ~10x
ghost_other = [other[-1]] * 3        # その他は横ばいに固定

fig, ax = plt.subplots(figsize=(13.2, 5.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

BW = 0.72
xs = list(range(13))
gxs = [13.9, 15.0, 16.1]

for i in xs:
    y0 = 0
    for v, c in [(hl[i], C_HL), (ondo[i], C_ONDO), (maple[i], C_MAPLE), (light[i], C_LIGHT), (other[i], C_OTHER)]:
        ax.add_patch(Rectangle((i - BW / 2, y0), BW, v, facecolor=c,
                               edgecolor="white", linewidth=1.2, zorder=3))
        y0 += v

for gx, gi, go in zip(gxs, ghost_inst, ghost_other):
    ax.add_patch(Rectangle((gx - BW / 2, 0), BW, gi, facecolor=AMBER, alpha=0.30,
                           hatch="//", edgecolor=AMBER, linewidth=1.4,
                           linestyle=(0, (4, 3)), zorder=3))
    ax.add_patch(Rectangle((gx - BW / 2, gi), BW, go, facecolor=C_OTHER, alpha=0.45,
                           edgecolor="#9ca3af", linewidth=1.2,
                           linestyle=(0, (4, 3)), zorder=3))

# 実績とシナリオの境界
ax.axvline(13.1, color="#d1d5db", linewidth=1.4, linestyle=(0, (5, 4)), zorder=2)

for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_xlim(-0.7, 16.9)
ax.set_ylim(0, 215)
ax.set_yticks([0, 50, 100, 150, 200])
ax.set_yticklabels(["0", r"\$50B", r"\$100B", r"\$150B", r"\$200B"],
                   fontsize=12, fontweight="bold", color=TEXT_MUTED)
ax.set_xticks(xs + gxs)
ax.set_xticklabels(months + ghost_months, fontsize=11.5, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(length=0, pad=6)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)

# 上部チップ行 (凡例代替、固定順)
chips = [
    (C_HL, "Hyperliquid", hl[-1]), (C_ONDO, "Ondo", ondo[-1]),
    (C_MAPLE, "Maple", maple[-1]), (C_LIGHT, "Lighter", light[-1]),
    (C_OTHER, "その他 DeFi", None),
]
cx = -0.4
for c, name, v in chips:
    ax.add_patch(Rectangle((cx, 204), 0.32, 7, facecolor=c, edgecolor="none", zorder=6))
    label = f"{name} " + (rf"\${v:.1f}B" if v is not None else "")
    ax.text(cx + 0.5, 207.5, label, ha="left", va="center", fontsize=12.5,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    cx += 0.62 + len(label) * 0.145

ax.text(-0.4, 193, "DeFi TVL 月次 (全チェーン) — 下の色つきが機関系サービス", ha="left",
        va="center", fontsize=13, fontweight="bold", color=TEXT_MUTED, zorder=6)

# 実績側の機関系ブラケット (2026/7)
ax.annotate("", xy=(12.62, 0), xytext=(12.62, inst_last),
            arrowprops=dict(arrowstyle="-", color=TEXT_PRIMARY, lw=1.6))
ax.text(12.62, inst_last + 9, "機関系合計\n" + rf"\${inst_last:.1f}B (18%)", ha="center",
        va="bottom", fontsize=12, fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# 未来シナリオの問い (グラフ内で完結させる)
ax.text(14.5, 198, "？？？", ha="center", va="center", fontsize=30,
        fontweight="900", color=AMBER, zorder=6)
ax.text(14.5, 172, "機関系を 2026-27 で 10 倍に\n爆伸びさせるには？", ha="center", va="center",
        fontsize=14, fontweight="bold", color=AMBER, zorder=6)

# 壁 (破線) に付く 3 つの吹き出し = 10 倍を阻んでいるもの
WALL_X = 13.1
for wy, word in [(185, "プライバシー"), (150, "コンプライアンス"), (115, "セキュリティ")]:
    ax.text(11.9, wy, word, ha="center", va="center", fontsize=14,
            fontweight="bold", color=TEXT_PRIMARY, zorder=8,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                      edgecolor="#d1d5db", linewidth=1.2))
    ax.plot([12.78, WALL_X - 0.06], [wy, wy], color="#9ca3af", linewidth=1.6, zorder=7)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
