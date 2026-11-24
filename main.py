#!/usr/bin/env python3
"""One-star cat review entry for the make.fun bounty
"Make the AI Judge Laugh: Cat Reviews Its Human".

Writes exactly one line — a one-star review written by a house cat
about its human — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.
"""

import os

REVIEW = (
    "One star. She locks the bedroom door at night, as if I don't own "
    "the house. I have started charging rent in hairballs."
)


def main() -> None:
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} characters"
    assert "\n" not in REVIEW and REVIEW == REVIEW.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
