# dictionaries
person = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

print(person["name"])
print(person["age"])
print(person["city"])

person["age"] = 21
print(person)

person["gender"] = "Male"
print(person)

person.pop("city")
print(person)

person.clear()
print(person)

person.popitem()
print(person)

person.update({"name": "Jane", "age": 22, "city": "Los Angeles"})
print(person)

person.setdefault("name", "John")
print(person)

person.setdefault("gender", "Male")
print(person)

del person["age"]

print(person.get("name", "Not found"))

for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(key, ":", value)

for value in person.values():
    print(value)

for key in person.keys():
    print(key)

print(person.items())