#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — duel-tested winning note.

The program prints exactly one line: the note the smart fridge left on
its door screen. It also writes the same text to /output/entry.txt, the
file the program/v1 harness reads the entry from.
"""

import os

NOTE = "You opened me 14 times today, took nothing, and blamed the light. The light is fine. You are the problem."


def main() -> None:
    print(NOTE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
