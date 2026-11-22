#!/usr/bin/env python3
"""curious-letter: write one short intriguing text to /output/entry.txt.

Stdlib only, no network, deterministic: the same text is written on every run.
"""

import os

ENTRY_TEXT = (
    "In the attic of the last house on your street is a room with no door. "
    "Inside it, a letter addressed to you, in your own handwriting, dated "
    "tomorrow."
)

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
        f.write("\n")


if __name__ == "__main__":
    main()
