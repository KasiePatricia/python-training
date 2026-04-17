# tuples
dimensions = (200, 40)

print(dimensions[0])

person = ("John", 20, "Male")

width, height = dimensions
print(width)
print(height)

# tuples are immutable
dimensions[0] = 100
print(dimensions) # this will raise an error TypeError: 'tuple' object does not support item assignment

# set is a collection of unique elements
letters = set("abc")
print(letters)
print("a" in letters) # True
print("e" not in letters) # True

letters.add("d")
print(letters)

letters.remove("b")
print(letters)

letters.discard("e")
print(letters)

numbers = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
another_numbers = set[int]([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(numbers.union(another_numbers)) # {1, 2, 3, 4, 5}
print(numbers.intersection(another_numbers)) # {1, 2, 3, 4, 5}
print(numbers.difference(another_numbers)) # numbers - another_numbers # {1, 2, 3, 4, 5}
print(numbers.symmetric_difference(another_numbers)) # numbers ^ another_numbers # {1, 2, 3, 4, 5}
print(numbers.issubset(another_numbers)) # numbers <= another_numbers # True
print(numbers.issuperset(another_numbers)) # numbers >= another_numbers # True
print(numbers.isdisjoint(another_numbers)) # numbers.isdisjoint(another_numbers) # False