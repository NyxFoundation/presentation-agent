# Verity deck — Nyx logo overlay

The original **Ethproofs call #9 — Verity Client** slides, kept exactly as
authored, with the Nyx Foundation wordmark added to the bottom-right of every
slide (title slide included).

## Files

| File | Description |
|---|---|
| `Verity.pptx` | Source deck, unmodified |
| `Verity_nyx.pptx` | Output — Nyx wordmark on the bottom-right of all 10 slides |
| `assets/nyx_logo.png` | Wordmark overlaid (rendered from `public/images/nyx_logo.svg`) |
| `add_nyx_logo.py` | Script that produces the output from the source |

## Regenerate

```bash
pip install python-pptx
python3 decks/verity/add_nyx_logo.py
```

The logo is placed at a fixed bottom-right position on each slide: width
1.6 in, 0.3 in right margin, 0.28 in bottom margin. All slides have a white
background, so the dark wordmark reads cleanly.
