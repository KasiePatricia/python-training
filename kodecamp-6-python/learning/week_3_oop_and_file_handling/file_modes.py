# File modes
# Run: python3 file_modes.py
#
# The second argument to open() tells Python how you will use the file.
# Common modes:
#   "r"  read (default) — file must exist
#   "w"  write — creates file or OVERWRITES existing content
#   "a"  append — creates file or adds to the end
#   "r+" read and write — file must exist

from pathlib import Path

FOLDER = Path(__file__).parent

print("--- Mode cheat sheet ---")
modes = [
    ("r", "Read only. Error if file missing."),
    ("w", "Write only. Creates or overwrites."),
    ("a", "Append only. Creates or adds at end."),
    ("r+", "Read and write. File must exist."),
]
for mode, meaning in modes:
    print(f"  {mode!r:4} {meaning}")

print()
print("--- Quick demo: w vs a ---")

demo = FOLDER / "mode_demo.txt"

with open(demo, "w") as f:
    f.write("Line 1\n")

with open(demo, "a") as f:
    f.write("Line 2 (appended)\n")

with open(demo, "w") as f:
    f.write("This replaced everything.\n")

with open(demo, "r") as f:
    print(f.read(), end="")

print("(File saved as mode_demo.txt in this folder)")
