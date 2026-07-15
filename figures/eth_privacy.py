# eth_privacy.py — Ethereum の tx 経路とプライバシー保護範囲 (SL10d)
#
# 生成: uv run --with matplotlib python3 figures/eth_privacy.py
# 出力: public/images/eth_privacy_arch.png
#
# 設計語彙は .claude/skills/arch-diagram/SKILL.md + figures/kelp_arch.py に従う:
#   枠なし (アイコン+ラベルのみ) / 直角配線・塗り矢印 / 境界バンド = on-chain 領域 /
#   amber = 現状の露出 (可視) / green = これから足す防御 (Kohaku・PIR・shielded write・
#   encrypted mempool) — p4→p6 と同じ「基底 + 差分」の読み方。
#   下部の 2 本のバー = 保護範囲 (これまで: TLS 区間のみ / これから: 全区間)。

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
OUT = "/home/gohan/workspace/presentation-agent/public/images/eth_privacy_arch.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST_EDGE = "#94a3b8"
AMBER = "#d97706"
AMBER_SOFT = "#fbbf24"
GREEN = "#059669"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.4, 6.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(70, 578)
ax.axis("off")

# ---------------------------------------------------------------- icon library
def icon_person(cx, cy, s=22, color=GRAY):
    ax.add_patch(Circle((cx, cy + s * 0.5), s * 0.34, facecolor=color, edgecolor="none", zorder=8))
    body = Polygon([(cx - s * 0.52, cy - s * 0.55), (cx, cy - s * 0.18), (cx + s * 0.52, cy - s * 0.55),
                     (cx + 0.42 * s, cy - s * 0.9), (cx - 0.42 * s, cy - s * 0.9)],
                    closed=True, facecolor=color, edgecolor="none", zorder=8)
    ax.add_patch(body)


def icon_mini_server(cx, cy, s=22, color=GRAY):
    w, h = s * 1.05, s * 1.3
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, facecolor=color,
                            edgecolor=color, linewidth=1.8, zorder=8))
    for dy in (0.28, -0.06, -0.4):
        ax.add_patch(Rectangle((cx - w * 0.32, cy + dy * h - 0.035 * h), w * 0.64, 0.07 * h,
                                facecolor="white", edgecolor="none", zorder=9))


def icon_block(cx, cy, s=22, color=GRAY):
    """EL client (実行エンジン): ブロック型。"""
    w = s * 1.5
    ax.add_patch(Rectangle((cx - w / 2, cy - w / 2), w, w, facecolor="white",
                            edgecolor=color, linewidth=2.2, zorder=8))
    ax.add_patch(Circle((cx, cy), s * 0.32, facecolor=color, edgecolor="none", zorder=9))


def icon_network(cx, cy, s=22, color=GRAY):
    """CL consensus (ノード網): 三角メッシュ。"""
    pts = [(cx, cy + s * 0.62), (cx - s * 0.72, cy - s * 0.45), (cx + s * 0.72, cy - s * 0.45)]
    for i in range(3):
        for j in range(i + 1, 3):
            ax.plot([pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]],
                    color=color, linewidth=1.8, zorder=7)
    for p in pts:
        ax.add_patch(Circle(p, s * 0.22, facecolor=color, edgecolor="white",
                            linewidth=1.5, zorder=8))


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, zorder=9, box_alignment=box_alignment)
    ax.add_artist(ab)


# ---------------------------------------------------------------- primitives
def entity(cx, cy, icon_fn, label, fontsize=15, gap=36, on_line=False, on_line_fc="white"):
    icon_fn(cx, cy)
    bbox = dict(facecolor=on_line_fc, edgecolor="none", pad=2.5) if on_line else None
    ax.text(cx, cy - gap, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=TEXT_PRIMARY, zorder=12, bbox=bbox)


def straight(p1, p2, color=GRAY, lw=2.4, ls="solid", z=4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=17, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


# ===================================================================== 座標定数
MAIN_Y = 420          # メインフロー行 (User → RPC → EL → CL)
X_USER, X_RPC, X_EL, X_CL = 110, 430, 770, 1070
BAND_FC = "#f6f9fc"   # on-chain バンド (#6366f1 α.04 相当) の合成地色

# ===================================================================== on-chain バンド
ax.add_patch(FancyBboxPatch((650, 245), 540, 245,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor="#6366f1", alpha=0.04, linestyle=(0, (6, 4)),
                             zorder=1))
ax.add_patch(FancyBboxPatch((650, 245), 540, 245,
                             boxstyle="round,pad=0,rounding_size=10",
                             linewidth=1.5, edgecolor=GHOST_EDGE,
                             facecolor="none", linestyle=(0, (6, 4)), zorder=1))
add_logo(f"{LOGO_DIR}/ethereum.png", (676, 472), zoom=0.075)
ax.text(694, 472, "Ethereum (on-chain)", ha="left", va="center", fontsize=13,
        fontweight="bold", color=GRAY, zorder=2)

# ===================================================================== メインフロー
entity(X_USER, MAIN_Y, lambda cx, cy: icon_person(cx, cy, s=22), "User (wallet)")
straight((150, MAIN_Y), (X_RPC - 46, MAIN_Y), lw=2.4)
entity(X_RPC, MAIN_Y, lambda cx, cy: icon_mini_server(cx, cy, s=22), "RPC provider")
straight((X_RPC + 46, MAIN_Y), (X_EL - 44, MAIN_Y), lw=2.4)
entity(X_EL, MAIN_Y, lambda cx, cy: icon_block(cx, cy, s=22), "EL client (mempool)",
       on_line=True, on_line_fc=BAND_FC)
straight((X_EL + 44, MAIN_Y), (X_CL - 44, MAIN_Y), lw=2.4)
entity(X_CL, MAIN_Y, lambda cx, cy: icon_network(cx, cy, s=24), "CL consensus",
       on_line=True, on_line_fc=BAND_FC)

# 配線ラベル: 線の上に 3 段 (gray = 何が流れるか / green = これから足す防御)
ax.text(292, MAIN_Y + 18, "eth_call ・ sendRawTransaction", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)
ax.text(292, MAIN_Y + 42, "shielded write (Privacy Pools / Railgun)", ha="center", va="center",
        fontsize=13, fontweight="bold", color=GREEN, zorder=6)
ax.text(292, MAIN_Y + 64, "PIR read — 何を読んだか秘匿", ha="center", va="center",
        fontsize=13, fontweight="bold", color=GREEN, zorder=6)

# ===================================================================== amber = 現状の露出
ax.text(X_RPC, MAIN_Y - 57, "アドレス・照会・IP が\nすべて見える", ha="center", va="top",
        fontsize=13, fontweight="bold", color=AMBER, zorder=6)
ax.text(X_EL, MAIN_Y - 57, "mempool は平文", ha="center", va="top",
        fontsize=13, fontweight="bold", color=AMBER, zorder=6, bbox=dict(
            facecolor=BAND_FC, edgecolor="none", pad=2.5))
ax.text(X_CL, MAIN_Y - 57, "チェーン上は全公開", ha="center", va="top",
        fontsize=13, fontweight="bold", color=AMBER, zorder=6, bbox=dict(
            facecolor=BAND_FC, edgecolor="none", pad=2.5))

# ===================================================================== green = 足す防御 (差分)
# Kohaku callout — kelp の setConfig callout と同じ形式 (プレーン 1 行 + 垂直 leader)
CALLOUT_Y = 538
ax.text(X_USER, CALLOUT_Y, "Kohaku (EF) — privacy 既定の wallet SDK", ha="left", va="center",
        fontsize=14, fontweight="bold", color=GREEN, zorder=11)
straight((X_USER, CALLOUT_Y - 16), (X_USER, MAIN_Y + 40), color=GREEN, lw=2.0,
         ls=(0, (3, 2)), z=5)

ax.text(X_EL, MAIN_Y - 100, "→ encrypted mempool\n(threshold 復号)", ha="center", va="top",
        fontsize=13, fontweight="bold", color=GREEN, zorder=6, bbox=dict(
            facecolor=BAND_FC, edgecolor="none", pad=2.5))
ax.text(X_CL, MAIN_Y - 100, "→ 証明とコミットメント\nのみを公開", ha="center", va="top",
        fontsize=13, fontweight="bold", color=GREEN, zorder=6, bbox=dict(
            facecolor=BAND_FC, edgecolor="none", pad=2.5))

# ===================================================================== 保護範囲バー (下部)
BAR_X0, BAR_X1 = X_USER, 1190

def coverage_bar(y, row_label, segments, labels):
    ax.text(BAR_X0 - 18, y + 4, row_label, ha="right", va="center", fontsize=13.5,
            fontweight="bold", color=TEXT_PRIMARY, zorder=6)
    for x1, x2, c in segments:
        ax.add_patch(Rectangle((x1, y), x2 - x1, 9, facecolor=c, edgecolor="none", zorder=5))
    for x, text, c in labels:
        ax.text(x, y - 17, text, ha="center", va="center", fontsize=12.5,
                fontweight="bold", color=c, zorder=6)

coverage_bar(200, "これまで",
             [(BAR_X0, X_RPC, GREEN), (X_RPC, BAR_X1, AMBER_SOFT)],
             [((BAR_X0 + X_RPC) / 2, "TLS — 通信路のみ", GREEN),
              ((X_RPC + BAR_X1) / 2, "中身は事業者・validator・全世界に可視", AMBER)])

coverage_bar(130, "これから",
             [(BAR_X0, BAR_X1, GREEN)],
             [((BAR_X0 + BAR_X1) / 2, "PIR + shielded write + encrypted mempool — 全区間を暗号で保護", GREEN)])

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
