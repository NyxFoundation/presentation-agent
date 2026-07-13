# trend_sumcheck.py — 系統 A (SL18): Sumcheck 系の実用性変化グラフ
#
# 生成: uv run --with matplotlib python3 figures/trend_sumcheck.py
# 出力: public/images/trend_sumcheck_static.png
#
# 1992 年の理論 (LFKN) が 21 年眠り、Thaler 2013 → Lasso 2023 → Jolt 2024 →
# zkVM 群 production という立ち上がりを実年軸で見せる。技術の中身は
# speaker notes と SL19 (Jolt) に譲る。

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trend_common import render_trend, AMBER

OUT = "/home/gohan/workspace/presentation-agent/public/images/trend_sumcheck_static.png"

series = [
    {
        "name": "Sumcheck 系",
        "color": AMBER,
        "points": [
            {"year": 1992, "y": 1.5, "label": "Sumcheck (LFKN)",
             "label_xy": (1991.2, 2.35), "ha": "left",
             "sub": "対話証明の理論", "sub_xy": (1991.2, 0.8), "sub_ha": "left"},
            {"year": 2013, "y": 3.0, "label": "Thaler 2013",
             "label_xy": (2013, 3.85),
             "sub": "structured ME 上で concretely efficient",
             "sub_xy": (2013, 2.2)},
            {"year": 2023, "y": 5.5, "label": "Lasso",
             "label_xy": (2022.6, 6.3),
             "sub": "lookup argument", "sub_xy": (2022.2, 4.35)},
            {"year": 2024.5, "y": 7.3, "label": "Jolt",
             "label_xy": (2023.7, 7.75), "logo": "a16z.png", "logo_xy": (2023.7, 8.75)},
            {"year": 2026, "y": 9.4, "label": "zkVM 群が production へ",
             "label_xy": (2026.7, 9.5), "ha": "left",
             "sub": "SP1 ・ RISC0 ・ Jolt", "sub_xy": (2026.7, 8.85), "sub_ha": "left",
             "logo": "succinct.png", "logo_xy": (2027.5, 10.4)},
        ],
    },
]

render_trend(
    OUT,
    xlim=(1990.5, 2032.5),
    xticks=[1992, 2013, 2023, 2026],
    series=series,
    band_label_xy=(1991.0, 10.9), band_label_ha="left",
    annotations=[
        {"xy": (2002.5, 2.9), "text": "理論のまま 21 年", "fontsize": 14,
         "color": "#9ca3af"},
    ],
)
