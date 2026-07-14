# proof_meanings.py — 「証明」の 3 つの意味を 1 枚で比較する静的図 (SL12)
#
# 生成: uv run --with matplotlib python3 figures/proof_meanings.py
# 出力: public/images/proof_meanings_static.png
#
# 設計語彙は .claude/skills/arch-diagram/SKILL.md に従う:
#   枠なし (アイコン+ラベルのみ) / 直角配線 / ゴースト破線=不在 (①の敵対者) /
#   赤=敵対者専用 / amber=主題 (③ 計算論的 = 2026 年の社会実装) /
#   境界バンド=③ を「我々が立つ場所」として囲う / ラベルは白 bbox で線上に座る
#
# 3 列とも同じ行構造 (ヘッダ → 証明の実体 → 敵対者 → 例) なので、
# 列を横に読めば各概念、行を横断すれば違い (敵対者の計算能力と仮定の有無) が読める。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import (FancyArrowPatch, FancyBboxPatch, Circle,
                                Rectangle, Polygon)

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/proof_meanings_static.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST_EDGE = "#94a3b8"
GHOST_TEXT = "#64748b"
RED = "#dc2626"
AMBER = "#d97706"
AMBER_BAND_FC = "#fdfaf2"   # amber #d97706 α.05 on white の合成色 (バンド上の on_line 用)
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
GREEN = "#059669"

fig, ax = plt.subplots(figsize=(13.4, 6.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(60, 580)
ax.axis("off")

# ---------------------------------------------------------------- icon library
def icon_person(cx, cy, s=22, color=GRAY, ghost=False):
    if ghost:
        ax.add_patch(Circle((cx, cy + s * 0.5), s * 0.34, facecolor="none",
                             edgecolor=color, linewidth=1.8, linestyle=(0, (3, 2)), zorder=8))
        body = Polygon([(cx - s * 0.52, cy - s * 0.55), (cx, cy - s * 0.18), (cx + s * 0.52, cy - s * 0.55),
                         (cx + 0.42 * s, cy - s * 0.9), (cx - 0.42 * s, cy - s * 0.9)],
                        closed=True, facecolor="none", edgecolor=color, linewidth=1.8,
                        linestyle=(0, (3, 2)), zorder=8)
        ax.add_patch(body)
    else:
        ax.add_patch(Circle((cx, cy + s * 0.5), s * 0.34, facecolor=color, edgecolor="none", zorder=8))
        body = Polygon([(cx - s * 0.52, cy - s * 0.55), (cx, cy - s * 0.18), (cx + s * 0.52, cy - s * 0.55),
                         (cx + 0.42 * s, cy - s * 0.9), (cx - 0.42 * s, cy - s * 0.9)],
                        closed=True, facecolor=color, edgecolor="none", zorder=8)
        ax.add_patch(body)


def icon_adversary(cx, cy, s=22, color=RED):
    """敵対者 — person にフラットハット。prover (素の person) と形で区別する。"""
    icon_person(cx, cy, s=s, color=color)
    ax.add_patch(Rectangle((cx - s * 0.5, cy + s * 0.72), s * 1.0, s * 0.14,
                            facecolor=color, edgecolor="none", zorder=9))
    ax.add_patch(Rectangle((cx - s * 0.26, cy + s * 0.84), s * 0.52, s * 0.3,
                            facecolor=color, edgecolor="none", zorder=9))


def icon_shield(cx, cy, s=22, color=GRAY):
    w, h = s * 1.15, s * 1.35
    pts = [(cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2), (cx + w / 2, cy),
           (cx, cy - h / 2), (cx - w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=color,
                          linewidth=1.8, zorder=8))
    ax.plot([cx - s * 0.3, cx - s * 0.06, cx + s * 0.32],
            [cy + s * 0.02, cy - s * 0.22, cy + s * 0.26],
            color="white", linewidth=2.6, solid_capstyle="round",
            solid_joinstyle="round", zorder=9)


def icon_book(cx, cy, s=22, color=GRAY):
    """公理系 (積み上がった書物)。"""
    for i, dy in enumerate((-0.5, -0.12, 0.26)):
        w = s * (1.5 - i * 0.12)
        ax.add_patch(Rectangle((cx - w / 2, cy + dy * s), w, s * 0.34,
                                facecolor="white", edgecolor=color, linewidth=2.0, zorder=8))


def straight(p1, p2, color=GRAY, lw=2.4, ls="solid", z=4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=17, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


# ===================================================================== 座標定数
C1, C2, C3 = 215, 630, 1045   # 3 列の中心
HEAD_Y = 545                  # 列ヘッダ
SUB_Y = 517
WIRE_Y = 400                  # 証明の実体の行 (Prover → π → Verifier)
ADV_Y = 205                   # 敵対者の行
EX_Y = 95                     # 例の行
PV_DX = 125                   # 列中心から Prover / Verifier までの距離

# ===================================================================== ③ のバンド (我々が立つ場所)
ax.add_patch(FancyBboxPatch((858, 72), 380, 492,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor=AMBER, alpha=0.05, linestyle=(0, (6, 4)), zorder=1))
ax.add_patch(FancyBboxPatch((858, 72), 380, 492,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor="none", linestyle=(0, (6, 4)), zorder=1))
ax.text(874, 84, "2026 年の社会実装はここ", ha="left", va="center", fontsize=13,
        fontweight="bold", color=AMBER, zorder=2)

# ===================================================================== ヘッダ行
def header(cx, num, title, sub):
    ax.text(cx, HEAD_Y, f"{num} {title}", ha="center", va="center", fontsize=17,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    ax.text(cx, SUB_Y, sub, ha="center", va="center", fontsize=13.5,
            fontweight="bold", color=TEXT_MUTED, zorder=6)

header(C1, "①", "数学的証明", "formal logic ・ 敵対者なし")
header(C2, "②", "情報論的暗号証明", "敵対者は計算能力 ∞")
header(C3, "③", "計算論的暗号証明", "敵対者は多項式時間 + 困難性仮定")

# ===================================================================== ① 公理 → 定理
icon_book(C1, WIRE_Y + 15)
ax.text(C1, WIRE_Y - 30, "公理系", ha="center", va="center", fontsize=15,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
straight((C1, WIRE_Y - 48), (C1, WIRE_Y - 110), color=GRAY, lw=2.4)
ax.text(C1 + 14, WIRE_Y - 79, "formal logic で導出", ha="left", va="center",
        fontsize=13, fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(C1, WIRE_Y - 140, "定理 (Q.E.D.)", ha="center", va="center", fontsize=16,
        fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(C1, WIRE_Y - 168, "誤りの確率 0 ・ 時間に依らない", ha="center", va="center",
        fontsize=13, fontweight="bold", color=TEXT_MUTED, zorder=6)

# 敵対者は「不在」 — ゴーストで描く
icon_person(C1, ADV_Y, s=22, color=GHOST_EDGE, ghost=True)
ax.text(C1, ADV_Y - 36, "敵対者なし", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color=GHOST_TEXT, zorder=6)

# ===================================================================== ②③ 共通: Prover → π → Verifier
def proof_wire(cx, pi_text, eq_text, icon_color, on_line_fc="white"):
    icon_person(cx - PV_DX, WIRE_Y, s=22, color=icon_color)
    ax.text(cx - PV_DX, WIRE_Y - 36, "Prover", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    icon_shield(cx + PV_DX, WIRE_Y, s=24, color=icon_color)
    ax.text(cx + PV_DX, WIRE_Y - 37, "Verifier", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    straight((cx - PV_DX + 40, WIRE_Y), (cx + PV_DX - 40, WIRE_Y), color=icon_color, lw=2.4)
    ax.text(cx, WIRE_Y + 24, pi_text, ha="center", va="center", fontsize=13,
            fontweight="bold", color=TEXT_PRIMARY, family="monospace", zorder=12,
            bbox=dict(facecolor=on_line_fc, edgecolor="none", pad=2.5))
    ax.text(cx + PV_DX, WIRE_Y - 64, eq_text, ha="center", va="center", fontsize=13,
            fontweight="bold", color=GREEN, family="monospace", zorder=6)

proof_wire(C2, "π = 0xA47B…", "g^z ≡ a·y^c ✓", GRAY)
proof_wire(C3, "π = 0x7a3f…", "e(a,b) ≡ e(g,vk) ✓", AMBER, on_line_fc=AMBER_BAND_FC)

# ===================================================================== ②③ の敵対者 (攻撃は届かない)
def adversary(cx, label, verdict, note=None):
    icon_adversary(cx, ADV_Y, s=22)
    ax.text(cx, ADV_Y - 38, label, ha="center", va="center", fontsize=13.5,
            fontweight="bold", color=RED, zorder=6)
    # 攻撃の試み: 上向きの赤い破線矢印が wire の手前で × に阻まれる
    straight((cx, ADV_Y + 32), (cx, WIRE_Y - 56), color=RED, lw=2.2, ls=(0, (4, 2.5)))
    ax.text(cx, WIRE_Y - 38, "×", ha="center", va="center", fontsize=20,
            fontweight="bold", color=RED, zorder=6)
    ax.text(cx + 12, ADV_Y + 75, verdict, ha="left", va="center", fontsize=13,
            fontweight="bold", color=RED, zorder=6)
    if note:
        ax.text(cx, ADV_Y - 64, note, ha="center", va="center", fontsize=13,
                fontweight="bold", color=AMBER, zorder=6)

adversary(C2, "敵対者 (計算能力 ∞)", "破れない — 確率 1")
adversary(C3, "敵対者 (多項式時間)", "偽造は negl(λ)", note="前提: DL / RSA / LWE が困難")

# ===================================================================== 例の行
# ③ の帯ラベル (y=84) と衝突しないよう、例の行は 3 列とも y=118 に揃える
EX_Y = 118
ax.text(C1, EX_Y, "例: フェルマーの最終定理", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(C2, EX_Y, "例: One-Time Pad / Σ-protocol", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(C3, EX_Y, "例: 電子署名 / SNARKs / Longfellow", ha="center", va="center", fontsize=13,
        fontweight="bold", color=TEXT_MUTED, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
