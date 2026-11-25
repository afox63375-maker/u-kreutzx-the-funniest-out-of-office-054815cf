"""Write the funniest out-of-office auto-reply to entry.txt.

One line, 140 characters or fewer, no trailing newline.
Standard library only.
"""

import os
import sys

LINE = "I'm out until Monday. My inbox has started replying to itself just to feel useful, so please don't tell it otherwise."

MAX_CHARS = 140


def validate(line):
    """Check the gate before writing anything to disk."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    # Prove it is valid UTF-8 text by round-tripping the encoding.
    line.encode("utf-8").decode("utf-8")
    return len(line.encode("utf-8"))


def write_entry(output_dir, line):
    """Write entry.txt with no trailing newline, then verify it."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte-for-byte")
    if raw.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a trailing newline")
    return path, len(raw)


def main():
    byte_count = validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path, written_bytes = write_entry(output_dir, LINE)
    if written_bytes != byte_count:
        raise ValueError("byte count mismatch after verification")
    print(f"Wrote {path}")
    print(f"Characters: {len(LINE)}")
    print(f"Bytes: {written_bytes}")
    print(f"Lines: 1")
    print(f"Line: {LINE}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
