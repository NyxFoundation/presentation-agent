# req_map_arch.py — KelpDAO アーキに対する 3 パターンの防御差分マップ (SL25b)
#
# 生成: uv run --with matplotlib python3 figures/req_map_arch.py
# 出力: public/images/req_map_arch.png
#
# 設計語彙は figures/kelp_arch.py / poe_arch.py に従う:
#   基底 (下段) = p5 の KelpDAO 事件アーキの簡約版 (User → Karak → DVN #1 → release())。
#   green = 追加する防御。上段に パターン A / B / C の監査モジュールを並べ、
#   「誰が」「何を計算する」だけが違い、どれも同じ on-chain Verifier + Circuit-Breaker に
#   証明を届ける — 差分として読める図。

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
OUT = "/home/gohan/workspace/presentation-agent/public/images/req_map_arch.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST_EDGE = "#94a3b8"
RED = "#dc2626"
AMBER = "#d97706"
GREEN = "#059669"
GREEN_FC = "#ecfdf5"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.4, 6.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(40, 640)
ax.axis("off")

# ---------------------------------------------------------------- icons
def icon_person(cx, cy, s=20, color=GRAY):
    ax.add_patch(Circle((cx, cy + s * 0.5), s * 0.34, facecolor=color, edgecolor="none", zorder=8))
    body = Polygon([(cx - s * 0.52, cy - s * 0.55), (cx, cy - s * 0.18), (cx + s * 0.52, cy - s * 0.55),
                     (cx + 0.42 * s, cy - s * 0.9), (cx - 0.42 * s, cy - s * 0.9)],
                    closed=True, facecolor=color, edgecolor="none", zorder=8)
    ax.add_patch(body)


def icon_shield(cx, cy, s=20, color=GRAY):
    w, h = s * 1.15, s * 1.35
    pts = [(cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2), (cx + w / 2, cy),
           (cx, cy - h / 2), (cx - w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=color,
                          linewidth=1.8, zorder=8))
    ax.plot([cx - s * 0.3, cx - s * 0.06, cx + s * 0.32],
            [cy + s * 0.02, cy - s * 0.22, cy + s * 0.26],
            color="white", linewidth=2.4, solid_capstyle="round",
            solid_joinstyle="round", zorder=9)


def icon_magnifier(cx, cy, s=20, color=GREEN):
    ax.add_patch(Circle((cx - s * 0.15, cy + s * 0.15), s * 0.5, facecolor="none",
                        edgecolor=color, linewidth=2.6, zorder=8))
    ax.plot([cx + s * 0.22, cx + s * 0.62], [cy - s * 0.22, cy - s * 0.62],
            color=color, linewidth=2.8, solid_capstyle="round", zorder=8)


def icon_chip(cx, cy, s=20, color=GREEN):
    """LLM チップ。"""
    w = s * 1.3
    ax.add_patch(Rectangle((cx - w / 2, cy - w / 2), w, w, facecolor="white",
                            edgecolor=color, linewidth=2.2, zorder=8))
    ax.text(cx, cy, "AI", ha="center", va="center", fontsize=11, fontweight="bold",
            color=color, zorder=9)
    for d in (-0.3, 0, 0.3):
        ax.plot([cx + d * s, cx + d * s], [cy + w / 2, cy + w / 2 + s * 0.28],
                color=color, linewidth=1.8, zorder=8)
        ax.plot([cx + d * s, cx + d * s], [cy - w / 2 - s * 0.28, cy - w / 2],
                color=color, linewidth=1.8, zorder=8)


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    ab = AnnotationBbox(OffsetImage(img, zoom=zoom), xy, frameon=False, zorder=9,
                        box_alignment=box_alignment)
    ax.add_artist(ab)


def straight(p1, p2, color=GRAY, lw=2.4, ls="solid", z=4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=16, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


def elbow(points, color=GREEN, lw=2.2, ls=(0, (4, 2.5)), z=4):
    for i in range(len(points) - 2):
        ax.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]],
                color=color, linewidth=lw, linestyle=ls, zorder=z)
    a = FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>", mutation_scale=13,
                         linewidth=lw, color=color, linestyle=ls, zorder=z,
                         shrinkA=0, shrinkB=2)
    ax.add_patch(a)


# ================================================================ 基底 (下段): KelpDAO 簡約版
MAIN_Y = 120
X_USER, X_KARAK, X_DVN, X_VER, X_ETH = 90, 300, 540, 810, 1110

icon_person(X_USER, MAIN_Y)
ax.text(X_USER, MAIN_Y - 34, "User", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=12)
straight((X_USER + 34, MAIN_Y), (X_KARAK - 46, MAIN_Y), lw=2.2)
add_logo(f"{LOGO_DIR}/karak.png", (X_KARAK, MAIN_Y), zoom=0.11)
ax.text(X_KARAK, MAIN_Y - 34, "Karak L2 Contract", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=12)
straight((X_KARAK + 46, MAIN_Y), (X_DVN - 40, MAIN_Y), lw=2.2)
icon_shield(X_DVN, MAIN_Y, s=21, color=AMBER)
ax.text(X_DVN, MAIN_Y - 34, "DVN #1 (1-of-1)", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=12)

# release() 要求は green Verifier で止まる (p7 と同じ読み方)
straight((X_DVN + 38, MAIN_Y), (X_VER - 42, MAIN_Y), color=RED, lw=2.6)
ax.text((X_DVN + X_VER) / 2, MAIN_Y + 18, "release() 要求", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=RED, zorder=6)

icon_shield(X_VER, MAIN_Y, s=23, color=GREEN)
ax.text(X_VER, MAIN_Y - 36, "Verifier + Circuit-Breaker", ha="center", va="center",
        fontsize=14, fontweight="bold", color=GREEN, zorder=12)
# 遮断 = Ethereum への線は無い (線の不在)
add_logo(f"{LOGO_DIR}/ethereum.png", (X_ETH, MAIN_Y), zoom=0.11)
ax.text(X_ETH, MAIN_Y - 34, "Ethereum Contract", ha="center", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, zorder=12)
ax.text(X_ETH, MAIN_Y + 32, "流出 0", ha="center", va="center", fontsize=14,
        fontweight="bold", color=GREEN, zorder=12)

# ================================================================ 上段: 3 パターンの監査モジュール (差分)
BOX_Y, BOX_H, BOX_W = 300, 240, 360
XS = [30, 450, 870]
HEAD = [("パターン A — ZK 証明", "A"), ("パターン B — MPC", "B"), ("パターン C — ZK + LLM (zkML)", "C")]

def module(x, head):
    ax.add_patch(FancyBboxPatch((x, BOX_Y), BOX_W, BOX_H,
                                 boxstyle="round,pad=0,rounding_size=10",
                                 linewidth=1.6, edgecolor=GREEN, facecolor=GREEN_FC,
                                 alpha=1.0, linestyle=(0, (6, 4)), zorder=1))
    ax.text(x + 18, BOX_Y + BOX_H - 26, head, ha="left", va="center", fontsize=15,
            fontweight="bold", color=GREEN, zorder=6)

for (head, _), x in zip(HEAD, XS):
    module(x, head)

def lines(x, l1, l2, l3):
    ax.text(x + 18, BOX_Y + 176, l1, ha="left", va="center", fontsize=13.5,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    ax.text(x + 18, BOX_Y + 136, l2, ha="left", va="center", fontsize=13.5,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    ax.text(x + 18, BOX_Y + 58, l3, ha="left", va="center", fontsize=12.5,
            fontweight="bold", color=GREEN, zorder=6)

# --- パターン A: 単独の AI Auditor が ZK 証明
x = XS[0]
icon_magnifier(x + 315, BOX_Y + 150, s=20)
lines(x, "誰が: 単独の AI Auditor", "計算: 「W で壊れる」を実行", "出力: ZK 証明 π — W は秘匿")

# --- パターン B: 複数の監査ノードが MPC 合議
x = XS[1]
for dx, dy in [(-24, 14), (24, 14), (0, -20)]:
    icon_shield(x + 315 + dx, BOX_Y + 150 + dy, s=11, color=GREEN)
for a, b in [((-24, 14), (24, 14)), ((-24, 14), (0, -20)), ((24, 14), (0, -20))]:
    ax.plot([x + 315 + a[0], x + 315 + b[0]], [BOX_Y + 150 + a[1], BOX_Y + 150 + b[1]],
            color=GREEN, linewidth=1.3, linestyle=(0, (2, 2)), zorder=5)
lines(x, "誰が: 複数の監査ノード", "計算: 合議で判定 (基準は秘匿)", "出力: threshold 署名つき判定")

# --- パターン C: LLM が判定 + 推論の検証
x = XS[2]
icon_chip(x + 315, BOX_Y + 150, s=18)
lines(x, "誰が: LLM エージェント", "計算: 判定 + 推論の検証", "出力: zkML 証明 — モデルも検証済")

# ================================================================ モジュール → Verifier への合流
COLLECT_Y = 232
for x in XS:
    elbow([(x + BOX_W / 2, BOX_Y - 2), (x + BOX_W / 2, COLLECT_Y), (X_VER, COLLECT_Y),
           (X_VER, MAIN_Y + 26)])
ax.add_patch(Circle((X_VER, COLLECT_Y), 5, facecolor=GREEN, edgecolor="none", zorder=5))
ax.text(330, COLLECT_Y - 22, "どのパターンでも、届くのは「検証できる証明」",
        ha="center", va="center", fontsize=13, fontweight="bold", color=GREEN, zorder=6)

# 上段の見出し
ax.text(30, 610, "差分 (green): 監査モジュールの「誰が」「何を計算する」を変えると、使う暗号が変わる",
        ha="left", va="center", fontsize=15, fontweight="bold", color=TEXT_PRIMARY, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
