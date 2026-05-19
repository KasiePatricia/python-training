# Reading JSON into Python objects
# Run: python3 reading_json_to_python.py
#
# Run python_objects_to_json.py first if sample.json does not exist.

import json
from pathlib import Path

FOLDER = Path(__file__).parent
INPUT = FOLDER / "sample.json"


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"


def book_from_dict(data):
    """Build a Book from a dict loaded from JSON."""
    return Book(data["title"], data["author"], data["pages"])


print("--- Load JSON file into Python ---")

if not INPUT.exists():
    print(f"Missing {INPUT.name}. Run: python3 python_objects_to_json.py")
    raise SystemExit(1)

with open(INPUT, "r") as f:
    raw = json.load(f)

print("Type of raw:", type(raw))
print("Keys:", list(raw.keys()))

print()
print("--- Turn dicts into Book objects ---")

books = [book_from_dict(item) for item in raw["books"]]

for book in books:
    print(book)
