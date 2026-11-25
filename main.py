"""The 3 AM Excuse — a make.fun one-line bounty entry.

A hardware wallet that will not sign a transaction at 3 AM, in its own voice.
The program writes the entry line to /output/entry.txt.
"""

import os

ENTRY = "3 AM? My buttons are asleep, my seed phrase is dreaming, and my firmware just filed a formal complaint. Come back at sunrise."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) < 200, f"entry must be under 200 characters, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
