# trend_common.py — 「実用性の変化グラフ」シリーズ (SL17/SL18/SL20/SL21) の共通描画基盤
#
# 使い方: figures/trend_*.py から import して render_trend(...) を呼ぶ。
# 1 スクリプト = 1 PNG の規約は各 trend_*.py 側が担う。
#
# 設計 (デッキのトンマナに従う):
#   - 折れ線 1-2 本、時間軸は実年 (理論が眠っていた期間の長さがそのまま物語になる)
#   - 縦軸は「実用性」の概念軸 — 目盛りなし、注記で定量値でないことを明示
#   - 上部の淡い緑バンド = production 域 (実サービスで稼働)
#   - 凡例は置かない。曲線への直接ラベルとマイルストーン注記で読ませる
#   - ロゴは public/logos/ から実寸逆算 zoom (固定 zoom 禁止) で配置
#
# point の指定:
#   {"year", "y"}                    … 波形制御用の無ラベル waypoint (label 省略)
#   {"label", "sub", "logo"}         … 注記。位置は side ("up"/"down") で自動、
#   {"label_xy", "sub_xy", "logo_xy"}… または座標で明示指定 (混雑地帯は明示が基本)
#   {"ha"}                           … テキストアンカー (default "center")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
FONT_FAMILY = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = FONT_FAMILY
plt.rcParams["axes.unicode_minus"] = False

LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

SURFACE = "#ffffff"
GRAY = "#475569"
AMBER = "#d97706"
GREEN = "#059669"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"
TEXT_FAINT = "#9ca3af"
BAND_FC = "#ecfdf5"
BAND_TEXT = "#059669"
AXIS = "#d1d5db"

Y_MAX = 11.4
BAND_Y = 8.3

TARGET_LOGO_H = 40.0   # 表示高さ (px 相当)。実寸から逆算する
MAX_LOGO_W = 110.0


def _logo_zoom(path):
    img = mpimg.imread(path)
    h, w = img.shape[0], img.shape[1]
    return min(TARGET_LOGO_H / h, MAX_LOGO_W / w)


def render_trend(out, xlim, series, xticks,
                 band_label="production ─ 実サービスで稼働",
                 band_label_xy=None, band_label_ha="right",
                 note="縦軸は実用性の概念図 (定量値ではない)",
                 annotations=None, figsize=(13.2, 5.9)):
    fig, ax = plt.subplots(figsize=figsize, dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(*xlim)
    ax.set_ylim(0, Y_MAX)

    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.tick_params(left=False, labelleft=False)

    # production 域バンド
    ax.axhspan(BAND_Y, Y_MAX, facecolor=BAND_FC, zorder=0)
    ax.axhline(BAND_Y, color="#a7f3d0", linewidth=1.5, linestyle=(0, (5, 4)), zorder=1)
    if band_label_xy is None:
        band_label_xy = (xlim[1] - (xlim[1] - xlim[0]) * 0.012, Y_MAX - 0.55)
    ax.text(band_label_xy[0], band_label_xy[1], band_label, ha=band_label_ha,
            va="center", fontsize=13.5, fontweight="bold", color=BAND_TEXT, zorder=6)

    # x 軸 (実年)
    ax.axhline(0, color=AXIS, linewidth=1.6, zorder=1)
    ax.set_xticks(xticks)
    ax.set_xticklabels([str(t) for t in xticks], fontsize=13,
                       fontweight="bold", color=TEXT_MUTED)
    ax.tick_params(axis="x", length=0, pad=8)

    # 縦軸の意味 (左端の上向き矢印)
    x_arrow = xlim[0] + (xlim[1] - xlim[0]) * 0.004
    ax.annotate("", xy=(x_arrow, 10.6), xytext=(x_arrow, 0.4),
                arrowprops=dict(arrowstyle="-|>", color=TEXT_FAINT, lw=1.8))
    ax.text(x_arrow + (xlim[1] - xlim[0]) * 0.012, 10.5, "実用性", ha="left",
            va="top", fontsize=14, fontweight="bold", color=TEXT_MUTED)

    for s in series:
        xs = [p["year"] for p in s["points"]]
        ys = [p["y"] for p in s["points"]]
        ax.plot(xs, ys, color=s["color"], linewidth=3.2, zorder=4,
                solid_capstyle="round", solid_joinstyle="round")
        marked = [p for p in s["points"] if p.get("label")]
        ax.scatter([p["year"] for p in marked], [p["y"] for p in marked],
                   s=95, facecolor=s["color"], edgecolor="white",
                   linewidth=2.2, zorder=5)

        # 曲線への直接ラベル (凡例の代わり)
        if "name_xy" in s:
            ax.text(s["name_xy"][0], s["name_xy"][1], s["name"], ha=s.get("name_ha", "left"),
                    va="center", fontsize=15, fontweight="bold", color=s["color"], zorder=6)

        for p in marked:
            side = 1 if p.get("side", "up") == "up" else -1
            ha = p.get("ha", "center")
            lx, ly = p.get("label_xy", (p["year"], p["y"] + side * 0.85))
            ax.text(lx, ly, p["label"], ha=ha, va="center", fontsize=14,
                    fontweight="bold", color=TEXT_PRIMARY, zorder=6)
            if p.get("sub"):
                sx, sy = p.get("sub_xy", (p["year"], p["y"] + side * 1.5))
                ax.text(sx, sy, p["sub"], ha=p.get("sub_ha", ha), va="center",
                        fontsize=12.5, fontweight="bold", color=TEXT_MUTED, zorder=6)
            if p.get("logo"):
                path = f"{LOGO_DIR}/{p['logo']}"
                gx, gy = p.get("logo_xy",
                               (p["year"], p["y"] + side * (2.5 if p.get("sub") else 1.9)))
                ab = AnnotationBbox(OffsetImage(mpimg.imread(path), zoom=_logo_zoom(path)),
                                    (gx, gy), frameon=False, zorder=7)
                ax.add_artist(ab)

    for a in (annotations or []):
        ax.text(a["xy"][0], a["xy"][1], a["text"], ha=a.get("ha", "center"), va="center",
                fontsize=a.get("fontsize", 13), fontweight="bold",
                color=a.get("color", TEXT_MUTED), zorder=6,
                fontstyle=a.get("style", "normal"))

    # 概念図であることの注記
    ax.text(xlim[1] - (xlim[1] - xlim[0]) * 0.012, 0.45, note, ha="right", va="center",
            fontsize=11.5, fontweight="bold", color=TEXT_FAINT, zorder=6)

    plt.tight_layout(pad=1.0)
    plt.savefig(out, facecolor=SURFACE, bbox_inches="tight")
    print("saved:", out, "| font:", FONT_FAMILY)
