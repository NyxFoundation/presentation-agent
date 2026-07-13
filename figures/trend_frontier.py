# trend_frontier.py — S2-C 扉 (SL17): 2 系統の実用性変化グラフ
#
# 生成: uv run --with matplotlib python3 figures/trend_frontier.py
# 出力: public/images/trend_frontier_static.png
#
# 系統 A (Sumcheck 系 zkVM) と系統 B (MPC-in-the-head 系 / Longfellow) が
# 独立に立ち上がり、2024-26 に同時に production 域へ入る「2 つの革命」を 1 枚で。
# 細部のマイルストーン (PLONK / Lasso / Bumble 等) は SL18 / SL20 / SL21 側に譲る。

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trend_common import render_trend, AMBER, GREEN

OUT = "/home/gohan/workspace/presentation-agent/public/images/trend_frontier_static.png"

series = [
    {
        "name": "系統 A ・ Sumcheck 系 (汎用 zkVM)",
        "color": AMBER,
        "name_xy": (2018.4, 4.6),
        "points": [
            {"year": 2016, "y": 1.8, "label": "Groth16",
             "label_xy": (2016, 2.65),
             "sub": "回路書き直し + trusted setup が前提",
             "sub_xy": (2015.45, 1.0), "sub_ha": "left"},
            {"year": 2021, "y": 3.2},
            {"year": 2024, "y": 6.6, "label": "Jolt",
             "label_xy": (2024, 7.45), "logo": "a16z.png", "logo_xy": (2024, 8.5)},
            {"year": 2025.8, "y": 9.3, "label": "SP1 / zkVM 群",
             "label_xy": (2025.15, 10.35), "ha": "left",
             "logo": "succinct.png", "logo_xy": (2024.75, 10.35)},
        ],
    },
    {
        "name": "系統 B ・ MPC-in-the-head 系 (既存 ID)",
        "color": GREEN,
        "name_xy": (2019.4, 1.0),
        "points": [
            {"year": 2017, "y": 1.2, "label": "Ligero", "label_xy": (2017, 0.55)},
            {"year": 2023, "y": 3.4},
            {"year": 2024.9, "y": 5.4, "label": "Longfellow 論文",
             "label_xy": (2024.6, 4.55), "side": "down"},
            {"year": 2025.5, "y": 8.9, "label": "Google Wallet deploy",
             "label_xy": (2025.65, 7.95), "ha": "left",
             "sub": "→ OSS 化 ・ EUDI / IETF へ",
             "sub_xy": (2025.65, 7.3), "sub_ha": "left",
             "logo": "google.png", "logo_xy": (2028.35, 7.95)},
        ],
    },
]

render_trend(
    OUT,
    xlim=(2015.2, 2028.8),
    xticks=[2016, 2017, 2021, 2023, 2024, 2025, 2026],
    series=series,
    band_label_xy=(2028.6, 10.9),
)
