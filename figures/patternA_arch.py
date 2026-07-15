# patternA_arch.py — パターン A (RISC Zero / Rust) の具体システム構成 (SL25c)
#
# 生成: uv run --with matplotlib python3 figures/patternA_arch.py
# 出力: public/images/patternA_arch.png
#
# 設計語彙は figures/kelp_arch.py / req_map_arch.py に従う:
#   左→右の pipeline。各ノードは実コード / ロゴ / アイコンで見せ、
#   機能要件 (どの言語・いつ WitnessGen/Prove/Verify するか・マシン制約) を
#   各ノードの下に添字する。zkVM 実行は Witness Generation と Proving の
#   2 ノードに分ける。Verify 通過後は 報酬支払い + 復号鍵 → プロバイダ修正 に分岐。
#   各 box の中身は center 揃えで統一する。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.patches import (FancyArrowPatch, FancyBboxPatch, Circle,
                                Rectangle, Polygon)
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"
OUT = "/home/gohan/workspace/presentation-agent/public/images/patternA_arch.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GREEN = "#059669"
AMBER = "#d97706"
BLUE = "#2563eb"
CODE_BG = "#1f2937"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.4, 6.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(30, 630)
ax.axis("off")


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    ab = AnnotationBbox(OffsetImage(mpimg.imread(path), zoom=zoom), xy, frameon=False,
                        zorder=9, box_alignment=box_alignment)
    ax.add_artist(ab)


def straight(p1, p2, color=GRAY, lw=2.6, ls="solid", z=4, mut=17):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=mut, linewidth=lw,
                                 color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2))


def node_box(x, y, w, h, fc="white", ec="#e5e7eb", lw=1.4):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=9",
                                 linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))


def title(cx, label):
    ax.text(cx, 566, label, ha="center", va="center", fontsize=15, fontweight="bold",
            color=TEXT_PRIMARY, zorder=6)


def req(cx, label):
    """機能要件の添字 (amber, center 揃え)。"""
    ax.text(cx, 442, label, ha="center", va="top", fontsize=12, fontweight="bold",
            color=AMBER, zorder=6)


def chip(cx, cy, glyph, color=BLUE):
    ax.add_patch(FancyBboxPatch((cx - 15, cy - 14), 30, 28,
                                 boxstyle="round,pad=0,rounding_size=6",
                                 facecolor="#eff6ff", edgecolor=color, linewidth=1.8, zorder=6))
    ax.text(cx, cy, glyph, ha="center", va="center", fontsize=15, fontweight="bold",
            color=color, zorder=7)


BOX_Y, BOX_H, BC = 460, 80, 500   # box 下端 / 高さ / 縦中心

# ===================================================================== ① 回路記述 (Rust / RISC Zero)
CX1, CW = 40, 306
ax.add_patch(FancyBboxPatch((CX1, BOX_Y - 8), CW, 96,
                             boxstyle="round,pad=0,rounding_size=8",
                             facecolor=CODE_BG, edgecolor="none", zorder=3))
code = [
    ("fn main() {", "#e5e7eb"),
    ("  let w = env::read();   // W", "#a7f3d0"),
    ("  assert!(exploit(w, C)); // break", "#fca5a5"),
    ("  commit(C.hash());", "#e5e7eb"),
    ("}", "#e5e7eb"),
]
for i, (line, col) in enumerate(code):
    ax.text(CX1 + 15, BOX_Y + 72 - i * 16, line, ha="left", va="center", fontsize=10.5,
            family="monospace", color=col, zorder=5)
CC1 = CX1 + CW / 2
title(CC1, "① 回路記述")
add_logo(f"{LOGO_DIR}/rust.png", (CX1 + CW - 20, 566), zoom=0.15)
req(CC1, "言語: Rust (RISC Zero guest)\n証明する命題: exploit(W, C) が成立")

# ===================================================================== ② zkVM 実行 (WitnessGen → Proving)
BX0, BX1 = 384, 800
ax.add_patch(FancyBboxPatch((BX0, BOX_Y - 12), BX1 - BX0, BOX_H + 24,
                             boxstyle="round,pad=0,rounding_size=10",
                             facecolor="#f0fdf4", edgecolor="#94a3b8", linewidth=1.5,
                             linestyle=(0, (6, 4)), zorder=1))
BCEN = (BX0 + BX1) / 2
title(BCEN, "② zkVM 実行")
add_logo(f"{LOGO_DIR}/risc0.png", (BCEN + 78, 566), zoom=0.085)

# --- Witness Generation ノード
WGX = 478
node_box(WGX - 78, BOX_Y, 156, BOX_H, fc="#ecfdf5", ec="#a7f3d0")
chip(WGX, BC + 18, "W", color=GREEN)
ax.text(WGX, BC - 12, "Witness", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(WGX, BC - 28, "Generation", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# --- Proving ノード
PVX = 706
node_box(PVX - 78, BOX_Y, 156, BOX_H, fc="#ecfdf5", ec="#a7f3d0")
chip(PVX, BC + 18, "π", color=BLUE)
ax.text(PVX, BC - 16, "Proving", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

straight((WGX + 78, BC), (PVX - 78, BC), mut=14)   # WitnessGen → Proving
req(BCEN, "同時・脆弱性発見時に実行\nクライアント上・マシン制約なし\n(時間はかかってよい)")
straight((CX1 + CW + 4, BC), (BX0 - 6, BC))         # 回路記述 → zkVM

# ===================================================================== ③ Groth16 wrap
GX0, GW = 838, 158
node_box(GX0, BOX_Y, GW, BOX_H, fc="white")
GCEN = GX0 + GW / 2
# 変換アイコン: 大きな STARK proof → 小さな SNARK (center 揃え, ラベル無し)
ax.add_patch(Rectangle((GCEN - 44, BC - 17), 34, 34, facecolor="#dbeafe",
                       edgecolor=BLUE, linewidth=2, zorder=6))
ax.text(GCEN - 27, BC, "π", ha="center", va="center", fontsize=15,
        fontweight="bold", color=BLUE, zorder=7)
straight((GCEN - 6, BC), (GCEN + 18, BC), color=BLUE, lw=2.2, mut=12)
ax.add_patch(Rectangle((GCEN + 22, BC - 10), 20, 20, facecolor="#dbeafe",
                       edgecolor=BLUE, linewidth=2, zorder=6))
ax.text(GCEN + 32, BC, "π", ha="center", va="center", fontsize=11,
        fontweight="bold", color=BLUE, zorder=7)
title(GCEN, "③ Groth16 wrap")
req(GCEN, "STARK → Groth16 に変換\nVerification Cost 一定")
straight((BX1 + 6, BC), (GX0 - 6, BC))              # zkVM → Groth16

# ===================================================================== ④ on-chain Verify
VX = 1118
add_logo(f"{LOGO_DIR}/ethereum.png", (VX, BC), zoom=0.14)
title(VX, "④ on-chain Verify")
straight((GX0 + GW + 6, BC), (VX - 30, BC))         # Groth16 → Verify

# ===================================================================== ⑤ 分岐 (報酬 + 復号鍵)
COL_Y = 350
BR_C = 185         # 報酬 / 復号鍵ノードの縦中心
# Verify から下へ (要件添字が無い列なので直下に降ろせる)
ax.plot([VX, VX], [BC - 30, COL_Y], color=GREEN, linewidth=2.4, zorder=4)
ax.add_patch(Circle((VX, COL_Y), 5, facecolor=GREEN, edgecolor="none", zorder=5))
ax.text(VX, 410, "verify(π) が通れば\n脆弱性の存在が確定", ha="center", va="center",
        fontsize=12, fontweight="bold", color=GREEN, zorder=6,
        bbox=dict(facecolor="white", edgecolor="none", pad=1))
# コレクタ + 2 枝
ax.plot([300, VX], [COL_Y, COL_Y], color=GREEN, linewidth=2.4, zorder=4)
straight((300, COL_Y), (300, BR_C + 40), color=GREEN, lw=2.4, mut=14)
straight((780, COL_Y), (780, BR_C + 43), color=GREEN, lw=2.4, mut=14)

# --- 報酬ノード (center 揃え)
node_box(165, BR_C - 40, 270, 80, fc="#ecfdf5", ec="#a7f3d0")
ax.add_patch(Circle((300, BR_C + 18), 15, facecolor="#fbbf24", edgecolor="#d97706",
                    linewidth=2, zorder=6))
ax.text(300, BR_C + 18, "¥", ha="center", va="center", fontsize=15, fontweight="bold",
        color="white", zorder=7)
ax.text(300, BR_C - 18, "報酬が自動で支払われる", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# --- 復号鍵ノード (center 揃え)
node_box(610, BR_C - 44, 340, 88, fc="#ecfdf5", ec="#a7f3d0")
# 鍵アイコン
ax.add_patch(Circle((780, BR_C + 24), 9, facecolor="none", edgecolor=GREEN, linewidth=2.4, zorder=6))
ax.plot([780, 780], [BR_C + 15, BR_C + 4], color=GREEN, linewidth=2.4, zorder=6)
ax.plot([780, 788], [BR_C + 8, BR_C + 8], color=GREEN, linewidth=2.4, zorder=6)
ax.text(780, BR_C - 8, "復号鍵がプロバイダに渡る", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(780, BR_C - 30, "→ 脆弱性を確認して修正できる", ha="center", va="center",
        fontsize=12, fontweight="bold", color=TEXT_MUTED, zorder=6)

# 見出し
ax.text(40, 610, "パターン A の具体構成 — RISC Zero (Rust) で「脆弱性の存在」を ZK 証明する",
        ha="left", va="center", fontsize=16, fontweight="bold", color=TEXT_PRIMARY, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
