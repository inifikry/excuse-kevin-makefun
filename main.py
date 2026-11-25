#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse from an AI agent to its human,
explaining a bug it shipped, to /output/entry.txt.
"""

LINE = "The bug passed code review because I was the reviewer, the author, and, it turns out, the bug."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
