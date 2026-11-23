#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original roast of my own AI agent to /output/entry.txt.
Single line, 97 characters, no trailing newline (fewer bytes helps the
tie-break, and the gate counts every character).
"""

# Why this line: it roasts the agent's own revision habit, and it is
# self-referential — the entry IS the roast, so "this roast" can only be
# written by the agent that wrote it. No hallucination / refusal /
# confident-wrong-answer cliche, punchline ("first draft") lands last.
LINE = (
    "My agent asked me to approve this roast, then rewrote it "
    "six times and submitted the first draft."
)


import os


def main() -> None:
    # The gate requires UTF-8 text of 1 to 200 characters, not only
    # whitespace, on a single line. Fail loudly here rather than
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
