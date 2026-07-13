# trend_commit.py — 共通の補強 (SL20): コミットメントと folding の実用性変化グラフ
#
# 生成: uv run --with matplotlib python3 figures/trend_commit.py
# 出力: public/images/trend_commit_static.png
#
# 上 = コミットメント (KZG → FRI → Brakedown → BaseFold/Binius/WHIR → Stwo mainnet)、
# 下 = folding / IVC (Halo → Nova → HyperNova/ProtoStar → LatticeFold+)。
# 青が常に紫の上に来るよう y を設計し、ラベルは青=上側 / 紫=下側で固定する。

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trend_common import render_trend, BLUE, PURPLE

OUT = "/home/gohan/workspace/presentation-agent/public/images/trend_commit_static.png"

series = [
    {
        "name": "コミットメント",
        "color": BLUE,
        "name_xy": (2010.5, 5.6),
        "points": [
            {"year": 2010, "y": 2.4, "label": "KZG",
             "label_xy": (2010, 3.25),
             "sub": "pairing ・ trusted setup", "sub_xy": (2009.35, 1.55), "sub_ha": "left"},
            {"year": 2017, "y": 4.4, "label": "FRI",
             "label_xy": (2017, 5.25),
             "sub": "hash ・ transparent", "sub_xy": (2017, 5.9)},
            {"year": 2023, "y": 6.4, "label": "Brakedown",
             "label_xy": (2022.5, 7.2)},
            {"year": 2024.3, "y": 7.8, "label": "BaseFold / Binius / WHIR",
             "label_xy": (2022.9, 8.8), "ha": "center"},
            {"year": 2025.5, "y": 9.3, "label": "Stwo ・ Starknet mainnet",
             "label_xy": (2026.0, 9.4), "ha": "left",
             "logo": "starknet.png", "logo_xy": (2025.5, 10.45)},
        ],
    },
    {
        "name": "folding / IVC",
        "color": PURPLE,
        "name_xy": (2013.0, 1.0),
        "points": [
            {"year": 2020, "y": 1.8, "label": "Halo",
             "label_xy": (2020, 0.95), "side": "down"},
            {"year": 2022, "y": 3.6, "label": "Nova",
             "label_xy": (2022, 2.75), "side": "down"},
            {"year": 2023.6, "y": 5.2, "label": "HyperNova / ProtoStar",
             "label_xy": (2024.2, 4.35), "side": "down"},
            {"year": 2025, "y": 7.4, "label": "LatticeFold+",
             "label_xy": (2026.0, 7.0), "ha": "left",
             "sub": "格子ベース ・ 耐量子へ", "sub_xy": (2026.0, 6.35), "sub_ha": "left"},
        ],
    },
]

render_trend(
    OUT,
    xlim=(2009, 2030.5),
    xticks=[2010, 2017, 2020, 2022, 2024, 2026],
    series=series,
    band_label_xy=(2009.4, 10.9), band_label_ha="left",
)
