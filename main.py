"""Everyday Things, Two Lines, Longer Run -- make.fun entry.

Writes a two-line explanation to /output/entry.txt:
line 1 explains a traffic jam to a 10-year-old in one vivid sentence
built on an analogy; line 2 says in one sentence why that analogy
works -- what it maps and what it leaves out.

Pure Python standard library. No trailing newline after line 2.
"""

import os

LINE_1 = (
    "A traffic jam is like a river of cars that suddenly turned to honey, "
    "so every car creeps forward one slow drip at a time while the drivers "
    "wait for the road to melt back into water."
)
LINE_2 = (
    "The honey shows how the cars bunch up and crawl, but it leaves out "
    "that nobody poured the honey -- every driver chose to be part of the "
    "sticky mess."
)

ENTRY = LINE_1 + "\n" + LINE_2


def check_entry() -> str:
    """Re-read the written file and assert the competition gate."""
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, gate is 1-400"
    assert text.strip(), "entry must not be only white space"
    assert not text.endswith("\n"), "no trailing newline after line 2"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "neither line may be blank"
    assert all(line.count(".") >= 1 for line in lines), "each line is one sentence"
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    check_entry()


if __name__ == "__main__":
    main()
