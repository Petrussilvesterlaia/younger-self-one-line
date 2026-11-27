#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Writes a single line, in English, to /output/entry.txt and validates it
against the bounty gate: UTF-8 text, 1-200 characters, a single line,
not only whitespace. No network, no secrets, no input files.
"""

import os
import sys

ENTRY = (
    "Kid, one day you'll run a store by daylight and hunt coins past "
    "midnight \u2014 the lathe taught you patience, the charts taught "
    "you nerve."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Raise ValueError unless the text passes the bounty gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 200):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Read back and verify what was actually written, byte for byte.
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("utf-8"):
        raise ValueError("read-back mismatch: file bytes differ from entry")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    validate(written)
    if written != ENTRY:
        raise ValueError("read-back mismatch: file differs from entry")
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
