#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes one line to entry.txt: a deadpan TV weather forecast for the
invented city of Port Null. Beat one is a straight broadcast read-off
— temperature, wind speed, wind direction. Beat two hands the weather
over to local politics: the mayor has banned the sun until the budget
passes. The forecast stops being weather and becomes a council
decision, and the deadpan never breaks — no wink, no punchline word,
just a mayor with a pen and a sky that has to wait.

Candidate tournament (specificity / surprise / freshness, each 1-5):
  1. Grimhollow: rain only falls on the tax office roof — 5/4/4 = 13
  2. WINNER: Port Null, mayor bans the sun until the budget passes — 5/5/5 = 15
  3. New Boring: fog may lift at noon, nobody will check — 4/3/4 = 11
  4. Zzyzx Falls: avalanche warning is a 47-year-old who shouts "run" — 5/5/4 = 14
  5. Vostok ferry left at 9 AM because the sea was in a hurry — 4/4/4 = 12
  6. Dullsville: radar broke in 1998, we guess now, professionally — 5/4/5 = 14
  7. Karpovsk: forecast after Thursday is classified by the council — 5/5/4 = 14

The winner is the only candidate whose second beat takes power away
from the weather itself. The sun is not a forecast here, it is a
budget item, and the line stays flat and broadcast-voiced all the way
through. It beats the round-1 Vostok line (5/4/4 = 13, one observation
about a radiator) on every axis. Verified length: 111 chars, inside
the 116-char round-1 bound and the 160-char gate.
"""

import os
import sys

FORECAST = (
    "Port Null: 6 degrees, wind from the east at 40 knots, and the "
    "mayor has banned the sun until the budget passes."
)

LOWER = 1
UPPER = 160


def problems(text):
    """List every way the text fails the competition gate."""
    found = []
    if not text or not text.strip():
        found.append("line is empty or only whitespace")
    if len(text) < LOWER:
        found.append("line is shorter than %d character" % LOWER)
    if len(text) > UPPER:
        found.append("line is %d characters, over the %d limit" % (len(text), UPPER))
    if "\n" in text or "\r" in text:
        found.append("line must be a single line, no newlines")
    if not any(ch.isdigit() for ch in text):
        found.append("line has no concrete number or detail")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        found.append("line is not valid UTF-8 text")
    return found


def out_dir():
    """Pick the output directory, harness convention first."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def emit(directory):
    """Write the forecast to entry.txt and check the bytes round-trip."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORECAST)
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != FORECAST:
        raise SystemExit("round-trip check failed: entry.txt differs from FORECAST")
    if len(raw) != len(FORECAST.encode("utf-8")):
        raise SystemExit("byte-length check failed: entry.txt is not the FORECAST bytes")
    return target


def run():
    bad = problems(FORECAST)
    if bad:
        for item in bad:
            print("gate failed: %s" % item, file=sys.stderr)
        return 1
    target = emit(out_dir())
    print("wrote %s: %d chars" % (target, len(FORECAST)))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
