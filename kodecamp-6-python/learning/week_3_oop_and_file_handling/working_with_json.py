# Working with JSON data
# Run: python3 working_with_json.py
#
# JSON is a text format for structured data (objects, lists, strings, numbers).
# Python's json module converts between JSON text and Python values.

import json

print("--- Python dict/list → JSON string ---")

person = {
    "name": "Grace",
    "role": "engineer",
    "skills": ["Python", "testing"],
}

json_text = json.dumps(person, indent=2)
print(json_text)

print()
print("--- JSON string → Python dict ---")

loaded = json.loads(json_text)
print("Name:", loaded["name"])
print("First skill:", loaded["skills"][0])

print()
print("--- JSON types map to Python types ---")
print("object  → dict")
print("array   → list")
print("string  → str")
print("number  → int or float")
print("true    → True")
print("false   → False")
print("null    → None")
