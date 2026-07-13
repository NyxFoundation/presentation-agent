import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon, Arc
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

candidates = ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic", "TakaoGothic"]
available = {f.name for f in fm.fontManager.ttflist}
font_family = next((c for c in candidates if c in available), "sans-serif")
plt.rcParams["font.family"] = font_family
plt.rcParams["axes.unicode_minus"] = False

LOGO_DIR = "/home/gohan/workspace/presentation-agent/public/logos"

SURFACE = "#ffffff"
GRAY = "#475569"
GRAY_LIGHT = "#94a3b8"
GRAY_BG = "#f1f5f9"
AMBER = "#d97706"
AMBER_BG = "#fffbeb"
GREEN = "#059669"
GREEN_BG = "#f0fdf4"
TEXT_PRIMARY = "#1f2937"
TEXT_MUTED = "#6b7280"

fig, ax = plt.subplots(figsize=(13.4, 6.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 1260)
ax.set_ylim(0, 580)
ax.axis("off")

# ---------------------------------------------------------------- icon library
def icon_magnifier(cx, cy, s=16, color=GRAY):
    r = s * 0.32
    ax.add_patch(Circle((cx - s * 0.1, cy + s * 0.12), r, facecolor="none",
                         edgecolor=color, linewidth=2.4, zorder=8))
    ax.plot([cx - s * 0.1 + r * 0.72, cx + s * 0.42], [cy + s * 0.12 - r * 0.72, cy - s * 0.42],
            color=color, linewidth=2.8, zorder=8, solid_capstyle="round")


def icon_pi(cx, cy, s=16, color=GRAY):
    ax.plot([cx - s * 0.5, cx + s * 0.5], [cy + s * 0.32, cy + s * 0.32],
            color=color, linewidth=2.8, zorder=8, solid_capstyle="round")
    ax.plot([cx - s * 0.26, cx - s * 0.3], [cy + s * 0.32, cy - s * 0.45],
            color=color, linewidth=2.8, zorder=8, solid_capstyle="round")
    ax.plot([cx + s * 0.3, cx + s * 0.34], [cy + s * 0.32, cy - s * 0.45],
            color=color, linewidth=2.8, zorder=8, solid_capstyle="round")


def icon_shield(cx, cy, s=17, color=GRAY, mode="check"):
    pts = [(cx - s * 0.52, cy + s * 0.5), (cx + s * 0.52, cy + s * 0.5), (cx + s * 0.52, cy - s * 0.05),
           (cx, cy - s * 0.62), (cx - s * 0.52, cy - s * 0.05)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=color, linewidth=1.8, zorder=8))
    if mode == "check":
        ax.plot([cx - s * 0.24, cx - s * 0.03, cx + s * 0.32],
                [cy + s * 0.02, cy - s * 0.18, cy + s * 0.28],
                color="white", linewidth=2.6, zorder=9, solid_capstyle="round", solid_joinstyle="round")


def icon_power(cx, cy, s=16, color=GRAY):
    ax.add_patch(Arc((cx, cy - s * 0.08), s * 0.92, s * 0.92, angle=0, theta1=35, theta2=325,
                      color=color, linewidth=2.6, zorder=8))
    ax.plot([cx, cx], [cy + s * 0.1, cy + s * 0.52], color=color, linewidth=2.6,
            zorder=8, solid_capstyle="round")


def icon_lock(cx, cy, s=16, color=GRAY):
    ax.add_patch(Arc((cx, cy + s * 0.18), s * 0.56, s * 0.68, angle=0, theta1=0, theta2=180,
                      color=color, linewidth=2.4, zorder=8))
    ax.add_patch(Rectangle((cx - s * 0.42, cy - s * 0.38), s * 0.84, s * 0.52,
                            facecolor="white", edgecolor=color, linewidth=2.2, zorder=8))
    ax.add_patch(Circle((cx, cy - s * 0.12), s * 0.08, facecolor=color, edgecolor="none", zorder=9))


def add_logo(path, xy, zoom, box_alignment=(0.5, 0.5)):
    img = mpimg.imread(path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, zorder=9, box_alignment=box_alignment)
    ax.add_artist(ab)


# ---------------------------------------------------------------- node/group helpers
def node(x, y, w, h, label, sub=None, style="normal", icon=None, fontsize=15):
    if style == "amber":
        face, edge, tcolor = AMBER_BG, AMBER, "#78350f"
    elif style == "green":
        face, edge, tcolor = GREEN_BG, GREEN, "#065f46"
    else:
        face, edge, tcolor = "white", GRAY, TEXT_PRIMARY
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=10",
                          linewidth=2, edgecolor=edge, facecolor=face, zorder=5)
    ax.add_patch(box)
    cx = x + w / 2
    if icon:
        icon(cx, y + h - 26)
        label_y = y + h - 52
    else:
        label_y = y + h / 2 + (11 if sub else 0)
    ax.text(cx, label_y, label, ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=tcolor, zorder=6)
    if sub:
        suby = (y + h - 52 - 20) if icon else (y + h / 2 - 16)
        ax.text(cx, suby, sub, ha="center", va="center", fontsize=11.5,
                color=tcolor, zorder=6, fontweight="bold")
    return (x, y, w, h)


def group_box(x, y, w, h, label, label_color=GRAY, bg="#f8fafc", mono=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=8",
                                 linewidth=1.3, edgecolor="#cbd5e1", facecolor=bg,
                                 linestyle=(0, (5, 3)), zorder=1))
    kwargs = {"family": "monospace"} if mono else {}
    ax.text(x + 16, y + h - 24, label, ha="left", va="center", fontsize=12.5,
            fontweight="bold", color=label_color, zorder=2, **kwargs)


def arrow(p1, p2, color=GRAY, lw=2.4, z=4, connectionstyle="arc3,rad=0", ls="solid"):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=18, linewidth=lw,
                         color=color, linestyle=ls, zorder=z, connectionstyle=connectionstyle,
                         shrinkA=2, shrinkB=2)
    ax.add_patch(a)


# ===== top: audit loop config-strip callout (mirrors kelp's setConfig callout style) =====
callout_x, callout_y, callout_w, callout_h = 330, 495, 600, 66
ax.add_patch(FancyBboxPatch((callout_x, callout_y), callout_w, callout_h,
                             boxstyle="round,pad=0,rounding_size=9",
                             linewidth=2, edgecolor=AMBER, facecolor=AMBER_BG, zorder=10))
ax.text(callout_x + callout_w / 2, callout_y + 44,
        "audit_loop: scan(C)  //  exploit 発見、まだ drain していない",
        ha="center", va="center", fontsize=14.5, fontweight="bold", color="#78350f",
        zorder=11)
ax.text(callout_x + callout_w / 2, callout_y + 15,
        "コントラクト C を継続監査 — ドレインが起きる前に手を打つ",
        ha="center", va="center", fontsize=11.5, color="#92400e", fontweight="bold", zorder=11)

# ===== OFF-CHAIN group =====
group_box(30, 260, 560, 210, "OFF-CHAIN (継続監査)", label_color="#4338ca", bg="#eef2ff", mono=False)
node(60, 300, 230, 130, "AI Auditor", "witness W を発見", style="amber",
     icon=lambda cx, cy: icon_magnifier(cx, cy, s=16, color=AMBER), fontsize=17)
node(345, 300, 220, 130, "ZK Prover", "π = Prove(∃W : drain(W,C))", style="amber",
     icon=lambda cx, cy: icon_pi(cx, cy, s=16, color=AMBER), fontsize=17)
arrow((290, 365), (345, 365), color=AMBER, lw=2.4)

# ===== ON-CHAIN group =====
group_box(30, 30, 1200, 200, "ON-CHAIN (プロトコル + 暗号的ガード)", label_color="#065f46", bg="#f0fdf4", mono=False)
node(60, 55, 220, 130, "ZK Verifier", "✓ π accepted", style="green",
     icon=lambda cx, cy: icon_shield(cx, cy, s=17, color=GREEN, mode="check"), fontsize=16)
node(340, 55, 230, 130, "Circuit-Breaker", "発火 (fired)", style="green",
     icon=lambda cx, cy: icon_power(cx, cy, s=16, color=GREEN), fontsize=16)
node(630, 55, 260, 130, "DeFi Contract", "halted — drain 阻止", style="green",
     icon=lambda cx, cy: icon_lock(cx, cy, s=16, color=GREEN), fontsize=16)

arrow((280, 120), (340, 120), color=GREEN, lw=2.6)
arrow((570, 120), (630, 120), color=GREEN, lw=2.6)

# vertical wire: Prover -> Verifier (π submitted on-chain) — enters from the right
# of the ON-CHAIN group so it never crosses the group's corner label
arrow((420, 300), (285, 140), color=AMBER, lw=2.6, connectionstyle="arc3,rad=0.12")
ax.text(378, 232, "π を on-chain に submit", ha="center", va="center", fontsize=12,
        color="#92400e", fontweight="bold", zorder=6, rotation=-49)

# ===== witness stays secret note =====
ax.add_patch(FancyBboxPatch((615, 300), 350, 40, boxstyle="round,pad=0,rounding_size=7",
                             linewidth=1.3, edgecolor=GRAY_LIGHT, facecolor="white", zorder=5))
ax.text(790, 320, "W (witness) は秘密のまま\non-chain には π だけを提出", ha="center", va="center",
        fontsize=11.5, color=TEXT_MUTED, fontweight="bold", zorder=6, linespacing=1.4)

# ===== diff: concrete KelpDAO instantiation of the abstract W / DeFi Contract =====
diff_x, diff_y, diff_w, diff_h = 615, 355, 350, 100
ax.add_patch(FancyBboxPatch((diff_x, diff_y), diff_w, diff_h, boxstyle="round,pad=0,rounding_size=8",
                             linewidth=1.4, edgecolor=GRAY_LIGHT, facecolor="white",
                             linestyle=(0, (4, 2)), zorder=5))
ax.text(diff_x + 16, diff_y + diff_h - 20, "KelpDAO の場合 (具体例)", ha="left", va="center",
        fontsize=12, fontweight="bold", color=TEXT_PRIMARY, zorder=6)
ax.text(diff_x + 16, diff_y + diff_h - 46, "W = config の requiredDVNCount = 1", ha="left", va="center",
        fontsize=11, color=TEXT_MUTED, fontweight="bold", zorder=6)
ax.text(diff_x + 16, diff_y + diff_h - 70, "DeFi Contract = rsETH Bridge (release() 阻止)",
        ha="left", va="center", fontsize=11, color=TEXT_MUTED, fontweight="bold", zorder=6)
add_logo(f"{LOGO_DIR}/layerzero.png", (diff_x + diff_w - 46, diff_y + diff_h - 20), zoom=0.045)
add_logo(f"{LOGO_DIR}/kelpdao.png", (diff_x + diff_w - 18, diff_y + diff_h - 20), zoom=0.035)  # 256px 版 (旧 128px 時代は 0.07)

# ===== on-chain permanence note =====
ax.add_patch(FancyBboxPatch((1000, 300), 190, 62, boxstyle="round,pad=0,rounding_size=7",
                             linewidth=1.2, edgecolor="#86efac", facecolor="white", zorder=5))
ax.text(1095, 331, "π は ON-CHAIN に\n永続 (紛争時の証拠)", ha="center", va="center", fontsize=11,
        color="#065f46", fontweight="bold", zorder=6, linespacing=1.4)

plt.tight_layout(pad=1.0)
plt.savefig("/home/gohan/workspace/presentation-agent/public/images/poe_arch_static.png",
            facecolor=SURFACE, bbox_inches="tight")
print("saved. font used:", font_family)
