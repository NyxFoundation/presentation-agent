# prover_overhead.py — 証明系の理論と実装を 1 本のグラフに統合 (SL17)
#
# 生成: uv run --with matplotlib python3 figures/prover_overhead.py
# 出力: public/images/prover_overhead.png
#
# 設計:
#   - グラフは 1 個。上段の破線シェルフ = 理論マイルストーン (オーバーヘッド計測の対象外):
#     Sumcheck (1992) / GKR (2008) / Spartan・Nova (Microsoft) / Lasso / Longfellow (Google)。
#   - 下段の折れ線 = 実装の最速 prover オーバーヘッド (native 比, log。下ほど速い):
#     Groth16 → RISC Zero → SP1 → Jolt。点の色 = 系統 (グレー pairing / 青 STARK・FRI / amber Sumcheck)。
#   - シェルフから Jolt への破線矢印 = 「1992 年の理論が 2025 年に最速実装へ」。
#   - 値は出典のある公表値・公表分析のみ (Thaler a16z 2022/2025, Jolt 2025)。凡例なし。

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

OUT = "/home/gohan/workspace/presentation-agent/public/images/prover_overhead.png"
LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST = "#94a3b8"
BLUE = "#2563eb"
AMBER = "#d97706"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"
GRID = "#f1f5f9"

TARGET_LOGO_H = 28.0

def logo_zoom(path):
    img = mpimg.imread(path)
    return min(TARGET_LOGO_H / img.shape[0], 90.0 / img.shape[1])

def logo_at(name, x, y):
    path = f"{LOGO_DIR}/{name}"
    ab = AnnotationBbox(OffsetImage(mpimg.imread(path), zoom=logo_zoom(path)),
                        (x, y), frameon=False, zorder=7)
    ax.add_artist(ab)

fig, ax = plt.subplots(figsize=(13.2, 5.8), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(1989.5, 2028.5)
ax.set_yscale("log")
ax.set_ylim(2e4, 3.5e8)

for sp in ax.spines.values():
    sp.set_visible(False)

ax.set_yticks([1e5, 1e6, 1e7])
ax.set_yticklabels([r"$10^5$ 倍", r"$10^6$ 倍", r"$10^7$ 倍"], fontsize=13,
                   fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="y", length=0, pad=6)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)

xticks = [1992, 2000, 2008, 2016, 2020, 2024]
ax.set_xticks(xticks)
ax.set_xticklabels([str(t) for t in xticks], fontsize=13, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="x", length=0, pad=8)

ax.text(1990.0, 3.3e4, "実装の prover オーバーヘッド (native 実行の何倍遅いか, log) — 下ほど速い",
        ha="left", va="bottom", fontsize=13, fontweight="bold", color=TEXT_FAINT)

# ================================================================ 理論シェルフ (上段)
SHELF = 6.5e7
ax.axhline(SHELF, xmin=0.02, xmax=0.93, color=GHOST, linewidth=1.5,
           linestyle=(0, (6, 4)), zorder=2)
ax.text(1990.0, 1.35e8, "理論のマイルストーン (実装前 — オーバーヘッド計測の対象外)",
        ha="left", va="center", fontsize=13, fontweight="bold", color=TEXT_MUTED)

theory = [
    {"x": 1992, "label": "Sumcheck (LFKN)", "side": "up", "logo": None},
    {"x": 2008, "label": "GKR", "side": "up", "logo": None},
    {"x": 2019, "label": "Spartan / Nova", "side": "up", "logo": "microsoft.png",
     "sub": "Microsoft Research"},
    {"x": 2022.6, "label": "Lasso", "side": "downdeep", "logo": None},
    {"x": 2025.2, "label": "Longfellow", "side": "up", "logo": "google.png"},
]
for t in theory:
    ax.scatter([t["x"]], [SHELF], s=85, marker="D", facecolor="white",
               edgecolor=GRAY, linewidth=2.0, zorder=5)
    if t["side"] == "up":
        ax.text(t["x"], 1.0e8, t["label"], ha="center", va="center", fontsize=14,
                fontweight="bold", color=TEXT_PRIMARY, zorder=6)
        if t.get("sub"):
            ax.text(t["x"], 4.2e7, t["sub"], ha="center", va="center", fontsize=11.5,
                    fontweight="bold", color=TEXT_MUTED, zorder=6)
    else:
        yy = 2.5e7 if t["side"] == "downdeep" else 4.2e7
        ax.text(t["x"], yy, t["label"], ha="center", va="center", fontsize=14,
                fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    if t.get("logo"):
        logo_at(t["logo"], t["x"], 1.75e8)

# Longfellow の補足 (右上、シェルフ下に 2 行で)
ax.text(2026.3, 4.2e7, "既存 ID を ZK 化", ha="center", va="center", fontsize=11.5,
        fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(2026.5, 2.5e7, "Google Wallet 稼働", ha="center", va="center", fontsize=11.5,
        fontweight="bold", color=TEXT_MUTED, zorder=6)

# 理論 → 実装の橋 (Sumcheck/GKR/Lasso → Jolt)
ax.annotate("", xy=(2025.6, 1.6e5), xytext=(2023.9, 4.0e7),
            arrowprops=dict(arrowstyle="-|>", color=GHOST, lw=2.0,
                            linestyle=(0, (5, 4))))
ax.text(2021.9, 1.25e7, "1992 年の理論が\n2025 年に最速実装へ", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# ================================================================ 実装 frontier (下段)
fx = [2016.2, 2023.4, 2024.4, 2025.6]
fy = [3e6, 1e6, 1e6, 9e4]
ax.plot(fx, fy, color="#cbd5e1", linewidth=3.0, zorder=3,
        solid_capstyle="round", solid_joinstyle="round")
ax.scatter([fx[0]], [fy[0]], s=110, facecolor=GRAY, edgecolor="white", linewidth=2.2, zorder=5)
ax.scatter(fx[1:3], fy[1:3], s=110, facecolor=BLUE, edgecolor="white", linewidth=2.2, zorder=5)
ax.scatter([fx[3]], [fy[3]], s=125, facecolor=AMBER, edgecolor="white", linewidth=2.2, zorder=5)

# Groth16 (pairing 系)
ax.text(2016.2, 1.05e7, "Groth16", ha="center", va="center", fontsize=15,
        fontweight="bold", color=GRAY, zorder=6)
ax.text(2016.2, 6.3e6, r"pairing 系 ｜ $10^6$-$10^7$ 倍", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# RISC Zero / SP1 (STARK / FRI 系)
ax.text(2021.6, 1e6, "RISC Zero ・ SP1", ha="right", va="center", fontsize=15,
        fontweight="bold", color=BLUE, zorder=6)
ax.text(2021.6, 6.1e5, r"STARK / FRI 系 ｜ ~$10^6$ 倍で横ばい", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)
logo_at("risc0.png", 2022.3, 4.6e5)
logo_at("succinct.png", 2025.15, 4.6e5)

# Jolt (Sumcheck 系)
ax.text(2026.0, 3.3e4, r"Jolt ｜ Sumcheck 系 ｜ $10^5$ 倍を切る (2025)", ha="right",
        va="center", fontsize=15, fontweight="bold", color=AMBER, zorder=6)
logo_at("a16z.png", 2026.6, 9e4)

# SP1 の Sumcheck 化の注記
ax.text(2027.55, 6.5e5, "SP1 も 2025 年に\nSumcheck 系へ刷新\n(→ real-time, p8)",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
