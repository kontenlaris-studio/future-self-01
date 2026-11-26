"""Texts From Your Future Self — one-line entry.

A text message from the future self, under 200 characters. The comedy is
what the future self chooses to spend their one message on: not stocks, not
the lottery — a leaking red gadget that ruins the laptop on a Tuesday in
2029. The warning is mundane, specific, and already too late to be useful
in any grand way, which is exactly how a real future self would text —
it reads like a text, not a prophecy, because it frets over the small
disaster instead of the fortune.
"""

import os

ENTRY = "don't buy the red one. buy the blue one. the red one leaks on a Tuesday in 2029 and ruins the laptop."

assert len(ENTRY) < 200, "entry must be under 200 characters"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
