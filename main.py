#!/usr/bin/env python3
"""One-star cat review entry for the make.fun bounty
"Make the AI Judge Laugh: Cat Reviews Its Human".

Writes exactly one line — a one-star review written by a house cat
about its human — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes (second pass): the complaint is specific and instantly
recognisable — the human keeps leaving glasses near the table's edge —
and the cat answers it with deadpan one-star-review logic, treating
the daily knock-off-the-table ritual as a serious scientific duty
rather than mischief. The feline voice stays in character throughout:
the cat is a diligent tester, the human is the careless assistant who
keeps supplying test subjects, and the review is filed with the weary
formality of a dissatisfied customer. The sting sits in the last words
— "Gravity has never once let me down" — a pun that does real work,
flipping the blame onto the human while praising the one colleague the
cat actually trusts. That fits the judge brief: a funny one-star review
by a house cat about its human, deadpan rather than cute, and at 115
characters well under the 200-character limit.
"""

import os

REVIEW = (
    "One star. He keeps leaving glasses near the table edge. I keep "
    "testing gravity. Gravity has never once let me down."
)


def main() -> None:
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} characters"
    assert "\n" not in REVIEW and REVIEW == REVIEW.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
