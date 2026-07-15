# hack_pie.py — 2025 年クリプト流出の攻撃ベクトル別内訳 (SL10)
#
# 生成: uv run --with matplotlib python3 figures/hack_pie.py
# 出力: public/images/hack_breakdown_2025.png
#
# 設計:
#   - 1 面構成のドーナツ。各カテゴリの注釈 (ラベル + 金額) の直下に
#     「どうやったら解決できるのかの例」を green で直接書き込む。
#   - 色は p4 (scope_gap_chart) と同義: グレー = コード脆弱性 (監査対象内)、赤系 = 監査対象外。
#   - 金額は円建てに統一 ($1 = ¥150 概算、脚注はスライド側)。凡例なし。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

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

fig, ax = plt.subplots(figsize=(13.2, 5.9), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.axis("off")

# Hacken 2025 Yearly Security Report (total ~$3.95B ≒ 約 5,900 億円)
vals = [2.12, 1.32, 0.51]           # アクセス侵害 / 社会工学・その他 / コード脆弱性
colors = [RED, RED_LIGHT, GRAY]

ax.pie(vals, colors=colors, startangle=90, counterclock=False,
       wedgeprops=dict(width=0.42, edgecolor=SURFACE, linewidth=3))
ax.set_aspect("equal")

ax.text(0, 0.13, "2025 年", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_MUTED)
ax.text(0, -0.13, "約 5,900 億円", ha="center", va="center", fontsize=22,
        fontweight="900", color=TEXT_PRIMARY)

def cluster(x, ha, rows):
    """rows: (y, text, color, fontsize)"""
    for y, text, color, fs in rows:
        ax.text(x, y, text, ha=ha, va="center", fontsize=fs,
                fontweight="bold", color=color, zorder=6)

# ---- アクセス侵害 54% (右)
cluster(1.45, "left", [
    (0.98, "アクセス侵害 54%", RED, 16),
    (0.77, "秘密鍵・署名者・運用 ｜ 約 3,180 億円", TEXT_MUTED, 12.5),
    (0.59, "例: Bybit 約 2,190 億円", TEXT_MUTED, 12.5),
    (0.32, "解決例: threshold 署名によるアクセス権利の分散", GREEN, 13),
    (0.13, "解決例: 生体認証による秘密鍵の堅牢化", GREEN, 13),
])

# ---- コード脆弱性 13% (左上)
cluster(-1.45, "right", [
    (1.22, "コード脆弱性 13%", GRAY, 16),
    (1.01, "約 765 億円 ｜ 例: Cetus 約 335 億円", TEXT_MUTED, 12.5),
    (0.76, "解決例: 形式検証による正しさの証明", GREEN, 13),
    (0.57, "解決例: Proof-of-Exploit による自動遮断 (前ページ)", GREEN, 13),
])

# ---- 社会工学・その他 33% (左下)
cluster(-1.45, "right", [
    (-0.32, "社会工学・その他 33%", "#dc2626", 16),
    (-0.53, "フィッシング・詐欺誘導 等 ｜ 約 1,980 億円", TEXT_MUTED, 12.5),
    (-0.78, "解決例: アクセス先サイトが安全であることの証明", GREEN, 13),
    (-0.97, "解決例: FHE — マルウェアに侵入されてもデータを読めなくする", GREEN, 13),
])

ax.set_xlim(-4.05, 4.05)
ax.set_ylim(-1.55, 1.55)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
