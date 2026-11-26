"""Deadpan forecast for a city that does not exist.

Writes one 160-character-max broadcast line to entry.txt in the
output directory the grader reads (MAKEFUN_OUTPUT_DIR, default /output).
"""
import os

ENTRY = (
    "Overnight in Port Sullen, a low of minus 4, light drizzle, "
    "and a 70 percent chance the fog asks where you have been all evening."
)


def main():
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
