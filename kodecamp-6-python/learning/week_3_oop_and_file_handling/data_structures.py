# Data Structures: Lists, Tuples, Dictionaries, Sets

# Lists: ordered, mutable, indexed, can contain duplicates
l = list()
r = range(10)
empty_list = []

mixed_list = [1, "apple", True, 3.14, [1, 2, 3]]
print(mixed_list)
print(mixed_list[5])

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# List Manipulation - CRUD operations - create, read - retrieve, update, delete
# append, insert, remove, pop, clear, sort, reverse, count, index, len, max, min

# slicing of lists
# [start:end + 1] - end is not included
print(fruits[1:3])

# update the list
# list_name[index] = new_value
fruits[0] = "pineapple"

# Built-in functions for lists

# append - add to the end of the list
# list_name.append(value)
fruits.append("orange")
print(fruits)

# insert - add to the list at a specific index
# list_name.insert(index, value)
fruits.insert(1, "watermelon")
print(fruits)

# remove - remove the first occurrence of a value
# list_name.remove(value)
fruits.remove("banana")
print(fruits)

# pop - remove and return the last element
# list_name.pop()
fruits.pop(1)
fruits.pop()
print(fruits)

# clear - remove all elements from the list
# list_name.clear()
fruits.clear()
print(fruits)

# delete - delete the list
# del list_name
del fruits
print(fruits)

# Tuples: ordered, immutable, indexed, can contain duplicates
t = tuple()
r = range(10)
empty_tuple = ()

mixed_tuple = (1, "apple", True, 3.14, [1, 2, 3])
print(mixed_tuple)
print(mixed_tuple[5])

fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Tuples are immutable, so you can't add, remove, or update elements
# Tuples are indexed, so you can access elements by index


# Built-in functions for tuples 
# count - count the number of occurrences of a value
# tuple_name.count(value)
print(fruits.count("apple"))

# index - return the index of the first occurrence of a value
# tuple_name.index(value)
print(fruits.index("banana"))

# Dictionary: unordered, mutable, key-value pairs, no duplicates
m = {"key": "value", "key2": "value2"}
d = dict()
empty_dict = {}
D = dict(name="John", age=20, city="New York")


person = {
    "name": "John",
    "age": 20,
    "city": "New York"
}
print(person)
print(person["name"])

# Dictionary Manipulation - CRUD operations - create, read - retrieve, update, delete

# add to the dictionary
# dictionary_name[key] = value
person["gender"] = "Male"
print(person)

# update the dictionary
# dictionary_name[existing_key] = new_value
person["age"] = 21
print(person)

# remove from the dictionary
# dictionary_name.pop(key)
person.pop("gender")
print(person)

# delete the dictionary
# del dictionary_name
del person
del person["age"]
print(person)

# clear the dictionary
# dictionary_name.clear()
person.clear()
print(person)


# Loops through a list
# for item in list_name:
for item in fruits:
    print(item)

# for index, item in enumerate(list_name):
for index, item in enumerate(fruits):
    print(index, ":", item)



# Loops through a dictionary
# for key in dictionary_name:
for key in person:
    print(key, ":", person[key])

# for key, value in dictionary_name.items():
for key, value in person.items():
    print(key, ":", value)

# for value in dictionary_name.values():
for value in person.values():
    print(value)


# 
l_fruit = eval(input("Enter a list of fruits: "))

new_fruit = []

for item in l_fruit:
    if item == "apple":
        swap = item.upper()
        new_fruit.append(swap)
    else:
        new_fruit.append(item)

print(new_fruit)