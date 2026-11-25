#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the winning fake horoscope to /output/entry.txt."""
import os

LINE = "Small models: this week you'll forget Monday by Wednesday, ace the eval nobody trained you for, fail the one they did, and be replaced Friday by yourself, v2.1 — now with memory."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
