# eth_privacy.py — Ethereum の tx 経路とプライバシー保護範囲の before/after (SL10d)
#
# 生成: uv run --with matplotlib python3 figures/eth_privacy.py
# 出力: public/images/eth_privacy_arch.png
#
# 設計 (.claude/skills/arch-diagram/SKILL.md):
#   - 同じ 4 actor (User → RPC → EL → CL) を上下 2 段に並べた before/after。
#   - 各段の下に「保護範囲バー」: green = 暗号で守られている区間 / amber = 可視のまま。
#     「どこからどこまで守られているか」をバーの長さだけで読ませる。
#   - green = 追加された防御 (Kohaku / PIR / shielded write / encrypted mempool)。
#   - amber = 可視・劣化 (赤は攻撃経路専用なので使わない)。枠なし・直角配線・塗り矢印。

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

OUT = "/home/gohan/workspace/presentation-agent/public/images/eth_privacy_arch.png"

SURFACE = "#ffffff"
GRAY = "#475569"
AMBER = "#d97706"
AMBER_SOFT = "#fbbf24"
GREEN = "#059669"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.2, 6.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(0, 640)
ax.axis("off")

X_USER, X_RPC, X_EL, X_CL = 130, 490, 830, 1140

# ---------------------------------------------------------------- icon library
def icon_person(cx, cy, s=20, color=GRAY):
    ax.add_patch(Circle((cx, cy + s * 0.55), s * 0.34, facecolor=color, edgecolor="none", zorder=8))
    ax.add_patch(Rectangle((cx - s * 0.5, cy - s * 0.75), s, s * 0.95, facecolor=color,
                           edgecolor="none", zorder=8))

def icon_server(cx, cy, s=20, color=GRAY):
    for i, dy in enumerate((0.45, -0.05, -0.55)):
        ax.add_patch(Rectangle((cx - s * 0.85, cy + dy * s), s * 1.7, s * 0.42,
                               facecolor="white", edgecolor=color, linewidth=2.0, zorder=8))
        ax.add_patch(Circle((cx + s * 0.55, cy + (dy + 0.21) * s), s * 0.07,
                            facecolor=color, edgecolor="none", zorder=9))

def icon_block(cx, cy, s=20, color=GRAY):
    ax.add_patch(Rectangle((cx - s * 0.8, cy - s * 0.7), s * 1.6, s * 1.4,
                           facecolor="white", edgecolor=color, linewidth=2.2, zorder=8))
    ax.add_patch(Circle((cx, cy), s * 0.3, facecolor=color, edgecolor="none", zorder=9))

def icon_network(cx, cy, s=20, color=GRAY):
    pts = [(cx, cy + s * 0.65), (cx - s * 0.75, cy - s * 0.45), (cx + s * 0.75, cy - s * 0.45)]
    for a in pts:
        for b in pts:
            if a < b:
                ax.plot([a[0], b[0]], [a[1], b[1]], color=color, linewidth=1.8, zorder=7)
    for p in pts:
        ax.add_patch(Circle(p, s * 0.22, facecolor=color, edgecolor="white", linewidth=1.5, zorder=8))

def wire(x1, x2, y, color=GRAY, lw=2.4, ls="solid"):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>", mutation_scale=16,
                                 linewidth=lw, color=color, linestyle=ls, zorder=5,
                                 shrinkA=2, shrinkB=2))

def actor_row(y_icon, y_label):
    icon_person(X_USER, y_icon)
    ax.text(X_USER, y_label, "User (wallet)", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=8)
    icon_server(X_RPC, y_icon)
    ax.text(X_RPC, y_label, "RPC provider", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=8)
    icon_block(X_EL, y_icon)
    ax.text(X_EL, y_label, "EL client (mempool)", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=8)
    icon_network(X_CL, y_icon)
    ax.text(X_CL, y_label, "CL consensus", ha="center", va="center", fontsize=15,
            fontweight="bold", color=TEXT_PRIMARY, zorder=8)

def coverage_bar(y, segments):
    """segments: list of (x1, x2, color, label, label_color)"""
    for x1, x2, c, label, lc in segments:
        ax.add_patch(Rectangle((x1, y), x2 - x1, 9, facecolor=c, edgecolor="none", zorder=6))
        if label:
            ax.text((x1 + x2) / 2, y - 17, label, ha="center", va="center", fontsize=13,
                    fontweight="bold", color=lc, zorder=8)

# ================================================================= 上段: これまで
Y1_ICON, Y1_LABEL, Y1_NOTE, Y1_BAR = 520, 478, 447, 400

ax.text(20, 610, "これまで — 暗号が守っていたのは通信路 (TLS) だけ", ha="left", va="center",
        fontsize=17, fontweight="bold", color=TEXT_PRIMARY)

actor_row(Y1_ICON, Y1_LABEL)
wire(X_USER + 40, X_RPC - 55, Y1_ICON, color=GREEN)
ax.text((X_USER + X_RPC) / 2, Y1_ICON + 22, "TLS", ha="center", va="center", fontsize=14,
        fontweight="bold", color=GREEN, zorder=8)
wire(X_RPC + 55, X_EL - 50, Y1_ICON, color=GRAY)
wire(X_EL + 50, X_CL - 55, Y1_ICON, color=GRAY)

ax.text(X_RPC, Y1_NOTE, "アドレス・残高照会・IP が\nすべて見える", ha="center", va="center",
        fontsize=13, fontweight="bold", color=AMBER, zorder=8)
ax.text(X_EL, Y1_NOTE, "mempool は平文 —\nvalidator に可視", ha="center", va="center",
        fontsize=13, fontweight="bold", color=AMBER, zorder=8)
ax.text(X_CL, Y1_NOTE, "チェーン上は\n全公開", ha="center", va="center",
        fontsize=13, fontweight="bold", color=AMBER, zorder=8)

coverage_bar(Y1_BAR, [
    (X_USER, X_RPC, GREEN, "通信路のみ暗号化", GREEN),
    (X_RPC, X_CL + 60, AMBER_SOFT, "中身は事業者・validator・全世界に可視", AMBER),
])

# ================================================================= 下段: これから
Y2_ICON, Y2_LABEL, Y2_NOTE, Y2_BAR = 240, 198, 167, 120

ax.text(20, 330, "これから — 経路全体がプライバシー前提に (EF ロードマップ)", ha="left",
        va="center", fontsize=17, fontweight="bold", color=TEXT_PRIMARY)

actor_row(Y2_ICON, Y2_LABEL)
wire(X_USER + 40, X_RPC - 55, Y2_ICON, color=GREEN)
wire(X_RPC + 55, X_EL - 50, Y2_ICON, color=GREEN)
wire(X_EL + 50, X_CL - 55, Y2_ICON, color=GREEN)

# green の追加要素
ax.text(X_USER, Y2_ICON + 52, "Kohaku (EF)", ha="center", va="center", fontsize=14,
        fontweight="bold", color=GREEN, zorder=8)
ax.text((X_USER + X_RPC) / 2, Y2_ICON + 24, "PIR read — 何を読んだか\nRPC にも見えない", ha="center",
        va="bottom", fontsize=13, fontweight="bold", color=GREEN, zorder=8)
ax.text((X_RPC + X_EL) / 2, Y2_ICON + 24, "shielded write\n(Privacy Pools / Railgun)", ha="center",
        va="bottom", fontsize=13, fontweight="bold", color=GREEN, zorder=8)
ax.text((X_EL + X_CL) / 2, Y2_ICON + 24, "encrypted mempool\n(threshold 復号)", ha="center",
        va="bottom", fontsize=13, fontweight="bold", color=GREEN, zorder=8)

ax.text(X_USER, Y2_NOTE, "privacy 既定の\nwallet SDK", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=8)
ax.text(X_CL, Y2_NOTE, "on-chain は証明と\nコミットメントのみ", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=GREEN, zorder=8)

coverage_bar(Y2_BAR, [
    (X_USER, X_CL + 60, GREEN, "読み取り・書き込み・伝播 — 全区間を暗号で保護", GREEN),
])

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
