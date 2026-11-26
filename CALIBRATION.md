# Calibration log — Office Artifacts: The One-Line Placard Contest

Rubric: 25 points, 5 points per judge criterion (in the judge's order):
1. Placard for an ordinary office object treated as an ancient artifact
2. Conceit inventiveness (specific, surprising imagined history)
3. Dryness of wit (deadpan, no straining or explaining)
4. Economy (<=180 chars, every word earns its place, reads well aloud)
5. Label craft (date, material, provenance, donor)

## Round 1 — 7 candidate lines

| Variant | C1 | C2 | C3 | C4 | C5 | Total | Chars |
|---|---|---|---|---|---|---|---|
| V1 stapler — "Stapler, c. 1997. Pressed steel. Used in the Rite of Binding, when two sheets were joined forever before witnesses. Donated by Accounts Payable." | 5 | 4 | 5 | 4 | 5 | 23 | 144 |
| V2 sticky note — "Sticky note, c. 2003. Paper, weak adhesive. A prayer left on a monitor, answered never. Excavated from the cubicle of a middle manager, third floor." | 5 | 5 | 5 | 5 | 4 | 24 | 148 |
| V3 lanyard — "Lanyard, c. 2011. Woven nylon, plastic clip. Worn at the neck to prove the wearer belonged. Recovered from a conference, still attached to its badge." | 5 | 3 | 4 | 4 | 4 | 20 | 149 |
| V4 microwave — "Microwave, c. 1998. Steel, scorched interior. A communal hearth where lunches were warmed and grudges kept hot. Donated by the break room." | 5 | 4 | 4 | 4 | 4 | 21 | 138 |
| V5 paperclip — "Paperclip, c. 1984. Bent steel wire. A binding charm for loose papers, believed to ward off the demon of disorder. Found in a desk drawer, hoarded." | 5 | 4 | 4 | 4 | 4 | 21 | 147 |
| V6 hole punch — "Hole punch, c. 2005. Cast iron. A ritual instrument for piercing the sacred page, that it might join the binder. Gift of the Records Office." | 5 | 4 | 4 | 4 | 4 | 21 | 140 |
| V7 rubber stamp — "Rubber stamp, c. 1992. Wood and rubber. Pressed onto documents to declare them APPROVED, a word the ancients held to be magic. Ink long dried." | 5 | 4 | 5 | 4 | 3 | 21 | 142 |

## Head-to-head (pairwise, first differing criterion decides)

- V2 vs V1: V2 wins on C2 — "a prayer left on a monitor, never answered"
  is a more surprising, specific imagined history than the "Rite of Binding"
  (a familiar trope); V1's "before witnesses" is dry but the conceit is weaker.
- V2 vs V4: V2 wins on C2/C3 — "communal hearth / grudges kept hot" is a good
  line but the hearth metaphor is generic; the prayer conceit is more specific.
- V2 vs V5/V6/V7: V2 wins on C2 — binding charm, sacred page, APPROVED-as-magic
  are all solid, but none is as surprising as a sticky note as an unanswered prayer.
- V3 loses early on C2 ("prove the wearer belonged" is a generic office joke).

Winner of round 1: **V2 sticky note (24/25)**.

## Round 2 — revising the winner (v2 -> v5)

- v2 (orig, 148 chars, 24/25): "…answered never. Excavated from the cubicle
  of a middle manager, third floor." — C5 docked: no donor.
- v3 (143 chars): "never answered" reads better aloud than "answered never";
  "a middle manager's cubicle" is tighter. Still 24/25 (C5 unchanged).
- v4 (160 chars): adds "Donor anonymous." — a deadpan catalogue touch that
  completes the label craft (date, material, provenance, donor) and adds dryness.
  Re-scored: C1 5, C2 5, C3 5, C4 5, C5 5 = **25/25**.
- v5 = v4 (no further change improved it; "Donor anonymous" is the last word
  the line needs — adding anything else would cost economy).

## Final line (v5, 160 characters, 25/25)

> Sticky note, c. 2003. Paper, weak adhesive. A prayer left on a monitor, never answered. Excavated from a middle manager's cubicle, third floor. Donor anonymous.

## Verification

- `python3 main.py` run 3x: output deterministic and byte-identical each run.
- `/output/entry.txt`: UTF-8, 1 line, 160 characters (plus trailing newline).
