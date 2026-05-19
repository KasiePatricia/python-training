# Converting Python objects to JSON
# Run: python3 python_objects_to_json.py

import json
from pathlib import Path

FOLDER = Path(__file__).parent
OUTPUT = FOLDER / "sample.json"

print("--- Save a dict to a .json file ---")


def book_to_dict(book):
    """Turn a Book object into a plain dict (JSON-friendly)."""
    return {
        "title": book.title,
        "author": book.author,
        "pages": book.pages,
    }


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


books = [
    Book("1984", "George Orwell", 328),
    Book("The Hobbit", "J.R.R. Tolkien", 310),
]

data = {"books": [book_to_dict(b) for b in books]}

with open(OUTPUT, "w") as f:
    json.dump(data, f, indent=2)

print("Saved to", OUTPUT.name)
print()
with open(OUTPUT, "r") as f:
    print(f.read(), end="")
