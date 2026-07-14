# hack_pie.py — 2025 年クリプト流出の攻撃ベクトル別内訳 (SL10)
#
# 生成: uv run --with matplotlib python3 figures/hack_pie.py
# 出力: public/images/hack_breakdown_2025.png
#
# 設計:
#   - ドーナツ (左) = 事実。Hacken 2025 Yearly Security Report の分類・金額。
#   - 右側 = 各領域に対する暗号の防ぎ方 (green = 防御、デッキの色語彙に従う)。
#   - 色は p3 (scope_gap_chart) と同義: グレー = コード脆弱性 (監査対象内)、
#     赤系 = 監査の外 (アクセス侵害 / 社会工学)。
#   - 凡例なし。スライス外の直接ラベル + 右のマッピング行で読ませる。

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
ax = fig.add_axes([0.015, 0.04, 0.42, 0.92])
ax.set_facecolor(SURFACE)
ax.axis("off")

# Hacken 2025 Yearly Security Report (total ~$3.95B)
vals = [2.12, 1.32, 0.51]           # $B
labels = ["アクセス侵害", "社会工学・その他", "コード脆弱性"]
colors = [RED, RED_LIGHT, GRAY]
pcts = [54, 33, 13]

wedges, _ = ax.pie(
    vals, colors=colors, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.42, edgecolor=SURFACE, linewidth=3),
)
ax.set_aspect("equal")

ax.text(0, 0.10, "2025 年", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_MUTED)
ax.text(0, -0.14, r"\$3.95B", ha="center", va="center", fontsize=26,
        fontweight="900", color=TEXT_PRIMARY)
ax.text(0, -0.35, "約 5,900 億円", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_FAINT)

# スライス外の直接ラベル (位置は手置き)
ax.text(0.68, 0.98, "アクセス侵害 54%", ha="left", va="center", fontsize=16,
        fontweight="bold", color=RED)
ax.text(0.68, 0.80, r"秘密鍵・署名者・運用インフラ" "\n" r"\$2.12B ｜ 例: Bybit \$1.46B", ha="left",
        va="center", fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-0.72, -1.02, "社会工学・その他 33%", ha="center", va="center", fontsize=16,
        fontweight="bold", color="#dc2626", alpha=0.75)
ax.text(-0.72, -1.24, r"フィッシング・詐欺誘導 等 ｜ \$1.32B", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-1.12, 0.72, "コード脆弱性 13%", ha="right", va="center", fontsize=16,
        fontweight="bold", color=GRAY)
ax.text(-1.12, 0.52, r"smart contract バグ" "\n" r"\$0.51B ｜ 例: Cetus \$223M", ha="right",
        va="center", fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-1.45, 1.45)

# ---------------------------------------------------------------- mapping (right)
axr = fig.add_axes([0.46, 0.04, 0.53, 0.92])
axr.set_facecolor(SURFACE)
axr.axis("off")
axr.set_xlim(0, 100)
axr.set_ylim(0, 100)

axr.text(2, 97, "この内訳に、暗号は何を足せるか", ha="left", va="center",
         fontsize=15, fontweight="bold", color=TEXT_PRIMARY)

rows = [
    {
        "y": 84, "color": RED, "head": "アクセス侵害 54%",
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
        "y": 20, "color": GRAY, "head": "コード脆弱性 13%",
        "lines": [
            ("形式検証・監査", "既存の守備範囲 — ここは今も機能している"),
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
        yy = y - 7.5 - i * 7.5
        axr.text(6.4, yy, tech, ha="left", va="center", fontsize=13.5,
                 fontweight="bold", color=GREEN)
        axr.text(34.5, yy, desc, ha="left", va="center", fontsize=13,
                 fontweight="bold", color=TEXT_MUTED)

plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
