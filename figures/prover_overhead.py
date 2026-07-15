# prover_overhead.py — 証明系 30 年の performance を 1 本の線で (SL17)
#
# 生成: uv run --with matplotlib python3 figures/prover_overhead.py
# 出力: public/images/prover_overhead.png
#
# 設計:
#   - 線は 1 本だけ。1992 (Sumcheck) から 2025 (Jolt) まで降りてくる。
#     破線区間 = 理論のみ (実装が無くオーバーヘッド計測なし)、実線区間 = 実装の最速値。
#   - 縦軸 = 証明オーバーヘッド (native 実行の何倍遅いか, log)。下ほど速い。
#   - 点の色 = 系統: グレー = pairing / 青 = STARK・FRI / amber = Sumcheck。
#     理論点 (Sumcheck / GKR) は白抜きダイヤ。
#   - Longfellow (Google) は zkVM と別指標のため右上の注記で併載。
#   - 実測値の出典: Thaler a16z (2022 / 2025-03), a16z Jolt (2025-08)。
#     Spartan / Nova の点は系譜上の中継点 (公表オーバーヘッド値なし、位置は模式)。

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
LINE = "#cbd5e1"
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
ax.set_xlim(1989.5, 2029.6)
ax.set_yscale("log")
ax.set_ylim(2.4e4, 6.5e7)

for sp in ax.spines.values():
    sp.set_visible(False)

ax.set_yticks([1e5, 1e6, 1e7])
ax.set_yticklabels([r"$10^5$ 倍", r"$10^6$ 倍", r"$10^7$ 倍"], fontsize=13,
                   fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="y", length=0, pad=6)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)

xticks = [1992, 2000, 2008, 2016, 2024]
ax.set_xticks(xticks)
ax.set_xticklabels([str(t) for t in xticks], fontsize=13, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="x", length=0, pad=8)

ax.text(1990.0, 2.9e4, "証明オーバーヘッド (native 実行の何倍遅いか, log) — 下ほど速い",
        ha="left", va="center", fontsize=13, fontweight="bold", color=TEXT_FAINT)

# ================================================================ 1 本の線
THEORY_Y = 2.3e7
# 破線区間 (理論のみ) : 1992 → 2008 → Groth16 の実装で降下開始
ax.plot([1992, 2008, 2016.2], [THEORY_Y, THEORY_Y, 3e6], color=LINE, linewidth=3.0,
        linestyle=(0, (5, 4)), zorder=3, solid_capstyle="round")
# 実線区間 (実装の最速値)
ax.plot([2016.2, 2019.5, 2023.4, 2024.4, 2025.6], [3e6, 1.6e6, 1e6, 1e6, 9e4],
        color=LINE, linewidth=3.2, zorder=3, solid_capstyle="round", solid_joinstyle="round")

# 理論点 (白抜きダイヤ)
ax.scatter([1992, 2008], [THEORY_Y, THEORY_Y], s=95, marker="D", facecolor="white",
           edgecolor=GRAY, linewidth=2.0, zorder=5)
# 実装点 (色 = 系統)
ax.scatter([2016.2], [3e6], s=110, facecolor=GRAY, edgecolor="white", linewidth=2.2, zorder=5)
ax.scatter([2019.5], [1.6e6], s=100, facecolor=AMBER, edgecolor="white", linewidth=2.2, zorder=5)
ax.scatter([2023.4, 2024.4], [1e6, 1e6], s=110, facecolor=BLUE, edgecolor="white",
           linewidth=2.2, zorder=5)
ax.scatter([2025.6], [9e4], s=125, facecolor=AMBER, edgecolor="white", linewidth=2.2, zorder=5)

# ================================================================ ラベル
# 各点: ロゴ / 写真 → 名前 → 系統 (それ以外の文言は置かない)

# Sumcheck (LFKN 1992) — Noam Nisan の写真
logo_at("nisan.jpg", 1992, 5.2e7)
ax.text(1990.0, 3.3e7, "Sumcheck (LFKN)", ha="left", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(2000, 1.32e7, "理論の時代 — 実装なし (破線)", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# GKR (2008) — Shafi Goldwasser の写真
logo_at("goldwasser.jpg", 2008, 5.2e7)
ax.text(2008, 3.3e7, "GKR", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# Longfellow (Google) — 右上に併記
logo_at("google.png", 2024.4, 5.2e7)
ax.text(2024.4, 3.3e7, "Longfellow (Google)", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(2024.4, 2.25e7, "MPC-in-the-head 系", ha="center", va="center", fontsize=12.5,
        fontweight="bold", color=TEXT_MUTED, zorder=6)

# Groth16 (写真・ロゴなし)
ax.text(2015.3, 4.4e6, "Groth16", ha="right", va="center", fontsize=15,
        fontweight="bold", color=GRAY, zorder=6)
ax.text(2015.3, 2.85e6, "pairing 系", ha="right", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# Spartan / Nova (Microsoft)
logo_at("microsoft.png", 2017.9, 8.2e5)
ax.text(2017.9, 5.0e5, "Spartan / Nova", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(2017.9, 3.4e5, "Sumcheck 系", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# RISC Zero / SP1 (STARK / FRI 系)
ax.text(2023.65, 2.4e6, "STARK / FRI 系", ha="center", va="center", fontsize=13,
        fontweight="bold", color=BLUE, zorder=6)
logo_at("risc0.png", 2022.2, 6.4e5)
ax.text(2022.2, 4.1e5, "RISC Zero", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
logo_at("succinct.png", 2025.9, 6.4e5)
ax.text(2025.9, 4.1e5, "SP1 (Succinct)", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# Jolt (a16z)
logo_at("a16z.png", 2027.6, 2.2e5)
ax.text(2027.6, 1.05e5, "Jolt (a16z)", ha="center", va="center", fontsize=14,
        fontweight="bold", color=AMBER, zorder=6)
ax.text(2027.6, 6.3e4, "Sumcheck 系", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
