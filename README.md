# THE LETTER

A story-driven 2D pixel-art mystery adventure, played like a 90s side-scrolling platformer.

A young man who grew up without his father finds a letter in his mailbox — written by that father, and dated three days ago. Follow it from the city, across the roofs of an eastbound train, to the countryside town of Ashbourne.

**Play:** open `index.html` in a browser (or enable GitHub Pages for this repo).

## Controls
| Action | Keyboard |
|---|---|
| Move | ← → / A D |
| Jump (hold for higher) | Z / Space / ↑ |
| Run | X / Shift |
| Talk | E / ↓ |
| Journal | J |
| Pause | P / Esc |
| Mute | M |

Touch controls appear automatically on phones and tablets.

## Chapter One
- **1-1 The City** — read the letter, question the neighbours, reach Central Station.
- **1-2 The Train** — cross the carriage roofs and find the 2005 photograph.
- **1-3 Ashbourne** — meet the townsfolk and find the bookseller.

Hit **?** blocks for stamps (25 stamps = +1 heart) and **!** envelope blocks for the 7 story clues.

## Project layout
- `index.html` — the complete, self-contained game (assets embedded).
- `src/template.html` — game source with an `%%ASSETS%%` placeholder.
- `assets/` — sprite sheet, portraits, backgrounds and chapter art cut from the concept sheets.
- `build.py` — embeds `assets/` into `src/template.html` and writes `index.html` (`pip install pillow`, then `python3 build.py`).
