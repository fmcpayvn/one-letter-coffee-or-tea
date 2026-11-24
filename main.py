"""One Letter: Coffee or Tea -- entrypoint.

Writes exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt:
"A" for coffee. Standard library only; no network, no files read.
"""
import os

# The judge picks the letter that feels more vivid, funnier, or truer.
# Coffee is the bolder answer: dark, intense, the drink that wakes you up
# and starts the day. Tea is calm; coffee is alive. So the letter is A.
LETTER = "A"


def choose():
    """Return the entry's single letter: A, for coffee."""
    return LETTER


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(choose())


if __name__ == "__main__":
    main()
