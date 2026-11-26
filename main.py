#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes one line to entry.txt: a deadpan TV weather forecast for the
invented city of Vostok-on-Sea. The line reads like a real broadcast
read-off — high, low, precipitation — but every figure is wrong in a
way only a city that does not exist could manage: a low of one (1)
working radiator, and snow that tastes faintly of paperwork.

The program is stdlib-only and deterministic. It validates the line
against the competition gate (UTF-8 text, 1 to 160 characters, not
only whitespace) before writing, then reads the file back and checks
the bytes round-trip so the submitted text is exactly the line.
"""

import os
import sys

# The entry, chosen by candidate tournament (8 candidates scored on
# specificity / surprise / freshness; this one scored 5/5/4, the
# highest). A deadpan forecast: real broadcast shape, absurd figures.
LINE = (
    "Vostok-on-Sea: a high of 2 degrees, a low of one (1) working "
    "radiator, and snow that tastes faintly of paperwork."
)

MIN_CHARS = 1
MAX_CHARS = 160


def gate_problems(text):
    """Return a list of every way the text fails the competition gate."""
    problems = []
    if not text or not text.strip():
        problems.append("line is empty or only whitespace")
    if len(text) < MIN_CHARS:
        problems.append("line is shorter than %d character" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("line must be a single line, no newlines")
    # The quest rewards a concrete number or detail that makes the
    # invented place feel real, so refuse a line with no digit at all.
    if not any(char.isdigit() for char in text):
        problems.append("line has no concrete number or detail")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not valid UTF-8 text")
    return problems


def resolve_output_dir():
    """Pick the output directory the harness convention names first."""
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(variable)
        if value:
            return value
    return "/output"


def write_entry(directory):
    """Write the line to entry.txt and verify the bytes round-trip."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != LINE:
        raise SystemExit("round-trip check failed: entry.txt differs from LINE")
    if len(raw) != len(LINE.encode("utf-8")):
        raise SystemExit("byte-length check failed: entry.txt is not the LINE bytes")
    return path


def main():
    problems = gate_problems(LINE)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    path = write_entry(resolve_output_dir())
    print("wrote %s: %d chars" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
