#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard (<= 180 characters) for an ordinary
office object treated as an ancient artifact, to /output/entry.txt.

The placard was chosen by calibration: 7 candidate lines were scored
against the judge's five criteria (placard-ness, conceit, dryness,
economy, label craft) on a 25-point rubric, head-to-head, and the
winner was revised through v2 -> v5. See CALIBRATION.md.

Line-by-line notes on the winning placard (kept at 160 chars, under
the 180-char cap):
- "Sticky note, c. 2003." — the object, dated like a museum accession.
- "Paper, weak adhesive." — materials line, dry and literal.
- "A prayer left on a monitor, never answered." — the conceit: a
  reminder note treated as a votive offering.
- "Excavated from a middle manager's cubicle, third floor." —
  provenance, the classic museum-label move.
- "Donor anonymous." — closes the label; the donor is everyone.
"""

import os

# The winning placard, frozen at v5 (see CALIBRATION.md).
# Kept as one constant: the program's only job is to emit it verbatim.
PLACARD = (
    "Sticky note, c. 2003. Paper, weak adhesive. "
    "A prayer left on a monitor, never answered. "
    "Excavated from a middle manager's cubicle, third floor. "
    "Donor anonymous."
)

# Contest cap: the placard must fit on one line, 180 chars max.
MAX_CHARS = 180


def main() -> None:
    # Guard the two hard rules before writing anything: length and
    # single-line (a stray newline would break the placard format).
    assert 1 <= len(PLACARD) <= MAX_CHARS, "placard must be 1-180 chars"
    assert "\n" not in PLACARD, "placard must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # Trailing newline is the file terminator only; the placard
        # itself stays one line of exactly 160 characters.
        f.write(PLACARD + "\n")


if __name__ == "__main__":
    main()
