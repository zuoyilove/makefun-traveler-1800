#!/usr/bin/env python3
"""One sentence explaining the modern internet to a traveler from 1800.

Writes the sentence to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single sentence.
"""

LINE = (
    "Imagine every library, post office, and market stall on earth joined by "
    "invisible roads, so a letter you write can reach anyone, anywhere, "
    "before your candle burns down."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
