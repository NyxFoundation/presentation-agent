#!/usr/bin/env python3
"""Generate the SL11b Japan map SVG with case-city pins + leader-line callouts.

Reads the Geolonia prefecture SVG, recolors it, highlights the four relevant
prefectures, and overlays five city pins. Each pin has a leader line that
hooks out to a callout block (city + brief case description) in the side
margins of the extended viewBox.
"""
import re
from pathlib import Path

SRC = Path("/home/gohan/workspace/presentation-agent/public/images/japan-map.svg")
OUT = Path("/home/gohan/workspace/presentation-agent/public/images/sl11b_map.svg")

BG = "#faf9f5"
BG_2 = "#f3f1ea"
LINE = "#cfcdc6"
INK = "#18181a"
INK_DIM = "#55524c"
ACCENT = "#1f3a52"
ACCENT_SOFT = "#e8edf2"
SEVERE = "#a25434"
SEVERE_SOFT = "#f0e2db"

HIGHLIGHT_PREFS = {
    "hokkaido": SEVERE_SOFT,
    "toyama":   ACCENT_SOFT,
    "tokyo":    SEVERE_SOFT,
    "chiba":    SEVERE_SOFT,
}

# Extended viewBox: keep the full Geolonia 0..1000 map space and add margins
# for callout text on left and right.
VB_LEFT, VB_RIGHT = -460, 1460   # width 1920
VB_TOP,  VB_BOT   = -20,  980    # height 1000 (≈ 1.92:1)

# Pin coordinates in the original Geolonia viewBox (0 0 1000 1000),
# tuned visually against the rendered prefecture shapes.
PINS = {
    "yubari":    (720, 200),
    "utashinai": (700, 170),
    "choshi":    (662, 654),
    "tama":      (580, 668),
    "nanto":     (462, 605),
}

# Callouts. Each has a pin, a side ('L', 'R', 'B'), and text content.
# tx = the *map-facing* edge of the text block (where the leader meets the text).
CALLOUTS = [
    {
        "pin": "utashinai", "side": "L",
        "tx": -20, "ty": 140,
        "place": "歌志内市（北海道）",
        "fact": "産業転換に失敗。\n最盛期の 約 5 % まで縮小。",
        "severe": True,
    },
    {
        "pin": "yubari", "side": "R",
        "tx": 1020, "ty": 260,
        "place": "夕張市（北海道）",
        "fact": "観光ハコモノで規模を追い、\n2007 年 財政破綻。",
        "severe": True,
    },
    {
        "pin": "tama", "side": "L",
        "tx": -20, "ty": 720,
        "place": "多摩ニュータウン",
        "fact": "規模で集めた世代が高齢化、\n空室と孤立が並走。",
        "severe": True,
    },
    {
        "pin": "choshi", "side": "R",
        "tx": 1020, "ty": 720,
        "place": "銚子市（千葉）",
        "fact": "大規模な公立病院を維持できず、\n2008 年 市立総合病院 休止。",
        "severe": True,
    },
]

# Nanto is rendered as a pin only (no label, no leader).
NANTO_PIN_KEY = "nanto"

svg = SRC.read_text()

# Recolor base map.
svg = svg.replace('fill="#EEEEEE"', f'fill="{BG_2}"')
svg = svg.replace('stroke="#000000"', f'stroke="{LINE}"')
# Hide the Okinawa-relocation boundary slash so it doesn't read as a stray line.
svg = svg.replace('stroke="#EEEEEE"', f'stroke="{BG}"')

# Highlight target prefectures.
for pref, color in HIGHLIGHT_PREFS.items():
    pattern = rf'(<g class="{pref}[^"]*" data-code="\d+" stroke-linejoin="round" )fill="{BG_2}"'
    svg, n = re.subn(pattern, rf'\g<1>fill="{color}"', svg)
    if n != 1:
        print(f"WARN: highlight {pref} replaced {n} times")

# Expand viewBox so callouts can live in the margins.
new_vb = f"{VB_LEFT} {VB_TOP} {VB_RIGHT - VB_LEFT} {VB_BOT - VB_TOP}"
svg = re.sub(r'viewBox="[^"]*"', f'viewBox="{new_vb}"', svg, count=1)

overlay = ['<g class="overlay">']

# ── Connector lines (drawn first, pins sit on top) ────────────────────────
def leader_path(pin, side, tx, ty):
    px, py = pin
    if side == "L":
        # pin → horizontal at pin's y → vertical to text level → small tail
        return (f"M{px:.1f},{py:.1f} "
                f"L{tx + 60:.1f},{py:.1f} "
                f"L{tx + 60:.1f},{ty:.1f} "
                f"L{tx + 10:.1f},{ty:.1f}")
    if side == "R":
        return (f"M{px:.1f},{py:.1f} "
                f"L{tx - 60:.1f},{py:.1f} "
                f"L{tx - 60:.1f},{ty:.1f} "
                f"L{tx - 10:.1f},{ty:.1f}")
    # B (bottom): straight down then horizontal to text x
    return (f"M{px:.1f},{py:.1f} "
            f"L{px:.1f},{ty - 40:.1f} "
            f"L{tx:.1f},{ty - 40:.1f} "
            f"L{tx:.1f},{ty - 20:.1f}")

for c in CALLOUTS:
    color = SEVERE if c["severe"] else ACCENT
    pin = PINS[c["pin"]]
    d = leader_path(pin, c["side"], c["tx"], c["ty"])
    overlay.append(
        f'  <path d="{d}" fill="none" stroke="{color}" '
        f'stroke-width="1.6" opacity="0.6"/>'
    )

# ── Pins (small filled dots, no number) ───────────────────────────────────
def emit_pin(pos, severe):
    x, y = pos
    color = SEVERE if severe else ACCENT
    overlay.append(f'  <circle cx="{x}" cy="{y}" r="14" fill="{BG}"/>')
    overlay.append(f'  <circle cx="{x}" cy="{y}" r="10" fill="{color}"/>')

for c in CALLOUTS:
    emit_pin(PINS[c["pin"]], c["severe"])

# Nanto pin (accent blue, no leader, no label).
emit_pin(PINS[NANTO_PIN_KEY], severe=False)

# ── Callout text blocks ───────────────────────────────────────────────────
def emit_callout(c):
    place_color = ACCENT if not c["severe"] else INK
    side = c["side"]
    tx, ty = c["tx"], c["ty"]
    if side == "L":
        anchor = "end"
    elif side == "R":
        anchor = "start"
    else:
        anchor = "middle"

    # Place name (city + prefecture).
    overlay.append(
        f'  <text x="{tx}" y="{ty}" text-anchor="{anchor}" '
        f'font-family="\'Shippori Mincho\', serif" font-size="38" '
        f'font-weight="600" fill="{place_color}">{c["place"]}</text>'
    )
    # Fact lines (split on \n).
    for i, line in enumerate(c["fact"].split("\n")):
        overlay.append(
            f'  <text x="{tx}" y="{ty + 50 + i * 40}" text-anchor="{anchor}" '
            f'font-family="\'Shippori Mincho\', serif" font-size="28" '
            f'fill="{INK_DIM}">{line}</text>'
        )

for c in CALLOUTS:
    emit_callout(c)

overlay.append("</g>")

svg = svg.replace("</svg>", "\n".join(overlay) + "\n</svg>")
OUT.write_text(svg)
print(f"saved → {OUT}")
