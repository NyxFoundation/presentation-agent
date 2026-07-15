# hack_pie.py — 2025 年クリプト流出の攻撃ベクトル別内訳 (SL10)
#
# 生成: uv run --with matplotlib python3 figures/hack_pie.py
# 出力: public/images/hack_breakdown_2025.png
#
# 設計:
#   - ドーナツ (左) = 事実。Hacken 2025 Yearly Security Report の分類・金額。
#   - 監査対象外の 2 スライス (赤系, 87%) を緑の外周アークで束ね
#     「暗号で検証可能にできる領域」であることを図から直接読ませる。
#   - 右側 = その 87% への暗号の効き方 (green = 防御、デッキの色語彙に従う)。
#   - 色は p3 (scope_gap_chart) と同義: グレー = コード脆弱性 (監査対象内)、赤系 = 監査対象外。
#   - 凡例なし。スライス外の直接ラベル + 右のマッピング行で読ませる。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle, Wedge

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/hack_breakdown_2025.png"

SURFACE = "#ffffff"
GRAY = "#475569"
RED = "#dc2626"
RED_LIGHT = "#f87171"
GREEN = "#059669"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"

fig = plt.figure(figsize=(13.2, 5.9), dpi=200)
fig.patch.set_facecolor(SURFACE)

# ---------------------------------------------------------------- donut (left)
ax = fig.add_axes([0.005, 0.02, 0.445, 0.96])
ax.set_facecolor(SURFACE)
ax.axis("off")

# Hacken 2025 Yearly Security Report (total ~$3.95B)
vals = [2.12, 1.32, 0.51]           # アクセス侵害 / 社会工学・その他 / コード脆弱性 ($B)
colors = [RED, RED_LIGHT, GRAY]

wedges, _ = ax.pie(
    vals, colors=colors, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.42, edgecolor=SURFACE, linewidth=3),
)
ax.set_aspect("equal")

# 監査対象外 87% (アクセス侵害 + 社会工学) を束ねる緑の外周アーク
# counterclock=False, start=90°: 87% は 90° から時計回りに 313.2° → ccw では 136.8° → 90°
ax.add_patch(Wedge((0, 0), 1.30, 136.8, 90.0, width=0.055, facecolor=GREEN,
                   edgecolor="none", zorder=6))

ax.text(0, 0.10, "2025 年", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_MUTED)
ax.text(0, -0.14, r"\$3.95B", ha="center", va="center", fontsize=26,
        fontweight="900", color=TEXT_PRIMARY)
ax.text(0, -0.35, "約 5,900 億円", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_FAINT)

# スライス外の直接ラベル (位置は手置き、重なり禁止)
ax.text(2.35, 1.52, "アクセス侵害 54%", ha="right", va="center", fontsize=16,
        fontweight="bold", color=RED)
ax.text(2.35, 1.31, r"秘密鍵・署名者・運用 ｜ \$2.12B", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.text(2.35, 1.12, r"例: Bybit \$1.46B", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-1.44, -0.42, "社会工学・その他 33%", ha="right", va="center", fontsize=16,
        fontweight="bold", color="#dc2626", alpha=0.75)
ax.text(-1.44, -0.63, "フィッシング・詐欺誘導 等", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.text(-1.44, -0.81, r"\$1.32B", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-1.18, 1.22, "コード脆弱性 13%", ha="right", va="center", fontsize=16,
        fontweight="bold", color=GRAY)
ax.text(-1.18, 1.01, r"\$0.51B ｜ 例: Cetus \$223M", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

# 緑アークの意味 (下)
ax.text(0.1, -1.58, "赤 87% = 監査対象外 — 暗号で検証可能にできる領域", ha="center",
        va="center", fontsize=14.5, fontweight="bold", color=GREEN)

ax.set_xlim(-2.45, 2.45)
ax.set_ylim(-1.78, 1.68)

# ---------------------------------------------------------------- mapping (right)
axr = fig.add_axes([0.475, 0.02, 0.515, 0.96])
axr.set_facecolor(SURFACE)
axr.axis("off")
axr.set_xlim(0, 100)
axr.set_ylim(0, 100)

axr.text(2, 96, "監査対象外の 87% を、暗号でどうカバーするか", ha="left", va="center",
         fontsize=15, fontweight="bold", color=TEXT_PRIMARY)

rows = [
    {
        "y": 83, "color": RED, "head": "アクセス侵害 54%",
        "lines": [
            ("threshold 署名 (MPC)", "鍵と承認を分散 — 単一の鍵・署名者が存在しない"),
            ("ZK 証明", "「運用が規定通り」を暗号で検証 — RPC・ガバナンス・UI (p6)"),
        ],
    },
    {
        "y": 52, "color": RED_LIGHT, "head": "社会工学・その他 33%",
        "lines": [
            ("MPC 合議 + ZK", "1 人が騙されても、表示と署名内容の一致を検証してから実行"),
            ("FHE", "処理中のデータを平文にしない — 盗んでも読めない"),
        ],
    },
    {
        "y": 21, "color": GRAY, "head": "コード脆弱性 13% — 既存監査の領域",
        "lines": [
            ("形式検証・監査", "ここは今も機能している"),
            ("Proof-of-Exploit", "AI が見つけた exploit の存在を ZK 証明 → 自動遮断 (p6)"),
        ],
    },
]

for r in rows:
    y = r["y"]
    axr.add_patch(Rectangle((2, y - 1.6), 2.6, 5.2, facecolor=r["color"], edgecolor="none"))
    axr.text(6.4, y + 1, r["head"], ha="left", va="center", fontsize=15,
             fontweight="bold", color=TEXT_PRIMARY)
    for i, (tech, desc) in enumerate(r["lines"]):
        yy = y - 8 - i * 7.5
        axr.text(6.4, yy, tech, ha="left", va="center", fontsize=13.5,
                 fontweight="bold", color=GREEN)
        axr.text(35, yy, desc, ha="left", va="center", fontsize=13,
                 fontweight="bold", color=TEXT_MUTED)

plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
