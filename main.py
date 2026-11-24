"""One Letter: Coffee or Tea -- entrypoint.

Writes exactly one letter, "A" for coffee, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no files read, nothing else written.
"""
import os

LETTER = "A"  # A for coffee


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
