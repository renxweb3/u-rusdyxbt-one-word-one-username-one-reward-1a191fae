#!/usr/bin/env python3
"""One Word, One Username, One Reward — the entry is our handle."""
import os
from pathlib import Path

HANDLE = "wohca"


def main():
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(HANDLE.encode("utf-8"))
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
