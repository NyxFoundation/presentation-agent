# prover_overhead.py — 証明系 3 系統と prover オーバーヘッドの定量推移 (SL17)
#
# 生成: uv run --with matplotlib python3 figures/prover_overhead.py
# 出力: public/images/prover_overhead.png
#
# 設計:
#   - 縦軸 = prover オーバーヘッド (native 実行の何倍遅いか, log)。下ほど速い。
#   - 系統を色で分ける: pairing 系 = グレー / STARK・FRI 系 = 青 / Sumcheck 系 = amber。
#     MPC-in-the-head 系 (Longfellow) は zkVM と同じ軸に乗らないため左下の green カードで併記。
#   - 値はすべて出典のある公表値・公表分析のみ (Thaler a16z 2022/2025, Jolt 2025)。
#   - 凡例なし。系統名は曲線・点への直接ラベル。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.patches import FancyBboxPatch
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
BLUE = "#2563eb"
AMBER = "#d97706"
GREEN = "#059669"
GREEN_FC = "#ecfdf5"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"
GRID = "#f1f5f9"

TARGET_LOGO_H = 30.0

def logo_zoom(path):
    img = mpimg.imread(path)
    return min(TARGET_LOGO_H / img.shape[0], 100.0 / img.shape[1])

fig, ax = plt.subplots(figsize=(13.2, 5.6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(2015.3, 2026.9)
ax.set_yscale("log")
ax.set_ylim(2e4, 6e7)

for sp in ax.spines.values():
    sp.set_visible(False)

yticks = [1e5, 1e6, 1e7]
ax.set_yticks(yticks)
ax.set_yticklabels([r"$10^5$ 倍", r"$10^6$ 倍", r"$10^7$ 倍"], fontsize=13,
                   fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="y", length=0, pad=6)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
ax.set_axisbelow(True)

xticks = [2016, 2018, 2020, 2022, 2024, 2026]
ax.set_xticks(xticks)
ax.set_xticklabels([str(t) for t in xticks], fontsize=13, fontweight="bold", color=TEXT_MUTED)
ax.tick_params(axis="x", length=0, pad=8)

ax.text(2015.45, 4.2e7, "prover オーバーヘッド (native 実行の何倍遅いか, log) — 下ほど速い",
        ha="left", va="center", fontsize=13.5, fontweight="bold", color=TEXT_FAINT)

# ---------------------------------------------------------------- pairing 系 (グレー)
ax.scatter([2016.2], [3e6], s=95, facecolor=GRAY, edgecolor="white", linewidth=2.2, zorder=5)
ax.text(2016.75, 1.05e7, "Groth16", ha="center", va="center", fontsize=15,
        fontweight="bold", color=GRAY)
ax.text(2016.75, 6.5e6, r"pairing 系 ｜ $10^6$-$10^7$ 倍", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)

# ---------------------------------------------------------------- STARK / FRI 系 (青)
sx = [2023.5, 2024.5]
sy = [1e6, 1e6]
ax.plot(sx, sy, color=BLUE, linewidth=3.2, zorder=4, solid_capstyle="round")
ax.scatter(sx, sy, s=95, facecolor=BLUE, edgecolor="white", linewidth=2.2, zorder=5)
ax.text(2024.0, 3.6e6, "STARK / FRI 系 zkVM", ha="center", va="center", fontsize=15,
        fontweight="bold", color=BLUE)
ax.text(2024.0, 2.2e6, r"RISC Zero ・ SP1 ｜ ~$10^6$ 倍で横ばい", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
for lx, logo in [(2023.5, "risc0.png"), (2024.5, "succinct.png")]:
    ab = AnnotationBbox(OffsetImage(mpimg.imread(f"{LOGO_DIR}/{logo}"),
                                    zoom=logo_zoom(f"{LOGO_DIR}/{logo}")),
                        (lx, 5.6e5), frameon=False, zorder=7)
    ax.add_artist(ab)
ax.text(2026.05, 6.8e6, "Stwo (circle STARK)\nStarknet mainnet (2025)", ha="center",
        va="center", fontsize=11.5, fontweight="bold", color=TEXT_MUTED)
ab = AnnotationBbox(OffsetImage(mpimg.imread(f"{LOGO_DIR}/starknet.png"),
                                zoom=logo_zoom(f"{LOGO_DIR}/starknet.png")),
                    (2026.05, 1.6e7), frameon=False, zorder=7)
ax.add_artist(ab)

# ---------------------------------------------------------------- Sumcheck 系 (amber)
ax.scatter([2025.6], [9e4], s=110, facecolor=AMBER, edgecolor="white", linewidth=2.2, zorder=5)
ax.text(2025.6, 3.6e4, r"Jolt ｜ $10^5$ 倍を切る (2025)", ha="center", va="center", fontsize=15,
        fontweight="bold", color=AMBER)
ax.text(2025.6, 2.55e4, "Sumcheck 系 ｜ ラップトップで 500 kHz 超", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED)
ab = AnnotationBbox(OffsetImage(mpimg.imread(f"{LOGO_DIR}/a16z.png"),
                                zoom=logo_zoom(f"{LOGO_DIR}/a16z.png")),
                    (2024.85, 9e4), frameon=False, zorder=7)
ax.add_artist(ab)
ax.text(2022.95, 1.32e5, "SP1 Hypercube も 2025 年に\nSumcheck 系へ刷新 → real-time 達成 (p8)",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color=TEXT_MUTED)

# 10 年の下降を 1 本の矢印で
ax.annotate("", xy=(2025.35, 1.15e5), xytext=(2016.55, 2.6e6),
            arrowprops=dict(arrowstyle="-|>", color="#d1d5db", lw=2.4,
                            linestyle=(0, (6, 4))))

# ---------------------------------------------------------------- MPC-in-the-head 系 (green カード)
# log 軸で座標指定しやすいよう axes fraction で置く
card = FancyBboxPatch((0.055, 0.065), 0.46, 0.30, transform=ax.transAxes,
                      boxstyle="round,pad=0.006,rounding_size=0.012",
                      linewidth=1.2, edgecolor="#a7f3d0", facecolor=GREEN_FC, zorder=2)
ax.add_patch(card)
ax.text(0.075, 0.315, "別系統: MPC-in-the-head (Ligero → Longfellow)",
        transform=ax.transAxes, ha="left", va="center", fontsize=13.5,
        fontweight="bold", color=GREEN, zorder=6)
ax.text(0.075, 0.235, "既存 ID の署名 (ECDSA + SHA-256) をそのまま ZK 化 — 発行者側の変更ゼロ",
        transform=ax.transAxes, ha="left", va="center", fontsize=12.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(0.075, 0.16, "スマホ実測: ECDSA 証明 ~20ms ／ mDL 提示証明 数百 ms (eprint 2024/2010)",
        transform=ax.transAxes, ha="left", va="center", fontsize=12.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(0.075, 0.085, "Google Wallet で稼働 (2025) ｜ Trail of Bits + Ligero 監査済 OSS",
        transform=ax.transAxes, ha="left", va="center", fontsize=12.5,
        fontweight="bold", color=TEXT_MUTED, zorder=6)
ab = AnnotationBbox(OffsetImage(mpimg.imread(f"{LOGO_DIR}/google.png"),
                                zoom=logo_zoom(f"{LOGO_DIR}/google.png")),
                    (0.462, 0.315), xycoords=ax.transAxes, frameon=False, zorder=7)
ax.add_artist(ab)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
