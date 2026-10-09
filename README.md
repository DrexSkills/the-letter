# THE LETTER

A story-driven 2D pixel-art mystery adventure, played like a 90s side-scrolling platformer.

A young man who grew up on a farm in Millbrook, without his father, finds a letter in his mailbox — written by that father, and dated three days ago. Follow it down the country lane, across the roofs of an eastbound train, to the old town of Ashbourne.

All art is true pixel art: backgrounds, tiles, the hero and every townsperson are drawn pixel-by-pixel in code (no AI images, no 3D, no blurry scaling). Dialogue portraits are 32-px pixel portraits.

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
- **1-1 Millbrook** — read the letter on the farm, question the villagers, reach Millbrook Halt.
- **1-2 The Train** — cross the carriage roofs and find the 2005 photograph.
- **1-3 Ashbourne** — a stone town at dusk; meet the townsfolk and find the bookseller.

Hit **?** blocks for stamps (25 stamps = +1 heart) and **!** envelope blocks for the 7 story clues.

## Project layout
- `index.html` — the complete, self-contained game (assets embedded).
- `src/template.html` — all game code, including the hero/NPC pixel bitmaps and the background generator.
- `assets/portraits/` — 32-px dialogue portraits.
- `build.py` — embeds the portraits and writes `index.html` (`python3 build.py`).
