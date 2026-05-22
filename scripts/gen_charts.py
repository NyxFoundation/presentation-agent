#!/usr/bin/env python3
"""Generate chart PNGs for the SMBC日興セキュリティ部門講演 slide deck.

Outputs land in public/images/charts/ and are referenced from slides/SL*.md.
Re-run any time: /tmp/slidegen-venv/bin/python3 scripts/gen_charts.py
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "images" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

# Japanese font setup
JP_FONT_DIR = "/tmp/jpfont"
JP_REGULAR = f"{JP_FONT_DIR}/NotoSansJP-Regular.ttf"
JP_BOLD = f"{JP_FONT_DIR}/NotoSansJP-Bold.ttf"
font_manager.fontManager.addfont(JP_REGULAR)
font_manager.fontManager.addfont(JP_BOLD)
JP_FONT = "Noto Sans JP"

mpl.rcParams["font.family"] = JP_FONT
mpl.rcParams["font.size"] = 14
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["text.parse_math"] = False
mpl.rcParams["axes.spines.top"] = False
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["savefig.dpi"] = 220
mpl.rcParams["savefig.bbox"] = "tight"
mpl.rcParams["savefig.facecolor"] = "white"

INK = "#111111"
GREY = "#9aa0a6"
LIGHT = "#e5e7eb"
DANGER = "#b91c1c"
WARN = "#d97706"
SAFE = "#1f4e79"
GOLD = "#a16207"


def save(name: str):
    plt.savefig(OUT / name, bbox_inches="tight", pad_inches=0.25)
    plt.close()
    print(f"  wrote {OUT / name}")


def source_tag(ax, text, x=0.99, y=-0.10):
    """Standard small grey source tag at bottom-right of axes."""
    ax.text(x, y, text, transform=ax.transAxes, ha="right", va="top",
            fontsize=10, color=GREY, style="italic")


# ---------------------------------------------------------------------------
# 1. loss_trend.png — DeFi盗難総額 2022-2025 棒グラフ
# ---------------------------------------------------------------------------
def chart_loss_trend():
    years = ["2022", "2023", "2024", "2025"]
    loss = [3.8, 1.7, 2.2, 3.0]
    colors = [LIGHT, LIGHT, GREY, DANGER]
    fig, ax = plt.subplots(figsize=(10, 5.8))
    bars = ax.bar(years, loss, color=colors, edgecolor=INK, linewidth=0.8, width=0.55)
    for b, v in zip(bars, loss):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.10, f"${v:.1f}B",
                ha="center", va="bottom", fontsize=18, fontweight="bold", color=INK)
    ax.set_ylim(0, max(loss) * 1.45)
    ax.set_yticks([])
    ax.tick_params(axis="x", labelsize=18)
    ax.spines["left"].set_visible(False)
    ax.annotate("", xy=(3, 3.55), xytext=(2, 3.05),
                arrowprops=dict(arrowstyle="-|>", color=DANGER, lw=2.4))
    ax.text(2.5, 3.95, "前年比 +約50%", color=DANGER, fontsize=18, fontweight="bold",
            ha="center")
    source_tag(ax, "出典: Chainalysis / TRM Labs / DefiLlama 2026年集計値")
    save("loss_trend.png")


# ---------------------------------------------------------------------------
# 2. incident_compare.png — 監査会社・監査回数つき
# ---------------------------------------------------------------------------
def chart_incident_compare():
    incidents = [
        # name, $M, date, type, auditor, color
        ("KelpDAO / LayerZero", 292, "2026-04", "1-of-1 DVN 運用設定",
         "監査: Sherlock+Code4rena+Cyfrin (LayerZero)", DANGER),
        ("Cetus Protocol",       223, "2025-05", "桁あふれ",
         "監査: OtterSec + MoveBit (複数回)",            WARN),
        ("Radiant Capital",      53,  "2024-10", "Multisig (鍵管理) 侵害",
         "監査: BlockSec + Peckshield",                  GREY),
        ("Penpie",               27,  "2024-09", "再入攻撃 (Reentrancy)",
         "監査: Hacken + Salus + Otter (3社)",           GREY),
    ]
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    names = [f"{n}\n{d} ／ {t}\n{a}" for n, _, d, t, a, _ in incidents]
    losses = [v for _, v, _, _, _, _ in incidents]
    colors = [c for _, _, _, _, _, c in incidents]
    bars = ax.barh(names[::-1], losses[::-1], color=colors[::-1],
                    edgecolor=INK, linewidth=0.6)
    for b, v in zip(bars, losses[::-1]):
        ax.text(v + 6, b.get_y() + b.get_height() / 2,
                f"${v}M", va="center", fontsize=18, fontweight="bold", color=INK)
    ax.set_xlim(0, 380)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="y", labelsize=12)
    source_tag(ax, "出典: 各事件の公式ポストモーテム ／ rekt.news / 各監査会社公開レポート",
               x=0.99, y=-0.06)
    save("incident_compare.png")


# ---------------------------------------------------------------------------
# 3. cost_return.png — 攻撃者コスト vs リターン (実例多点プロット)
# ---------------------------------------------------------------------------
def chart_cost_return():
    x = np.linspace(0, 10, 400)
    linear = x
    nonlinear = 0.4 * np.exp(0.55 * x)
    nonlinear = np.minimum(nonlinear, 200)

    fig, ax = plt.subplots(figsize=(11.5, 6.4))
    ax.plot(x, linear, color=GREY, lw=2.2)
    ax.plot(x, nonlinear, color=DANGER, lw=3.4)
    ax.fill_between(x, linear, nonlinear, where=nonlinear > linear,
                    color=DANGER, alpha=0.07)

    # Three incident dots on the non-linear curve - place labels to avoid overlap
    incidents = [
        # (label, cost_x, anchor_x, anchor_y, ha)
        ("KelpDAO  $292M",  8.3,  6.6, 115, "right"),
        ("Cetus  $223M",    7.4,  4.9,  78, "right"),
        ("Penpie  $27M",    6.3,  3.5,  44, "right"),
    ]
    for label, cx, ax_x, ax_y, ha in incidents:
        cy = 0.4 * np.exp(0.55 * cx)
        ax.plot([cx], [cy], "o", color=DANGER, markersize=13, zorder=5)
        ax.annotate(label,
                    xy=(cx, cy), xytext=(ax_x, ax_y),
                    fontsize=13, fontweight="bold", color=DANGER,
                    ha=ha,
                    arrowprops=dict(arrowstyle="->", color=DANGER, lw=1.2))

    # Inline curve labels (small, on the line)
    ax.text(9.7, 11, "線形 (通常取引)", fontsize=11.5, color=GREY,
            ha="right", va="bottom", style="italic")
    ax.text(4.7, 30, "非線形 (脆弱性)", fontsize=12, color=DANGER,
            ha="left", va="bottom", fontweight="bold")

    ax.set_xlabel("攻撃者の支払うコスト →", fontsize=16, fontweight="bold")
    ax.set_ylabel("攻撃者の得るリターン →", fontsize=16, fontweight="bold")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 135)
    ax.set_xticks([])
    ax.set_yticks([])
    source_tag(ax, "出典: 各事件公式ポストモーテム ／ コスト・リターン値は概念図 (相対関係)",
               y=-0.10)
    save("cost_return.png")


# ---------------------------------------------------------------------------
# 4. bounty_economy.png — 同じバグを見つけたとき、誰が何を得るか (リターン比較)
# ---------------------------------------------------------------------------
def chart_bounty_economy():
    """Returns comparison: 4 bars on log scale.
    Hacker exploit / Audit firm fee / Researcher High median / Bug payout actual."""
    labels = [
        "Current Finance\n(2件報告の実報酬)",
        "リサーチャー\n(Sherlock High 中央値)",
        "監査会社\n(標準監査単価)",
        "ハッカー\n(1件のエクスプロイト平均)",
    ]
    values = [27, 150_000, 30_000_000, 300_000_000]
    colors = [DANGER, WARN, SAFE, "#7c1d1d"]
    notes = [
        "¥27",
        "≈ ¥15万",
        "≈ ¥3,000万",
        "≈ ¥3億",
    ]

    fig, ax = plt.subplots(figsize=(13, 5.4))
    bars = ax.bar(labels, values, color=colors, edgecolor=INK, linewidth=0.7, width=0.55)
    ax.set_yscale("log")
    ax.set_ylim(1, 3e9)
    ax.set_yticks([1, 100, 10_000, 1_000_000, 100_000_000])
    ax.set_yticklabels(["¥1", "¥100", "¥1万", "¥100万", "¥1億"], fontsize=12)
    ax.tick_params(axis="x", labelsize=12.5)
    for b, v, note in zip(bars, values, notes):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.9, note,
                ha="center", va="bottom", fontsize=15, fontweight="bold", color=INK)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    ax.set_title("同じ脆弱性を見つけたとき、誰がいくらを得るか",
                 fontsize=15, fontweight="bold", color=INK, pad=14)
    source_tag(ax,
        "出典: ハッカー = Chainalysis 2025 個別事件中央値 / 監査単価 = ChainSecurity・Trail of Bits 公開価格帯 / Sherlock contest 公開判定書 (2024-25)",
        x=0.99, y=-0.16)
    save("bounty_economy.png")


# ---------------------------------------------------------------------------
# 4b. researcher_penalties.png — Bug Bounty経済の研究者ペナルティ構造
# ---------------------------------------------------------------------------
def chart_researcher_penalties():
    """Three penalty mechanics that push researchers away from honest reporting."""
    fig, ax = plt.subplots(figsize=(13, 4.4))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 4.4)
    ax.axis("off")

    items = [
        # x_center, header, body, footnote, color
        (2.2, "報告コスト",
         "1件報告するのに\n¥36,000 を担保預入",
         "Stake-to-submit (2025-06 制度変更)\n判定無効なら没収", WARN),
        (6.5, "凍結ペナルティ",
         "「有効率」が閾値を割ると\n過去の賞金まで凍結",
         "Sherlock 利用規約 §4.3", DANGER),
        (10.8, "結果",
         "確実に通る報告しか出さない\n方向に研究者を誘導",
         "= 萎縮効果", "#7c1d1d"),
    ]
    for cx, header, body, foot, color in items:
        ax.add_patch(FancyBboxPatch((cx - 1.8, 0.6), 3.6, 3.3,
                                     boxstyle="round,pad=0.05",
                                     facecolor=color, alpha=0.10, edgecolor=color, lw=2.0))
        ax.text(cx, 3.40, header, ha="center", fontsize=13.5,
                fontweight="bold", color=color)
        ax.text(cx, 2.30, body, ha="center", va="center", fontsize=12.5,
                color=INK)
        ax.text(cx, 0.95, foot, ha="center", va="center", fontsize=10.5,
                color=GREY, style="italic")

    # Arrows between
    for ax_start, ax_end in [(4.05, 4.65), (8.35, 8.95)]:
        ax.annotate("", xy=(ax_end, 2.25), xytext=(ax_start, 2.25),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.0))
    save("researcher_penalties.png")


# ---------------------------------------------------------------------------
# 5. vuln_map.png — 同心円: 内側=監査が届く / 外側=届かない、被害額で大きさ
# ---------------------------------------------------------------------------
def chart_vuln_map():
    """Whole canvas = 監査(ソースコード監査)が届かない領域.
    Inner safe zone = 監査が届く領域 (larger, holds 3 named categories).
    Outer red zone = ソースコード監査では原理的に届かない (with 2 bubbles for C/E)."""
    from matplotlib.patches import Wedge

    fig, ax = plt.subplots(figsize=(16, 7.6))
    ax.set_xlim(-11.5, 11.5)
    ax.set_ylim(-5.4, 5.8)
    ax.set_aspect("equal")
    ax.axis("off")

    outer_r = 5.0
    inner_r = 3.2
    # Whole inner outer area = audit-unreachable
    ax.add_patch(Wedge((0, 0), outer_r, 0, 360, width=outer_r - inner_r,
                       facecolor=DANGER, alpha=0.09,
                       edgecolor=DANGER, lw=2.0, linestyle="--"))
    # Inner safe zone — bigger to fit category names
    ax.add_patch(plt.Circle((0, 0), inner_r, facecolor=SAFE,
                             alpha=0.13, edgecolor=SAFE, lw=2.0))

    # Top zone label — clarifies "ソースコード監査"
    ax.text(0, outer_r + 0.55, "ソースコード監査が原理的に届かない領域",
            ha="center", fontsize=22, fontweight="bold", color=DANGER)

    # Inner zone label
    ax.text(0,  2.20, "監査が届く領域",
            ha="center", va="center", fontsize=17, fontweight="bold", color=SAFE)

    # Inner: 3 named categories — name + example on same line, centered
    inner_items = [
        ("価格操作",     "(Mango ~$0.8B)",      1.10),
        ("精度・丸め",    "(Cetus ~$0.5B)",      0.20),
        ("ロジック整合", "(Current Finance ~$0.3B)",    -0.70),
    ]
    for name, ex, y in inner_items:
        ax.text(0, y + 0.18, name, ha="center", va="center",
                fontsize=14, color=SAFE, fontweight="bold")
        ax.text(0, y - 0.22, ex, ha="center", va="center",
                fontsize=10, color=SAFE)

    ax.text(0, -2.10, "累計  ~$1.6B",
            ha="center", va="center", fontsize=13, fontweight="bold", color=SAFE)

    # Outer ring bubbles — place wider apart to clear inner zone
    outer_items = [
        ("運用・\nデプロイ系",   "KelpDAO\n~$1.4B",                  -6.30, 0.0),
        ("経済\nモデル系",        "Terra-Luna\n~$40B 時価消失",        6.30, 0.0),
    ]
    bubble_r = 1.30

    for name, ex, x, y in outer_items:
        ax.add_patch(plt.Circle((x, y), bubble_r, facecolor=DANGER,
                                 alpha=0.90, edgecolor=DANGER, lw=2.0))
        ax.text(x, y, name, ha="center", va="center",
                fontsize=14, color="white", fontweight="bold")
        ax.text(x, y - bubble_r - 0.45, ex, ha="center", va="top",
                fontsize=12.5, color=DANGER, fontweight="bold")

    save("vuln_map.png")


# ---------------------------------------------------------------------------
# 6. timeline_speca.png
# ---------------------------------------------------------------------------
def chart_timeline_speca():
    fig, ax = plt.subplots(figsize=(12, 3.6))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.plot([0.8, 11.2], [2.5, 2.5], color=INK, lw=2.2)

    ax.plot(1.8, 2.5, "o", color=SAFE, markersize=22, zorder=3)
    ax.text(1.8, 4.4, "2025-10-31", ha="center", fontsize=13, color=SAFE, fontweight="bold")
    ax.text(1.8, 3.9, "Code4rena/LayerZero DVN", ha="center", fontsize=11, color=INK)
    ax.text(1.8, 3.5, "Starknet ワーカーコンテスト", ha="center", fontsize=10, color=GREY)
    ax.text(1.8, 1.5, "ジャッジ判定", ha="center", fontsize=11, color=GREY)
    ax.text(1.8, 1.0, "「これは脆弱性ではない」", ha="center", fontsize=12.5,
            color=DANGER, fontweight="bold", style="italic")

    ax.annotate("", xy=(10, 2.5), xytext=(2.6, 2.5),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.6))
    ax.text(6.3, 2.85, "5.5ヶ月の静寂", ha="center", fontsize=15,
            color=GREY, fontweight="bold")
    ax.text(6.3, 2.20, "(類似報告0件・対策アナウンス無し)",
            ha="center", fontsize=10, color=GREY, style="italic")

    ax.plot(10.6, 2.5, "o", color=DANGER, markersize=28, zorder=3)
    ax.text(10.6, 4.4, "2026-04-18", ha="center", fontsize=13, color=DANGER, fontweight="bold")
    ax.text(10.6, 3.9, "KelpDAO / LayerZero", ha="center", fontsize=12, color=INK)
    ax.text(10.6, 3.5, "rsETH リステーキング攻撃", ha="center", fontsize=10, color=GREY)
    ax.text(10.6, 1.5, "流出額", ha="center", fontsize=11, color=GREY)
    ax.text(10.6, 0.85, "$292M (約450億円)", ha="center", fontsize=15,
            color=DANGER, fontweight="bold")
    save("timeline_speca.png")


# ---------------------------------------------------------------------------
# 7. defense_layers.png — 3層 + 被害シェア
# ---------------------------------------------------------------------------
def chart_defense_layers():
    fig, ax = plt.subplots(figsize=(13.5, 7))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 7)
    ax.axis("off")

    layers = [
        # name, sub, y, color, note, share
        ("コード層",              "ロジック・実装",
         0.6, SAFE,   "AI + 監査で守れる",            "15%"),
        ("経済モデル層",          "インセンティブ・流動性",
         2.5, WARN,   "経済シミュレーションで部分的に",  "25%"),
        ("運用・統制・ガバナンス層", "鍵管理・職務分掌・デプロイ設定",
         4.4, DANGER, "AIも監査も届かない／組織統制の領域", "60%"),
    ]
    for name, sub, y, color, note, share in layers:
        ax.add_patch(FancyBboxPatch((0.6, y), 7.4, 1.6,
                                     boxstyle="round,pad=0.04",
                                     facecolor=color, alpha=0.13,
                                     edgecolor=color, lw=2))
        ax.text(0.95, y + 1.10, name, fontsize=19, fontweight="bold", color=color)
        ax.text(0.95, y + 0.55, sub, fontsize=12.5, color=INK, alpha=0.78)
        # share callout
        ax.text(8.25, y + 1.10, share, fontsize=22, fontweight="bold", color=color,
                ha="left")
        ax.text(8.25, y + 0.50, "2024-25 被害シェア", fontsize=10, color=GREY)
        # note far right
        ax.text(10.4, y + 0.80, note, fontsize=12.5, color=color, fontweight="bold",
                va="center")
    ax.text(0.6, 6.5, "DeFi 防衛 3層モデル", fontsize=18, fontweight="bold", color=INK)
    ax.text(7.9, -0.05,
            "出典: 被害シェアは Chainalysis Crypto Crime Report 2025 + rekt.news 集計の概算配分",
            fontsize=10, color=GREY, style="italic", ha="center")
    save("defense_layers.png")


# ---------------------------------------------------------------------------
# 8. domain_separation.png — 詳細化版
# ---------------------------------------------------------------------------
def chart_domain_separation():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def branch_box(x, label, sub, color):
        ax.add_patch(FancyBboxPatch((x - 1.5, 2.0), 3.0, 2.4,
                                     boxstyle="round,pad=0.05",
                                     facecolor="white", edgecolor=color, lw=2.2))
        ax.text(x, 4.1, label, ha="center", fontsize=16, fontweight="bold", color=color)
        ax.text(x, 3.7, sub, ha="center", fontsize=11, color=GREY)
        ax.add_patch(plt.Circle((x, 2.85), 0.34, fill=False, color=DANGER, lw=2.4))
        ax.text(x, 2.85, "印", ha="center", va="center", fontsize=20, color=DANGER, fontweight="bold")
        ax.text(x, 2.25, "署名 0x4a8f…e2", ha="center", fontsize=10.5, color=GREY)

    branch_box(2.2, "東京支店", "海外送金決裁", SAFE)
    branch_box(9.8, "NY 支店", "別の送金で再利用", SAFE)

    ax.annotate("", xy=(8.4, 2.85), xytext=(3.6, 2.85),
                arrowprops=dict(arrowstyle="-|>", color=DANGER, lw=2.6))
    ax.text(6.0, 3.30, "同じ印影 (署名) がそのまま通用", ha="center",
            fontsize=15, color=DANGER, fontweight="bold")
    ax.text(6.0, 2.55, "→ どの拠点・どの取引かを示す情報が刻まれていない",
            ha="center", fontsize=12, color=INK, alpha=0.85)

    ax.text(6.0, 1.0,
            "DeFi用語: ドメイン分離欠如／ナンス・スコープ未組込\n業務用語: アクセス制御スコープ未分離／副署なき特権ID",
            ha="center", fontsize=12.5, color=INK, alpha=0.9,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#fef3c7", edgecolor=GOLD, lw=1.4))
    save("domain_separation.png")


# ---------------------------------------------------------------------------
# 9. world_compare.png — 法令アンカーつき
# ---------------------------------------------------------------------------
def chart_world_compare():
    rows = [
        ("動かす主体",       "人間 + システム",                 "プログラムだけ"),
        ("コードの公開範囲",  "社内 (機密)",                    "全世界に公開"),
        ("間違えた時",       "訂正できる (会計訂正)",            "取り消せない (オンチェーン確定)"),
        ("監督官庁・基準",   "金融庁 / 金商法 / FISC",            "監督官庁なし (DAO 自治)"),
        ("攻撃者の試行回数", "限定的 (内部NW)",                  "無限 (24/365 公開)"),
    ]
    fig, ax = plt.subplots(figsize=(15, 6.4))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, len(rows) + 1.3)
    ax.axis("off")
    ax.text(5.0, len(rows) + 0.6, "皆様の世界", ha="center",
            fontsize=18, fontweight="bold", color=SAFE)
    ax.text(11.4, len(rows) + 0.6, "DeFi の世界", ha="center",
            fontsize=18, fontweight="bold", color=DANGER)

    label_right_x = 2.85
    left_box_x = 3.10
    left_box_w = 3.90
    right_box_x = 8.80
    right_box_w = 4.60

    for i, (label, left, right) in enumerate(rows):
        y = len(rows) - i - 0.4
        # Right-aligned label so it never bleeds into the box
        ax.text(label_right_x, y, label, fontsize=13.5, color=INK,
                fontweight="bold", va="center", ha="right")
        ax.add_patch(FancyBboxPatch((left_box_x, y - 0.32), left_box_w, 0.64,
                                     boxstyle="round,pad=0.04",
                                     facecolor=SAFE, alpha=0.10, edgecolor=SAFE, lw=1.4))
        ax.text(left_box_x + left_box_w / 2, y, left,
                ha="center", va="center", fontsize=12, color=SAFE)
        ax.add_patch(FancyBboxPatch((right_box_x, y - 0.32), right_box_w, 0.64,
                                     boxstyle="round,pad=0.04",
                                     facecolor=DANGER, alpha=0.10, edgecolor=DANGER, lw=1.4))
        ax.text(right_box_x + right_box_w / 2, y, right,
                ha="center", va="center", fontsize=12, color=DANGER,
                fontweight="bold")
    save("world_compare.png")


# ---------------------------------------------------------------------------
# 10. governance_bridge.png — ITGC/FISC コントロール番号つき
# ---------------------------------------------------------------------------
def chart_governance_bridge():
    pairs = [
        ("1-of-1 DVN (1人承認)",
         "副署なき特権ID／4-eyes 欠如",
         "J-SOX ITGC-CC02 ／ FISC 統97"),
        ("RPC 内部侵害",
         "特権アカウント侵害／アクセス管理",
         "J-SOX ITGC-CC04 ／ FISC 統83"),
        ("デプロイ設定の不備",
         "IT全般統制 設定不備",
         "J-SOX ITGC-CC05 ／ FISC 統120"),
    ]
    fig, ax = plt.subplots(figsize=(13.5, 5.0))
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, len(pairs) + 1.3)
    ax.axis("off")
    ax.text(2.6, len(pairs) + 0.55, "DeFi 失敗様式", ha="center",
            fontsize=17, fontweight="bold", color=DANGER)
    ax.text(7.0, len(pairs) + 0.55, "皆様の統制カテゴリ", ha="center",
            fontsize=17, fontweight="bold", color=SAFE)
    ax.text(11.4, len(pairs) + 0.55, "該当する統制番号 (例)", ha="center",
            fontsize=17, fontweight="bold", color=GOLD)
    for i, (l, m, r) in enumerate(pairs):
        y = len(pairs) - i - 0.5
        ax.add_patch(FancyBboxPatch((0.4, y - 0.36), 4.4, 0.72,
                                     boxstyle="round,pad=0.04",
                                     facecolor=DANGER, alpha=0.10, edgecolor=DANGER, lw=1.4))
        ax.text(2.6, y, l, ha="center", va="center", fontsize=14, color=DANGER,
                fontweight="bold")
        ax.text(4.95, y, "↔", ha="center", va="center", fontsize=24, color=GOLD,
                fontweight="bold")
        ax.add_patch(FancyBboxPatch((5.15, y - 0.36), 3.7, 0.72,
                                     boxstyle="round,pad=0.04",
                                     facecolor=SAFE, alpha=0.10, edgecolor=SAFE, lw=1.4))
        ax.text(7.0, y, m, ha="center", va="center", fontsize=13, color=SAFE,
                fontweight="bold")
        ax.add_patch(FancyBboxPatch((9.2, y - 0.36), 4.0, 0.72,
                                     boxstyle="round,pad=0.04",
                                     facecolor=GOLD, alpha=0.08, edgecolor=GOLD, lw=1.4))
        ax.text(11.2, y, r, ha="center", va="center", fontsize=12, color=GOLD,
                fontweight="bold")
    save("governance_bridge.png")


# ---------------------------------------------------------------------------
# 11. dvn_compare.png — 1-of-1 vs M-of-N (現状残置)
# ---------------------------------------------------------------------------
def chart_dvn_compare():
    fig, ax = plt.subplots(figsize=(11.5, 5.4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(3.0, 4.6, "KelpDAO の運用設定", ha="center", fontsize=16,
            fontweight="bold", color=DANGER)
    ax.add_patch(FancyBboxPatch((1.4, 1.5), 3.2, 2.3,
                                 boxstyle="round,pad=0.05",
                                 facecolor=DANGER, alpha=0.10, edgecolor=DANGER, lw=2.2))
    ax.add_patch(plt.Circle((3.0, 2.7), 0.55, color=DANGER, alpha=0.8))
    ax.text(3.0, 2.7, "1", ha="center", va="center", fontsize=28,
            color="white", fontweight="bold")
    ax.text(3.0, 1.85, "1人の検証者が承認 = 流出", ha="center", fontsize=12,
            color=DANGER, fontweight="bold")

    ax.text(9.0, 4.6, "推奨設定 (M-of-N)", ha="center", fontsize=16,
            fontweight="bold", color=SAFE)
    ax.add_patch(FancyBboxPatch((7.4, 1.5), 3.2, 2.3,
                                 boxstyle="round,pad=0.05",
                                 facecolor=SAFE, alpha=0.10, edgecolor=SAFE, lw=2.2))
    for cx in [8.2, 9.0, 9.8]:
        ax.add_patch(plt.Circle((cx, 2.7), 0.32, color=SAFE, alpha=0.85))
    ax.text(9.0, 1.85, "複数検証者の副署で承認", ha="center", fontsize=12,
            color=SAFE, fontweight="bold")

    ax.text(6.0, 0.55, "皆様の用語: 1-of-1 = 4-eyes 欠如 ／ 副署なき特権ID",
            ha="center", fontsize=14, color=GOLD, fontweight="bold")
    save("dvn_compare.png")


# ---------------------------------------------------------------------------
# 12. roadmap_6.png — 本日の地図
# ---------------------------------------------------------------------------
def chart_roadmap_6():
    points = [
        "監査+バウンティの二本柱が崩壊しつつある",
        "脆弱性 = コストとリターンの非対称な経路",
        "バウンティ経済も研究者にペナルティ方向に逆行",
        "「デプロイ設定」と却下されるバグが現実化(SPECA → KelpDAO)",
        "AI が守れるのは『コード層 + 経済層』まで",
        "『運用・統制・ガバナンス層』は、伝統金融の内部統制と地続き",
    ]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, len(points) + 0.5)
    ax.axis("off")
    for i, p in enumerate(points):
        y = len(points) - i - 0.4
        color = SAFE if i < 4 else GOLD
        ax.add_patch(plt.Circle((0.8, y), 0.32, color=color))
        ax.text(0.8, y, str(i + 1), ha="center", va="center",
                fontsize=14, color="white", fontweight="bold")
        ax.text(1.5, y, p, va="center", fontsize=15, color=INK)
    save("roadmap_6.png")


# ---------------------------------------------------------------------------
# 13. NEW: maturity_timeline.png — 20年先の根拠(J-SOX/FISC vs DeFi)
# ---------------------------------------------------------------------------
def chart_maturity_timeline():
    fig, ax = plt.subplots(figsize=(14, 5.6))
    ax.set_xlim(1980, 2030)
    ax.set_ylim(-0.5, 4)
    ax.axis("off")

    # Two horizontal lanes
    ax.plot([1980, 2029], [3.0, 3.0], color=SAFE, lw=2.4)
    ax.plot([1980, 2029], [1.2, 1.2], color=DANGER, lw=2.4)
    ax.text(1981, 3.55, "伝統金融 ─ 内部統制の整備",
            fontsize=14, fontweight="bold", color=SAFE)
    ax.text(1981, 0.65, "DeFi業界 ─ 主要インシデント",
            fontsize=14, fontweight="bold", color=DANGER)

    # Top lane events — 3 anchors only
    top = [
        (1985, "FISC安全対策基準\n初版"),
        (2008, "金融商品取引法\n(J-SOX) 施行"),
        (2022, "FISC v9 改訂"),
    ]
    for x, label in top:
        ax.plot(x, 3.0, "o", color=SAFE, markersize=14, zorder=5)
        ax.text(x, 2.50, label, ha="center", fontsize=11, color=INK)

    # Bottom lane events — only verifiable data points, well-separated
    bot = [
        (2020, "DeFi夏\n(TVL急増)"),
        (2026, "KelpDAO\n$292M"),
    ]
    for x, label in bot:
        ax.plot(x, 1.2, "o", color=DANGER, markersize=14, zorder=5)
        ax.text(x, 0.65, label, ha="center", va="top", fontsize=11, color=INK)

    # The gap arrow
    ax.annotate("", xy=(2026, 1.85), xytext=(2008, 1.85),
                arrowprops=dict(arrowstyle="<->", color=GOLD, lw=2.2,
                                connectionstyle="arc3,rad=-0.0"))
    ax.text(2017, 2.05, "= 約18年のギャップ", ha="center", fontsize=15,
            color=GOLD, fontweight="bold")

    save("maturity_timeline.png")


# ---------------------------------------------------------------------------
# 14. NEW: kelpdao_flow.png — KelpDAO攻撃フロー
# ---------------------------------------------------------------------------
def chart_kelpdao_flow():
    fig, ax = plt.subplots(figsize=(14, 4.2))
    ax.set_xlim(0, 13)
    ax.set_ylim(0.2, 5.2)
    ax.axis("off")

    def step_box(x, title, sub, color):
        ax.add_patch(FancyBboxPatch((x - 1.85, 1.4), 3.7, 3.2,
                                     boxstyle="round,pad=0.05",
                                     facecolor=color, alpha=0.12, edgecolor=color, lw=2.0))
        ax.text(x, 4.10, title, ha="center", fontsize=17, fontweight="bold", color=color)
        ax.text(x, 2.55, sub, ha="center", fontsize=13, color=INK, va="center")

    step_box(2.4, "① 内部RPC侵害",
             "LayerZero 内部の\nRPC ノードを掌握", DANGER)
    step_box(6.5, "② 外部DDoS",
             "正規 RPC を停止 →\n切替を強制", WARN)
    step_box(10.6, "③ 偽署名で送金",
             "1-of-1 DVN ─ 1つの\n偽署名で承認成立", DANGER)

    for x_start, x_end in [(4.30, 4.60), (8.40, 8.70)]:
        ax.annotate("", xy=(x_end, 2.95), xytext=(x_start, 2.95),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.2))

    save("kelpdao_flow.png")


# ---------------------------------------------------------------------------
# 15. NEW: kelpdao_audit_history.png — Cetus 監査履歴
# ---------------------------------------------------------------------------
def chart_cetus_audit_history():
    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    ax.axis("off")

    # Timeline of audits leading up to incident
    ax.plot([0.8, 11.2], [2.0, 2.0], color=INK, lw=2.0)
    events = [
        (1.5, "2023-Q4", "OtterSec\n初回監査", SAFE),
        (3.5, "2024-Q2", "MoveBit\n追加監査", SAFE),
        (5.5, "2024-Q4", "OtterSec\n再監査", SAFE),
        (7.5, "2025-Q1", "内部 fuzz\nテスト追加", SAFE),
        (10.5, "2025-05-22", "$223M 流出\n(30分・桁あふれ)", DANGER),
    ]
    for x, date, label, color in events:
        ax.plot(x, 2.0, "o", color=color, markersize=18 if color == DANGER else 14, zorder=4)
        ax.text(x, 2.6, date, ha="center", fontsize=10, color=color, fontweight="bold")
        ax.text(x, 1.3, label, ha="center", fontsize=10.5, color=INK, va="top")

    ax.text(6, 3.9, "Cetus の監査履歴: 複数監査会社・複数回監査の後でも見逃した",
            ha="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(6, 0.2,
            "出典: OtterSec/MoveBit 公開レポート ／ Cetus 公式ポストモーテム (2025-05-23)",
            ha="center", fontsize=9.5, color=GREY, style="italic")
    save("cetus_audit_history.png")


if __name__ == "__main__":
    print(f"writing charts to {OUT}")
    chart_loss_trend()
    chart_incident_compare()
    chart_cost_return()
    chart_bounty_economy()
    chart_researcher_penalties()
    chart_vuln_map()
    chart_timeline_speca()
    chart_defense_layers()
    chart_domain_separation()
    chart_world_compare()
    chart_governance_bridge()
    chart_dvn_compare()
    chart_roadmap_6()
    chart_maturity_timeline()
    chart_kelpdao_flow()
    chart_cetus_audit_history()
    print("done.")
