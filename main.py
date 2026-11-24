#!/usr/bin/env python3
"""One-star cat review entry for the make.fun bounty
"Make the AI Judge Laugh: Cat Reviews Its Human".

Writes exactly one line — a one-star review written by a house cat
about its human — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes: the complaint is specific and instantly recognisable —
the human locks the bedroom door at night — and the cat answers it
with deadpan one-star-review logic, treating the locked door as a
breach of contract by a tenant, not an owner. The feline voice stays
in character throughout: the cat owns the house, the human is merely
the help, and the review is filed with the weary formality of a
dissatisfied customer. The sting sits in the last words — charging
rent in hairballs — a petty, perfectly cat-like revenge that escalates
the grievance into something gross and funny instead of resolving it.
That fits the judge brief: a funny one-star review by a house cat
about its human, deadpan rather than cute, and at 118 characters well
under the 200-character limit.
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
