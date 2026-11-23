"""One line to make the judge fall in love.

Writes the line to /output/entry.txt (the gate requires UTF-8 text,
1 to 240 characters, not only white space).
"""

import os

ENTRY_TEXT = "She folds the corner of every page she loves, so the book she lends you arrives already knowing which parts of her to give away."


def main() -> None:
    text = ENTRY_TEXT.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the written file is byte-identical to the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the entry text")


if __name__ == "__main__":
    main()
