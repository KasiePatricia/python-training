# Working with files: read, write, append
# Run: python3 working_with_files.py

from pathlib import Path

FOLDER = Path(__file__).parent
NOTES = FOLDER / "notes.txt"

print("--- Write a new file ---")

with open(NOTES, "w") as f:
    f.write("Shopping list\n")
    f.write("- milk\n")
    f.write("- eggs\n")

print("Wrote", NOTES.name)

print()
print("--- Read the whole file ---")

with open(NOTES, "r") as f:
    content = f.read()

print(content, end="")

print()
print("--- Read line by line ---")

with open(NOTES, "r") as f:
    for line in f:
        print(">", line.rstrip())

print()
print("--- Append a line ---")

with open(NOTES, "a") as f:
    f.write("- bread\n")

with open(NOTES, "r") as f:
    print(f.read(), end="")
