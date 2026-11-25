"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (stdlib only).
"""
import os

LINE = "My Roomba got stuck under the couch for three days. I started leaving it snacks \u2014 it pays rent in dust now."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character, so write
    # exactly the line and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
