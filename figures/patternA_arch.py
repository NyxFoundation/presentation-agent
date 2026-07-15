# patternA_arch.py — パターン A (RISC Zero / Rust) の具体システム構成 (SL25c)
#
# 生成: uv run --with matplotlib python3 figures/patternA_arch.py
# 出力: public/images/patternA_arch.png
#
# 設計語彙は figures/kelp_arch.py / req_map_arch.py に従う:
#   左→右の pipeline。各ノードは実コード / ロゴ / アイコンで見せ、
#   機能要件 (どの言語・いつ WitnessGen/Prove/Verify するか・マシン制約) を
#   各ノードの下に添字する。Verify 通過後は 報酬支払い + 復号鍵 → プロバイダ修正 に分岐。

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


def req(x, y, label):
    """機能要件の添字 (amber)。"""
    ax.text(x, y, label, ha="center", va="top", fontsize=12, fontweight="bold",
            color=AMBER, zorder=6)


MAIN_Y = 430
# ===================================================================== ① 回路記述 (Rust / RISC Zero)
CX1, CW = 60, 340
ax.add_patch(FancyBboxPatch((CX1, MAIN_Y - 5), CW, 118,
                             boxstyle="round,pad=0,rounding_size=8",
                             facecolor=CODE_BG, edgecolor="none", zorder=3))
code = [
    ("#[no_mangle]", "#7dd3fc"),
    ("fn main() {", "#e5e7eb"),
    ("  let w = env::read();      // W", "#a7f3d0"),
    ("  assert!(exploit(w, C));   // break?", "#fca5a5"),
    ("  env::commit(&C.hash());", "#e5e7eb"),
    ("}", "#e5e7eb"),
]
for i, (line, col) in enumerate(code):
    ax.text(CX1 + 16, MAIN_Y + 96 - i * 17, line, ha="left", va="center", fontsize=11.5,
            family="monospace", color=col, zorder=5)
add_logo(f"{LOGO_DIR}/rust.png", (CX1 + CW - 52, MAIN_Y + 138), zoom=0.16)
add_logo(f"{LOGO_DIR}/risc0.png", (CX1 + CW - 20, MAIN_Y + 138), zoom=0.085)
ax.text(CX1 + 4, MAIN_Y + 138, "① 回路記述", ha="left", va="center", fontsize=15,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
req(CX1 + CW / 2, MAIN_Y - 18, "言語: Rust (RISC Zero guest)\n証明する命題: exploit(W, C) が成立")

# ===================================================================== ② Witness Gen + Proving
CX2 = 470
node_box(CX2, MAIN_Y + 6, 230, 100, fc="#ecfdf5", ec="#a7f3d0")
add_logo(f"{LOGO_DIR}/risc0.png", (CX2 + 40, MAIN_Y + 62), zoom=0.12)
ax.text(CX2 + 78, MAIN_Y + 74, "Witness Gen", ha="left", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(CX2 + 78, MAIN_Y + 50, "+ Proving", ha="left", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(CX2 + 115, MAIN_Y + 130, "② zkVM 実行", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
req(CX2 + 115, MAIN_Y - 18, "同時・脆弱性発見時に実行\nクライアント上・マシン制約なし\n(時間はかかってよい)")
straight((CX1 + CW + 6, MAIN_Y + 55), (CX2 - 8, MAIN_Y + 55))

# ===================================================================== ③ Groth16 wrap
CX3 = 770
node_box(CX3, MAIN_Y + 6, 190, 100, fc="white")
# 変換アイコン: STARK proof → 小さな SNARK
ax.add_patch(Rectangle((CX3 + 30, MAIN_Y + 40), 34, 34, facecolor="#dbeafe",
                       edgecolor=BLUE, linewidth=2, zorder=6))
ax.text(CX3 + 47, MAIN_Y + 57, "π", ha="center", va="center", fontsize=15,
        fontweight="bold", color=BLUE, zorder=7)
straight((CX3 + 70, MAIN_Y + 57), (CX3 + 96, MAIN_Y + 57), color=BLUE, lw=2.2, mut=13)
ax.add_patch(Rectangle((CX3 + 100, MAIN_Y + 47), 20, 20, facecolor="#dbeafe",
                       edgecolor=BLUE, linewidth=2, zorder=6))
ax.text(CX3 + 138, MAIN_Y + 57, "小さく", ha="left", va="center", fontsize=13,
        fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(CX3 + 95, MAIN_Y + 130, "③ Groth16 wrap", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
req(CX3 + 95, MAIN_Y - 18, "STARK → Groth16 に変換\nVerification Cost 一定")
straight((CX2 + 230 + 6, MAIN_Y + 55), (CX3 - 8, MAIN_Y + 55))

# ===================================================================== ④ on-chain Verify
CX4 = 1050
add_logo(f"{LOGO_DIR}/ethereum.png", (CX4 + 55, MAIN_Y + 56), zoom=0.14)
ax.text(CX4 + 55, MAIN_Y + 130, "④ on-chain Verify", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
req(CX4 + 55, MAIN_Y - 18, "コントラクトが verify(π)\n通れば脆弱性の存在が確定")
straight((CX3 + 190 + 6, MAIN_Y + 55), (CX4 + 20, MAIN_Y + 55))

# ===================================================================== ⑤ 分岐 (報酬 + 復号鍵)
BR_Y = 150
COL_Y = 300   # 要件添字の下を通す水平コレクタ
ax.plot([CX4 + 55, CX4 + 55], [MAIN_Y + 8, COL_Y], color=GREEN, linewidth=2.4, zorder=4)
ax.text(CX4 + 55, COL_Y + 14, "verify 通過", ha="center", va="center", fontsize=12.5,
        fontweight="bold", color=GREEN, zorder=6,
        bbox=dict(facecolor="white", edgecolor="none", pad=1))
ax.add_patch(Circle((CX4 + 55, COL_Y), 5, facecolor=GREEN, edgecolor="none", zorder=5))
# 左枝: 報酬支払い / 右枝: 復号鍵
ax.plot([300, CX4 + 55], [COL_Y, COL_Y], color=GREEN, linewidth=2.4, zorder=4)
straight((300, COL_Y), (300, BR_Y + 58), color=GREEN, lw=2.4, mut=14)
straight((760, COL_Y), (760, BR_Y + 58), color=GREEN, lw=2.4, mut=14)

# 報酬ノード
node_box(180, BR_Y - 8, 240, 66, fc="#ecfdf5", ec="#a7f3d0")
ax.add_patch(Circle((222, BR_Y + 25), 15, facecolor="#fbbf24", edgecolor="#d97706",
                    linewidth=2, zorder=6))
ax.text(222, BR_Y + 25, "¥", ha="center", va="center", fontsize=15, fontweight="bold",
        color="white", zorder=7)
ax.text(250, BR_Y + 25, "報酬が自動で支払われる", ha="left", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)

# 復号鍵 → プロバイダ修正ノード
node_box(560, BR_Y - 8, 400, 66, fc="#ecfdf5", ec="#a7f3d0")
# 鍵アイコン
ax.add_patch(Circle((602, BR_Y + 30), 10, facecolor="none", edgecolor=GREEN, linewidth=2.4, zorder=6))
ax.plot([602, 602], [BR_Y + 20, BR_Y + 8], color=GREEN, linewidth=2.4, zorder=6)
ax.plot([602, 610], [BR_Y + 12, BR_Y + 12], color=GREEN, linewidth=2.4, zorder=6)
ax.text(624, BR_Y + 30, "復号鍵がプロバイダに渡る", ha="left", va="center", fontsize=13.5,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(624, BR_Y + 8, "→ 脆弱性の内容を確認して修正できる", ha="left", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)

# 見出し
ax.text(60, 600, "パターン A の具体構成 — RISC Zero (Rust) で「脆弱性の存在」を ZK 証明する",
        ha="left", va="center", fontsize=16, fontweight="bold", color=TEXT_PRIMARY, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
