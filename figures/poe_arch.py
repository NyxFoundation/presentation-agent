# poe_arch.py — Proof-of-Exploit を KelpDAO 図 (kelp_arch.py) への「差分」として描く静的アーキ図 (SL09)
#
# 生成: uv run --with matplotlib python3 figures/poe_arch.py
# 出力: public/images/poe_arch_static.png
#
# 設計: p4 (SL08b, kelp_arch.py) と同じ actor 配置・同じ設計語彙の上に、
# 追加された防御要素 (AI Auditor / ZK Prover / ZK Verifier / Circuit-Breaker) だけを
# 緑 (#059669) で重ねる。緑は kelp_arch に存在しない色なので「何が追加されたか」が
# 色だけで浮き上がる。基底部 (User / Karak / LayerZero バンド / DVN / RPC 汚染 / callout)
# は kelp_arch.py の座標・色をそのまま流用する。
#
# 設計語彙は .claude/skills/arch-diagram/SKILL.md に従う:
#   枠なし (アイコン+ラベルのみ) / 直角配線 / ゴースト破線=不在 /
#   赤=攻撃・改ざん (被害者は中立色) / 緑=追加された防御要素 / ラベルは白 bbox で線上に座る

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.patches import (FancyArrowPatch, FancyBboxPatch, Circle,
                                Rectangle, Polygon, Arc)
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"
OUT = "/home/gohan/workspace/presentation-agent/public/images/poe_arch_static.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST_EDGE = "#94a3b8"
GHOST_TEXT = "#64748b"
RED = "#dc2626"
AMBER = "#d97706"
GREEN = "#059669"          # 追加された防御要素 (kelp_arch に無い色 = 差分)
GREEN_DARK = "#065f46"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.4, 6.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(85, 578)
ax.axis("off")

# ---------------------------------------------------------------- icon library
def icon_person(cx, cy, s=22, color=GRAY):
    ax.add_patch(Circle((cx, cy + s * 0.5), s * 0.34, facecolor=color, edgecolor="none", zorder=8))
    body = Polygon([(cx - s * 0.52, cy - s * 0.55), (cx, cy - s * 0.18), (cx + s * 0.52, cy - s * 0.55),
                     (cx + 0.42 * s, cy - s * 0.9), (cx - 0.42 * s, cy - s * 0.9)],
                    closed=True, facecolor=color, edgecolor="none", zorder=8)
    ax.add_patch(body)


def icon_mini_server(cx, cy, s=22, color=GRAY, ghost=False):
    w, h = s * 1.05, s * 1.3
    if ghost:
        ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, facecolor="none",
                                edgecolor=color, linewidth=1.8, linestyle=(0, (3, 2)), zorder=8))
        for dy in (0.28, -0.06, -0.4):
            ax.add_patch(Rectangle((cx - w * 0.32, cy + dy * h - 0.035 * h), w * 0.64, 0.07 * h,
                                    facecolor="none", edgecolor=color, linewidth=1.2, zorder=8))
    else:
        ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, facecolor=color,
                                edgecolor=color, linewidth=1.8, zorder=8))
        for dy in (0.28, -0.06, -0.4):
            ax.add_patch(Rectangle((cx - w * 0.32, cy + dy * h - 0.035 * h), w * 0.64, 0.07 * h,
                                    facecolor="white", edgecolor="none", zorder=9))


def icon_shield(cx, cy, s=22, color=GRAY, ghost=False):
    """検証者 (DVN / ZK Verifier)。形=役割: 検証者はすべてシールド。"""
    w, h = s * 1.15, s * 1.35
    pts = [(cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2), (cx + w / 2, cy),
           (cx, cy - h / 2), (cx - w / 2, cy)]
    if ghost:
        ax.add_patch(Polygon(pts, closed=True, facecolor="none", edgecolor=color,
                              linewidth=1.8, linestyle=(0, (3, 2)), zorder=8))
        check_color, check_lw = color, 1.8
    else:
        ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=color,
                              linewidth=1.8, zorder=8))
        check_color, check_lw = "white", 2.6
    ax.plot([cx - s * 0.3, cx - s * 0.06, cx + s * 0.32],
            [cy + s * 0.02, cy - s * 0.22, cy + s * 0.26],
            color=check_color, linewidth=check_lw, solid_capstyle="round",
            solid_joinstyle="round", zorder=9)


def icon_magnifier(cx, cy, s=22, color=GREEN):
    """AI Auditor (監査エージェント)。"""
    r = s * 0.36
    ax.add_patch(Circle((cx - s * 0.08, cy + s * 0.14), r, facecolor="none",
                         edgecolor=color, linewidth=3.0, zorder=8))
    ax.plot([cx - s * 0.08 + r * 0.72, cx + s * 0.5], [cy + s * 0.14 - r * 0.72, cy - s * 0.48],
            color=color, linewidth=3.4, zorder=8, solid_capstyle="round")


def icon_pi(cx, cy, s=22, color=GREEN):
    """ZK Prover (証明 π の生成者)。"""
    ax.plot([cx - s * 0.5, cx + s * 0.5], [cy + s * 0.34, cy + s * 0.34],
            color=color, linewidth=3.2, zorder=8, solid_capstyle="round")
    ax.plot([cx - s * 0.26, cx - s * 0.3], [cy + s * 0.34, cy - s * 0.44],
            color=color, linewidth=3.2, zorder=8, solid_capstyle="round")
    ax.plot([cx + s * 0.3, cx + s * 0.34], [cy + s * 0.34, cy - s * 0.44],
            color=color, linewidth=3.2, zorder=8, solid_capstyle="round")


def icon_breaker(cx, cy, s=22, color=GREEN):
    """Circuit-Breaker (電源記号)。"""
    ax.add_patch(Arc((cx, cy - s * 0.06), s * 1.0, s * 1.0, angle=0, theta1=35, theta2=325,
                      color=color, linewidth=3.0, zorder=8))
    ax.plot([cx, cx], [cy + s * 0.12, cy + s * 0.58], color=color, linewidth=3.0,
            zorder=8, solid_capstyle="round")


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, zorder=9, box_alignment=box_alignment)
    ax.add_artist(ab)


# ---------------------------------------------------------------- primitives
def entity(cx, cy, icon_fn, label, sub=None, color=TEXT_PRIMARY, sub_color=None,
           fontsize=15, subfontsize=13.5, gap=36, subgap=19, on_line=False,
           on_line_fc="white", label_above=False):
    """浮遊アイコン+ラベル (枠なし)。label_above=True はラベルをアイコンの上に置く
    (上段の off-chain actor 用 — 下を通る配線とラベルが衝突しないように)。"""
    icon_fn(cx, cy)
    bbox = dict(facecolor=on_line_fc, edgecolor="none", pad=2.5) if on_line else None
    ly = cy + gap if label_above else cy - gap
    ax.text(cx, ly, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=color, zorder=12, bbox=bbox)
    if sub:
        sy = ly + subgap if label_above else ly - subgap
        ax.text(cx, sy, sub, ha="center", va="center", fontsize=subfontsize,
                fontweight="bold", color=(sub_color or color), zorder=12, bbox=bbox)


def straight(p1, p2, color=GRAY, lw=2.4, ls="solid", z=4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=17, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


def elbow_path(points, color=GRAY, lw=2.4, ls="solid", z=4, mutation_scale=14):
    for i in range(len(points) - 2):
        ax.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]],
                color=color, linewidth=lw, linestyle=ls, zorder=z)
    a = FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>", mutation_scale=mutation_scale,
                         linewidth=lw, color=color, linestyle=ls, zorder=z, shrinkA=0, shrinkB=2)
    ax.add_patch(a)


# ===================================================================== 座標定数
# 基底部は kelp_arch.py と同一。追加要素のために Ethereum Contract のみ右へ寄せる
MAIN_Y = 420          # メインフロー行
DVN_X = 580           # DVN #1 中心 (callout leader / trunk と共有)
COLLECT_Y = 330       # 改ざん RPC の応答が合流するコレクタ
VER_X = 845           # ZK Verifier (追加) — LayerZero バンドの外
BRK_X = 1000          # Circuit-Breaker (追加)
ETH_X = 1175          # Ethereum Contract (kelp_arch では 950。ガード挿入のため右へ)
TOP_Y = 525           # off-chain 追加 actor 行 (AI Auditor / ZK Prover)
PROVER_X = 1080

# ===================================================================== 基底部 (kelp_arch と同一)
entity(110, MAIN_Y, lambda cx, cy: icon_person(cx, cy, s=22), "User")
straight((150, MAIN_Y), (266, MAIN_Y), lw=2.4)
ax.text(208, MAIN_Y + 17, "burns rsETH", ha="center", va="center", fontsize=13,
        color=TEXT_MUTED, fontweight="bold", zorder=6)
entity(320, MAIN_Y, lambda cx, cy: add_logo(f"{LOGO_DIR}/karak.png", (cx, cy), zoom=0.13),
       "Karak L2 Contract", fontsize=15)

# LayerZero バンド + DVN 群 (kelp_arch と同一)
ax.add_patch(FancyBboxPatch((365, 226), 447, 230,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor="#6366f1", alpha=0.05, linestyle=(0, (6, 4)),
                             zorder=1))
ax.add_patch(FancyBboxPatch((365, 226), 447, 230,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor="none", linestyle=(0, (6, 4)), zorder=1))
add_logo(f"{LOGO_DIR}/layerzero.png", (388, 440), zoom=0.065)
ax.text(404, 440, "LayerZero", ha="left", va="center", fontsize=13,
        fontweight="bold", color=GRAY, zorder=2)

straight((362, MAIN_Y), (552, MAIN_Y), lw=2.4)
entity(DVN_X, MAIN_Y, lambda cx, cy: icon_shield(cx, cy, s=24, color=AMBER),
       "DVN #1", "active・signs (1-of-1)", color=TEXT_PRIMARY, sub_color=AMBER,
       gap=37, subgap=21, on_line=True, on_line_fc="#f7f7fe")
entity(430, 290, lambda cx, cy: icon_shield(cx, cy, s=20, color=GHOST_EDGE, ghost=True),
       "DVN #2", "未参加", color=GHOST_TEXT, gap=30, subgap=18, fontsize=13.5, subfontsize=12.5)
entity(740, 290, lambda cx, cy: icon_shield(cx, cy, s=20, color=GHOST_EDGE, ghost=True),
       "DVN #3", "未参加", color=GHOST_TEXT, gap=30, subgap=18, fontsize=13.5, subfontsize=12.5)

# config callout (kelp_arch と同一) — 脆弱性はまだそこにある。これが witness W になる
CALLOUT_Y = 530
ax.text(DVN_X - 21, CALLOUT_Y, "setConfig( requiredDVNCount:", ha="right", va="center",
        fontsize=14, fontweight="bold", color=TEXT_PRIMARY, family="monospace", zorder=11)
ax.add_patch(FancyBboxPatch((DVN_X - 15, CALLOUT_Y - 14), 30, 28,
                             boxstyle="round,pad=0,rounding_size=5",
                             linewidth=1.5, edgecolor=RED, facecolor="none", zorder=11))
ax.text(DVN_X, CALLOUT_Y, "1", ha="center", va="center", fontsize=16,
        fontweight="bold", color=RED, zorder=12)
ax.text(DVN_X + 21, CALLOUT_Y, ")", ha="left", va="center", fontsize=14,
        fontweight="bold", color=TEXT_PRIMARY, family="monospace", zorder=11)
straight((DVN_X, CALLOUT_Y - 16), (DVN_X, MAIN_Y + 18), color=RED, lw=2.0, ls=(0, (3, 2)), z=5)

# Karak RPC 群 (kelp_arch と同一)
rpc = [
    (290, 148, "Karak RPC #3", "オフライン", "offline"),
    (500, 168, "Karak RPC #1", "改ざん済み", "compromised"),
    (660, 148, "Karak RPC #2", "改ざん済み", "compromised"),
    (820, 165, "Karak RPC #4", "オフライン", "offline"),
    (970, 145, "Karak RPC #5", "オフライン", "offline"),
]
for x, y, label, sub, style in rpc:
    if style == "compromised":
        entity(x, y, lambda cx, cy: icon_mini_server(cx, cy, s=21, color=RED), label, sub,
               color=RED, sub_color=RED, fontsize=14, subfontsize=13, gap=31, subgap=18)
    else:
        entity(x, y, lambda cx, cy: icon_mini_server(cx, cy, s=21, color=GHOST_EDGE, ghost=True),
               label, sub, color=GHOST_TEXT, sub_color=GHOST_TEXT,
               fontsize=14, subfontsize=13, gap=31, subgap=18)

feed_ls = (0, (4, 2.5))
ax.plot([500, 500], [185, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.plot([660, 660], [165, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.plot([500, 660], [COLLECT_Y, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.add_patch(Circle((DVN_X, COLLECT_Y), 5, facecolor=RED, edgecolor="none", zorder=5))
straight((DVN_X, COLLECT_Y), (DVN_X, MAIN_Y - 18), color=RED, lw=2.4, ls=feed_ls, z=4)
ax.text(DVN_X, COLLECT_Y - 16, "偽の応答", ha="center", va="center", fontsize=13,
        fontweight="bold", color=RED, zorder=6)

# ===================================================================== 差分: 攻撃は Verifier で止まる
# kelp_arch では DVN → Ethereum に赤矢印「release() 実行」が貫通していた。
# ここでは同じ赤矢印が追加ガード (ZK Verifier) の左辺で止まる = 図の中心的な差分
straight((598, MAIN_Y), (822, MAIN_Y), color=RED, lw=2.8)
ax.text(710, MAIN_Y + 17, "release() 要求", ha="center", va="center", fontsize=13.5,
        color=RED, fontweight="bold", zorder=6)

entity(VER_X, MAIN_Y, lambda cx, cy: icon_shield(cx, cy, s=24, color=GREEN),
       "ZK Verifier", "π 受理 ✓", color=TEXT_PRIMARY, sub_color=GREEN,
       gap=37, subgap=21)
straight((VER_X + 18, MAIN_Y), (BRK_X - 22, MAIN_Y), color=GREEN, lw=2.6)
ax.text(922, MAIN_Y + 17, "発火", ha="center", va="center", fontsize=13.5,
        color=GREEN, fontweight="bold", zorder=6)
entity(BRK_X, MAIN_Y, lambda cx, cy: icon_breaker(cx, cy, s=22, color=GREEN),
       "Circuit-Breaker", "release() を遮断", color=TEXT_PRIMARY, sub_color=GREEN,
       gap=37, subgap=21)

# Circuit-Breaker → Ethereum Contract の線は引かない (線の不在 = release() は届かない)
entity(ETH_X, MAIN_Y, lambda cx, cy: add_logo(f"{LOGO_DIR}/ethereum.png", (cx, cy), zoom=0.13),
       "Ethereum Contract", color=TEXT_PRIMARY, fontsize=15, gap=36)
ax.text(ETH_X, MAIN_Y - 60, "流出 0", ha="center", va="center",
        fontsize=15, fontweight="bold", color=GREEN, zorder=6)

# ===================================================================== 差分: off-chain の監査ループ
# AI Auditor が config の欠陥 (= callout の赤い「1」) を witness W として発見し、
# ZK Prover が π を生成、on-chain の ZK Verifier に submit する
entity(845, TOP_Y, lambda cx, cy: icon_magnifier(cx, cy, s=22), "AI Auditor",
       gap=33, label_above=True)
entity(PROVER_X, TOP_Y, lambda cx, cy: icon_pi(cx, cy, s=22), "ZK Prover",
       gap=33, label_above=True)

# AI Auditor → callout (config を監査して W を発見)
straight((797, CALLOUT_Y), (628, CALLOUT_Y), color=GREEN, lw=2.2, ls=(0, (4, 2.5)))
ax.text(712, CALLOUT_Y - 18, "config を監査 — W を発見", ha="center", va="center",
        fontsize=13, fontweight="bold", color=GREEN, zorder=6)

# AI Auditor → ZK Prover (W を渡す)
straight((893, TOP_Y), (1032, TOP_Y), color=GREEN, lw=2.2)
ax.text(962, TOP_Y + 16, "W (witness)", ha="center", va="center", fontsize=13,
        fontweight="bold", color=GREEN, zorder=6)

# ZK Prover → ZK Verifier (π を on-chain に submit)。直角エルボー、ラベルは白 bbox で線上
elbow_path([(PROVER_X, TOP_Y - 20), (PROVER_X, 478), (VER_X, 478), (VER_X, MAIN_Y + 22)],
           color=GREEN, lw=2.4, ls=(0, (4, 2.5)))
ax.text(963, 478, "π = Prove(∃W : exploit)", ha="center", va="center", fontsize=13,
        fontweight="bold", color=GREEN, zorder=6,
        bbox=dict(facecolor="white", edgecolor="none", pad=2.5))

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
