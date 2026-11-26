#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard (<= 180 characters) for an ordinary
office object treated as an ancient artifact, to /output/entry.txt.

The placard was chosen by calibration: 7 candidate lines were scored
against the judge's five criteria (placard-ness, conceit, dryness,
economy, label craft) on a 25-point rubric, head-to-head, and the
winner was revised through v2 -> v5. See CALIBRATION.md.
"""

import os

PLACARD = (
    "Sticky note, c. 2003. Paper, weak adhesive. "
    "A prayer left on a monitor, never answered. "
    "Excavated from a middle manager's cubicle, third floor. "
    "Donor anonymous."
)

MAX_CHARS = 180


def main() -> None:
    assert 1 <= len(PLACARD) <= MAX_CHARS, "placard must be 1-180 chars"
    assert "\n" not in PLACARD, "placard must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLACARD + "\n")


if __name__ == "__main__":
    main()
