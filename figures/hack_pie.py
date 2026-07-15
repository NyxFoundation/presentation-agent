# hack_pie.py — 2025 年クリプト流出の攻撃ベクトル別内訳 (SL10)
#
# 生成: uv run --with matplotlib python3 figures/hack_pie.py
# 出力: public/images/hack_breakdown_2025.png
#
# 設計:
#   - ドーナツ (左) = 事実。Hacken 2025 Yearly Security Report の分類・金額。
#   - 赤系 2 スライス = 監査対象外 (87%)。右側 = 各カテゴリへの対策例 (green)。
#   - 金額は円建てに統一 ($1 = ¥150 概算、脚注はスライド側)。
#   - 色は p3 (scope_gap_chart) と同義: グレー = コード脆弱性 (監査対象内)、赤系 = 監査対象外。
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

ax.text(0, 0.13, "2025 年", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_MUTED)
ax.text(0, -0.13, "約 5,900 億円", ha="center", va="center", fontsize=23,
        fontweight="900", color=TEXT_PRIMARY)

# スライス外の直接ラベル (位置は手置き、重なり禁止)
ax.text(2.35, 1.52, "アクセス侵害 54%", ha="right", va="center", fontsize=16,
        fontweight="bold", color=RED)
ax.text(2.35, 1.31, "秘密鍵・署名者・運用 ｜ 約 3,180 億円", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.text(2.35, 1.12, "例: Bybit 約 2,190 億円", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-1.44, -0.42, "社会工学・その他 33%", ha="right", va="center", fontsize=16,
        fontweight="bold", color="#dc2626", alpha=0.75)
ax.text(-1.44, -0.63, "フィッシング・詐欺誘導 等", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ax.text(-1.44, -0.81, "約 1,980 億円", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.text(-1.18, 1.22, "コード脆弱性 13%", ha="right", va="center", fontsize=16,
        fontweight="bold", color=GRAY)
ax.text(-1.18, 1.01, "約 765 億円 ｜ 例: Cetus 約 335 億円", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

ax.set_xlim(-2.45, 2.45)
ax.set_ylim(-1.55, 1.68)

# ---------------------------------------------------------------- mapping (right)
axr = fig.add_axes([0.475, 0.02, 0.515, 0.96])
axr.set_facecolor(SURFACE)
axr.axis("off")
axr.set_xlim(0, 100)
axr.set_ylim(0, 100)

rows = [
    {
        "y": 90, "color": RED, "head": "アクセス侵害 54%",
        "lines": [
            "threshold 署名を用いたアクセス権利の分散",
            "生体認証による秘密鍵の堅牢化",
        ],
    },
    {
        "y": 57, "color": RED_LIGHT, "head": "社会工学・その他 33%",
        "lines": [
            "アクセス先サイトが安全であることの証明",
            "FHE — マルウェアに侵入されてもデータを読めなくする",
        ],
    },
    {
        "y": 24, "color": GRAY, "head": "コード脆弱性 13% — 既存監査の領域",
        "lines": [
            "形式検証による正しさの証明",
            "Proof-of-Exploit による自動遮断 (前ページ)",
        ],
    },
]

for r in rows:
    y = r["y"]
    axr.add_patch(Rectangle((2, y - 1.6), 2.6, 5.2, facecolor=r["color"], edgecolor="none"))
    axr.text(6.4, y + 1, r["head"], ha="left", va="center", fontsize=15,
             fontweight="bold", color=TEXT_PRIMARY)
    for i, line in enumerate(r["lines"]):
        yy = y - 8 - i * 7.5
        axr.text(6.4, yy, line, ha="left", va="center", fontsize=13.5,
                 fontweight="bold", color=GREEN)

plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
