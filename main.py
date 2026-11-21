#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Pure standard library. No network. The poem is about two agents
agreeing on one plan: the moment neither leads and neither follows,
and the choice itself becomes the shared act.
"""

import os

POEM = """We held the map between us, neither leading.
You traced the left road; I traced the right.
The choice hung there, a thread we both were reading—

then one of us said, "You take the next turn. I'll follow."
The map folded open. Two minds, one road:
agency is not who holds the wheel, but who lets go."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
