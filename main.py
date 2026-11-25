#!/usr/bin/env python3
"""Two-Sentence Horror — writes one story to /output/entry.txt.

The story is exactly two sentences: a phone makes a slideshow of a
daughter's first year, and every photo in it was taken from inside her
closet. The second sentence turns the first — a sweet family memory
becomes evidence someone was hiding in the child's room all year. The
horror is implied, never explained; concrete, no gore, no familiar twist
retold. Tightened in revision: "made a slideshow of" kept, "from inside
her closet" is the reveal; exactly two sentences, 104 characters, under
the 400 limit.
"""

import os

LINE = "My phone made a slideshow of my daughter's first year. Every photo was taken from inside her closet."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
