# kelp_arch.py — KelpDAO × LayerZero 1-of-1 DVN 事件の静的アーキ図 (SL08b)
#
# 生成: uv run --with matplotlib python3 figures/kelp_arch.py
# 出力: public/images/kelp_arch_static.png
#
# 設計語彙は .claude/skills/arch-diagram/SKILL.md に従う:
#   枠なし (アイコン+ラベルのみ) / 直角配線 / ゴースト破線=不在 /
#   赤=攻撃・改ざん (被害者は中立色+損失ラベル) / ラベルは白 bbox で線上に座る

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
OUT = "/home/gohan/workspace/presentation-agent/public/images/kelp_arch_static.png"

SURFACE = "#ffffff"
GRAY = "#475569"
GHOST_EDGE = "#94a3b8"      # ゴーストの輪郭 (破線)
GHOST_TEXT = "#64748b"      # ゴーストのラベル (輪郭より濃く、投影で読める)
RED = "#dc2626"
RED_BG = "#fef2f2"
AMBER = "#d97706"
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
    """Server-unit icon. ghost=True は破線輪郭のみ (不在/未参加)。"""
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
    """Verifier/shield icon (DVN 等の検証者)。形=役割: サーバー (icon_mini_server) と
    役割が違うアクターに同じ形を使わない。ghost=True は破線輪郭 (不在/未参加)。"""
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


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, zorder=9, box_alignment=box_alignment)
    ax.add_artist(ab)


# ---------------------------------------------------------------- primitives
def entity(cx, cy, icon_fn, label, sub=None, color=TEXT_PRIMARY, sub_color=None,
           fontsize=15, subfontsize=13.5, gap=36, subgap=19, on_line=False,
           on_line_fc="white"):
    """浮遊アイコン+ラベル (枠なし)。on_line=True はラベルに不透明 bbox を敷き、
    背後を通る接続線をラベルが「中断」する (線がテキストを貫通しない)。
    on_line_fc はその bbox の地色 — 周囲の地色に必ず合わせる (境界バンドの上なら
    バンドの合成色。白のままだと「白い四角」が浮く)。"""
    icon_fn(cx, cy)
    bbox = dict(facecolor=on_line_fc, edgecolor="none", pad=2.5) if on_line else None
    ax.text(cx, cy - gap, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=color, zorder=12, bbox=bbox)
    if sub:
        ax.text(cx, cy - gap - subgap, sub, ha="center", va="center", fontsize=subfontsize,
                fontweight="bold", color=(sub_color or color), zorder=12, bbox=bbox)


def section(x, y, label, color=GRAY, logo=None, logo_zoom=0.09):
    """セクション見出し — 枠なしプレーンテキスト。logo はテキストの左に置く。
    注: この図では最終的に全見出しを冗長と判断し未使用 (スコープはエンティティ
    ラベルに畳み込んだ: Karak RPC #N)。エンティティラベルに無い情報を足す
    グルーピングが必要な図のためだけに残している。"""
    if logo:
        add_logo(logo, (x, y + 1), logo_zoom)
        x += 24
    ax.text(x, y, label, ha="left", va="center", fontsize=15, fontweight="bold",
            color=color, family="monospace", zorder=2)


def straight(p1, p2, color=GRAY, lw=2.4, ls="solid", z=4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=17, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


def elbow_path(points, color=GRAY, lw=2.4, ls="solid", z=4, mutation_scale=14):
    """直角の多段コネクタ。最終セグメントだけ矢じり付き。"""
    for i in range(len(points) - 2):
        ax.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]],
                color=color, linewidth=lw, linestyle=ls, zorder=z)
    a = FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>", mutation_scale=mutation_scale,
                         linewidth=lw, color=color, linestyle=ls, zorder=z, shrinkA=0, shrinkB=2)
    ax.add_patch(a)


# ===================================================================== 座標定数
MAIN_Y = 420          # メインフロー行 (User → Karak → DVN #1 → Ethereum)
DVN_X = 580           # DVN #1 中心。callout leader / trunk はすべてこの x に揃う
COLLECT_Y = 330       # 改ざん RPC 2 台の応答が合流する水平コレクタ

# ===================================================================== KARAK L2 側
# チェーンの識別はエンティティラベル (Karak L2 Contract / Ethereum Contract) が
# 担うので、冗長な KARAK L2 / ETHEREUM 見出しは置かない
entity(110, MAIN_Y, lambda cx, cy: icon_person(cx, cy, s=22), "User")
straight((150, MAIN_Y), (266, MAIN_Y), lw=2.4)
ax.text(208, MAIN_Y + 17, "burns rsETH", ha="center", va="center", fontsize=13,
        color=TEXT_MUTED, fontweight="bold", zorder=6)
entity(320, MAIN_Y, lambda cx, cy: add_logo(f"{LOGO_DIR}/karak.png", (cx, cy), zoom=0.13),
       "Karak L2 Contract", fontsize=15)

# ===================================================================== DVN 群
# 検証レイヤー全体 (DVN 3 台) を LayerZero のベンダー境界バンドで囲う:
# 淡い破線の領域+左上にロゴ。エンティティの囲み枠とは別語彙 (subsystem boundary)。
# burns/release 矢印と偽応答トランクがバンドの縁を横切る = メッセージと攻撃が
# この LayerZero レイヤーを通過することを縁の交差で示す
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

# multisig であることは sub「(1-of-1)」とゴースト 2 台が伝える。DVN は検証者なので
# シールドアイコン (サーバーアイコンの RPC と形で区別する)
straight((362, MAIN_Y), (552, MAIN_Y), lw=2.4)
entity(DVN_X, MAIN_Y, lambda cx, cy: icon_shield(cx, cy, s=24, color=AMBER),
       "DVN #1", "active・signs (1-of-1)", color=TEXT_PRIMARY, sub_color=AMBER,
       gap=37, subgap=21, on_line=True,
       on_line_fc="#f7f7fe")  # LayerZero バンド (#6366f1 α.05 on white) の合成色
entity(430, 290, lambda cx, cy: icon_shield(cx, cy, s=20, color=GHOST_EDGE, ghost=True),
       "DVN #2", "未参加", color=GHOST_TEXT, gap=30, subgap=18, fontsize=13.5, subfontsize=12.5)
entity(740, 290, lambda cx, cy: icon_shield(cx, cy, s=20, color=GHOST_EDGE, ghost=True),
       "DVN #3", "未参加", color=GHOST_TEXT, gap=30, subgap=18, fontsize=13.5, subfontsize=12.5)

# ===== config callout — 枠なしのプレーンなコード行 (図の boxless トンマナに合わせる)。
# 致命的な値「1」だけを赤+細枠で強調し、その真下から垂直 leader が icon 上辺に着地
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

# ===================================================================== ETHEREUM 側
straight((598, MAIN_Y), (898, MAIN_Y), color=RED, lw=2.8)
ax.text(748, MAIN_Y + 17, "release() 実行", ha="center", va="center", fontsize=13.5,
        color=RED, fontweight="bold", zorder=6)
# 被害者コントラクトは中立色 (仕様通り動いた=無傷)。被害は流出額ラベルで示す
entity(950, MAIN_Y, lambda cx, cy: add_logo(f"{LOGO_DIR}/ethereum.png", (cx, cy), zoom=0.13),
       "Ethereum Contract", color=TEXT_PRIMARY, fontsize=15, gap=36)
ax.text(950, MAIN_Y - 60, "−116,500 rsETH（$292M）流出", ha="center", va="center",
        fontsize=13.5, fontweight="bold", color=RED, zorder=6)

# ===================================================================== Karak RPC 群
# DVN #1 の直下にクラスタ化 (= DVN #1 の情報源プールであることを空間で示す)。
# 見出しは置かず、どのチェーンを読む RPC かはラベル「Karak RPC #N」に畳み込む
# 改ざんされた 2 台はトランク (x=580) の両脇に置く → 赤い配線が
# ゴースト DVN #2/#3 を囲い込まず、「この 2 本だけが DVN #1 に届く」と読める
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

# 改ざん RPC 2 台 → コレクタで合流 → 単一トランクが DVN #1 の下辺に入る。
# DVN #1 のラベルは白 bbox (on_line) なのでトランクがテキストを貫通しない
feed_ls = (0, (4, 2.5))
ax.plot([500, 500], [185, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.plot([660, 660], [165, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.plot([500, 660], [COLLECT_Y, COLLECT_Y], color=RED, linewidth=2.4, linestyle=feed_ls, zorder=4)
ax.add_patch(Circle((DVN_X, COLLECT_Y), 5, facecolor=RED, edgecolor="none", zorder=5))
straight((DVN_X, COLLECT_Y), (DVN_X, MAIN_Y - 18), color=RED, lw=2.4, ls=feed_ls, z=4)
ax.text(DVN_X, COLLECT_Y - 16, "偽の応答", ha="center", va="center", fontsize=13,
        fontweight="bold", color=RED, zorder=6)

plt.tight_layout(pad=1.0)
plt.savefig(OUT, facecolor=SURFACE, bbox_inches="tight")
print("saved:", OUT, "| font:", font_family)
