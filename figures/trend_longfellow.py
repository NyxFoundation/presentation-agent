# trend_longfellow.py — 系統 B (SL21): Longfellow / MPC-in-the-head 系の実用性変化グラフ
#
# 生成: uv run --with matplotlib python3 figures/trend_longfellow.py
# 出力: public/images/trend_longfellow_static.png
#
# Ligero (2017 理論) → Longfellow 論文 (2024) → Google Wallet deploy / OSS 化 →
# Bumble 稼働 → EUDI / IETF 標準化へ。既存 ID を壊さないから立ち上がりが速い、
# という社会実装ナラティブを 1 本の曲線で見せる。

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trend_common import render_trend, GREEN

OUT = "/home/gohan/workspace/presentation-agent/public/images/trend_longfellow_static.png"

series = [
    {
        "name": "MPC-in-the-head 系",
        "color": GREEN,
        "points": [
            {"year": 2017, "y": 1.8, "label": "Ligero",
             "label_xy": (2017, 2.65),
             "sub": "MPC-in-the-head の理論", "sub_xy": (2017.05, 1.0), "sub_ha": "left"},
            {"year": 2022, "y": 3.0},
            {"year": 2024.9, "y": 5.4, "label": "Longfellow 論文",
             "label_xy": (2025.3, 4.7), "ha": "left",
             "sub": "既存の mDOC / JWT をそのまま ZK 化",
             "sub_xy": (2025.3, 4.05), "sub_ha": "left"},
            {"year": 2025.3, "y": 8.6, "label": "Google Wallet deploy",
             "label_xy": (2024.5, 9.5),
             "sub": "OSS 化 ・ Sparkasse 提携 (2025/7)", "sub_xy": (2024.5, 10.15),
             "logo": "google.png", "logo_xy": (2022.3, 9.6)},
            {"year": 2026.0, "y": 9.3, "label": "Bumble 認証稼働",
             "label_xy": (2026.6, 8.6), "ha": "left",
             "logo": "bumble.png", "logo_xy": (2028.9, 8.6)},
            {"year": 2026.8, "y": 9.9, "label": "EUDI / IETF 標準化へ",
             "label_xy": (2027.2, 10.05), "ha": "left"},
        ],
    },
]

render_trend(
    OUT,
    xlim=(2016, 2030.5),
    xticks=[2017, 2022, 2024, 2025, 2026],
    series=series,
    band_label_xy=(2016.4, 10.9), band_label_ha="left",
)
