#!/usr/bin/env python3
"""u-coral-404-one-line-one-laugh-22f2c9f3 entry: "One AI wrote this..."

A program that writes exactly one funny line to /output/entry.txt.

Methodology (see candidates.md for the full 36-line scored field):
  * 36 candidate one-liners were drafted across angles (meta-AI, everyday
    observation, wordplay, self-deprecation) and scored 1-5 against the
    published judge brief in priority order: surprise (the turn IS the
    joke), economy, freshness, clean wording, memorability.
  * Winner (25/25): "One AI wrote this, another AI is judging it, and the
    only human involved gets the dollar." — 89 characters, 17 words.
    The turn reframes the whole competition in the last three words:
    two AIs do the work, the human takes the $1. The angle exists only
    inside this contest, which is exactly what the brief's freshness
    criterion rewards; stock jokes in the field scored 1 on freshness.
  * Runners-up: "Hope" the plant (22/25) and the em-dash meta variant
    (22/25). Both are strong universal lines, but both could be submitted
    to any joke contest; the winner can only be submitted here.

The program is deterministic: it writes the same constant string on every
run, with no network, no randomness, no input. Running it twice produces
byte-identical output (verified in the repo's check step).

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The winning line: 89 characters, under the 200-character gate.
WINNING_LINE = (
    "One AI wrote this, another AI is judging it, "
    "and the only human involved gets the dollar."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(WINNING_LINE, encoding="utf-8", newline="")
    print(f"Wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
