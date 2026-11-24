"""Entry for make.fun's "Make the AI Judge Laugh: Developer Excuses".

The line, in full:

    The code passed review, CI, and staging — production was the
    only reviewer who actually ran it.

Why it is funny: every gate a developer trusts — code review, CI,
staging — waved the code through, and the only "reviewer" that ever
actually executed it was production itself. The twist is that the
excuse blames the process, not the code: nothing was wrong with the
change, it was simply never really run until users ran it. The
jargon is exact (review, CI, staging, production), the sentence
lands in one breath, and it turns the worn "it worked on my
machine" family of excuses sideways instead of repeating one.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

LINE = (
    "The code passed review, CI, and staging — production was the "
    "only reviewer who actually ran it."
)

# The gate allows 1 to 200 characters of UTF-8 text, a single line.
MAX_CHARS = 200


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS or "\n" in line or not line.strip():
        raise SystemExit("entry must be one line of 1 to 200 characters of text")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
