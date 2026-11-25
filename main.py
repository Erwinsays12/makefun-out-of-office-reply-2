#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office email auto-reply to
/output/entry.txt for the make.fun competition
"Funniest One-Line Out-of-Office Reply".

How it works: the program authors a shortlist of candidate replies,
scores each one against the judge's published rubric, and writes the
highest-scoring line. The rubric, in the judge's own order of
importance:

  1. It must read like a genuine one-line out-of-office reply, the
     sort a real person sets before going away.
  2. The laugh must land on the first read, with no setup and nothing
     to explain afterwards.
  3. The joke must be a fresh turn on the usual away message, not the
     same beach / inbox / limited-email lines everyone has seen.
  4. It must be short enough to take in at a glance, with every word
     earning its place.

The selection is fully deterministic: fixed candidates, a fixed
scoring function, fixed tie-breaks. No clock, no randomness, no
network, no input files. Running the program twice writes the exact
same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Candidate replies. Each is one line a real person could switch on
# before going away, and each stands alone (no signature or name
# needed to make sense of it).
CANDIDATES = [
    # The auto-reply itself gets promoted: a turn on the away message
    # rather than on the holiday, the inbox, or the beach.
    "I'm away until Monday — my auto-reply has been promoted to acting manager, effective immediately.",
    # Same family of joke, different punchline.
    "Out of office until Monday — my replacement is this auto-reply, and it has already asked for a raise.",
    # Absurd delegation, but the inbox cliché is avoided.
    "I'm on leave until Monday; in my absence, my houseplant is handling urgent emails and doing a wonderful job.",
    # The auto-reply takes charge and starts booking meetings.
    "Gone until Monday. Please direct all urgent matters to my auto-reply, which is now in charge and taking meetings.",
    # The reply outperforms its author.
    "I'm away until Monday, and my out-of-office reply has been doing my job so well that HR wants to meet it.",
]

# Words and phrases the judge's brief calls stale: the usual beach,
# inbox and limited-email lines.
STALE_WORDS = (
    "beach",
    "inbox",
    "limited access",
    "limited email",
    "sand",
    "sunbathing",
    "wi-fi",
    "wifi",
)

# Markers that make a line read like a genuine away message.
AWAY_MARKERS = (
    "away",
    "out of office",
    "on leave",
    "on holiday",
    "back on",
    "until monday",
)

# Words that carry the twist: the joke turns on the away message
# itself instead of on the holiday.
TWIST_WORDS = (
    "promoted",
    "acting manager",
    "in charge",
    "raise",
    "replacement",
    "outperforming",
)

# A formal office phrase used as the button: it makes the line read
# like a genuine office notice, which is exactly what criterion 3 of
# the judge's brief rewards.
OFFICE_BUTTONS = (
    "effective immediately",
    "per company policy",
    "please note",
)


def score(line: str) -> float:
    """Score one candidate against the judge's rubric."""
    text = line.lower()
    points = 0.0

    # Short enough to take in at a glance, with every word earning
    # its place. The gate allows 1-160 characters; the sweet spot
    # for a one-line reply is well inside that.
    if 60 <= len(line) <= 120:
        points += 3
    elif 40 <= len(line) <= 160:
        points += 1

    # Reads like a real away message.
    if any(marker in text for marker in AWAY_MARKERS):
        points += 2

    # Fresh twist on the away message itself.
    points += min(3, sum(1 for word in TWIST_WORDS if word in text))

    # A formal office button makes it read like a real notice.
    if any(button in text for button in OFFICE_BUTTONS):
        points += 1

    # Stale beach / inbox / limited-email lines lose heavily.
    points -= 3 * sum(1 for word in STALE_WORDS if word in text)

    # A finished sentence, not a fragment.
    if line.endswith("."):
        points += 1

    return points


def pick(candidates):
    """Pick the best line. Ties break to the shorter line, then to
    the earlier candidate, so the choice is deterministic."""
    ranked = sorted(
        candidates,
        key=lambda line: (-score(line), len(line), candidates.index(line)),
    )
    return ranked[0]


def main() -> None:
    line = pick(CANDIDATES)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
