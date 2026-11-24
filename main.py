#!/usr/bin/env python3
"""One-Liner Laugh Lab: the robot vacuum's excuse after eating a sock.

Writes a single short funny line to entry.txt in the grader's output
directory (MAKEFUN_OUTPUT_DIR, default /output). The gate requires UTF-8
text of 1 to 200 characters, not only white space, so the line is checked
here before it is written. The output is fully deterministic: the same
line every run.
"""

import os
import sys

# The excuse. Deadpan legal defence: the floor is the vacuum's
# jurisdiction, and the sock was on the floor. Short, original, and the
# joke comes from the fit - a vacuum would absolutely argue this.
LINE = "The sock was on the floor. The floor is my jurisdiction. I rest my case."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
