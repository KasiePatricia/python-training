# ============================================================
#         PYTHON ERRORS - Simple Reference Guide
# ============================================================
# HOW TO USE THIS FILE:
#   - Read through the examples to learn each error
#   - To TEST an error: uncomment the code under "Try it"
#   - Run the file and read the error message Python gives you
#   - Re-comment it when done, then try the next one
# ============================================================


# ------------------------------------------------------------
# 1. SyntaxError — Code is written incorrectly
# ------------------------------------------------------------
# Python can't even read the code. Usually a missing symbol.
#
# Try it (remove the # to test):
# if True
#     print("Hello")        # ❌ Missing colon :


# ------------------------------------------------------------
# 2. IndentationError — Wrong spacing/indentation
# ------------------------------------------------------------
# Python uses indentation (spaces) to understand structure.
#
# Try it:
# def greet():
# print("Hello")            # ❌ Should be indented


# ------------------------------------------------------------
# 3. NameError — Variable doesn't exist
# ------------------------------------------------------------
# You're using a variable you never created.
#
# Try it:
# print(age)                # ❌ age was never defined


# ------------------------------------------------------------
# 4. TypeError — Wrong data type
# ------------------------------------------------------------
# Mixing types that don't work together.
#
# Try it:
# result = "5" + 3          # ❌ Can't add string and number


# ------------------------------------------------------------
# 5. ValueError — Right type, wrong value
# ------------------------------------------------------------
# The type is correct but the value makes no sense.
#
# Try it:
# int("hello")              # ❌ "hello" can't become a number


# ------------------------------------------------------------
# 6. IndexError — List position doesn't exist
# ------------------------------------------------------------
# You're asking for an item that isn't there.
#
# Try it:
# numbers = [1, 2, 3]
# print(numbers[5])         # ❌ Only indexes 0, 1, 2 exist


# ------------------------------------------------------------
# 7. KeyError — Dictionary key doesn't exist
# ------------------------------------------------------------
# Like IndexError but for dictionaries.
#
# Try it:
# person = {"name": "John"}
# print(person["age"])      # ❌ "age" key doesn't exist


# ------------------------------------------------------------
# 8. AttributeError — Object doesn't have that feature
# ------------------------------------------------------------
# You're calling a method that doesn't belong to that type.
#
# Try it:
# x = 10
# x.append(5)               # ❌ Numbers don't have append()


# ------------------------------------------------------------
# 9. ZeroDivisionError — Dividing by zero
# ------------------------------------------------------------
# Math rule: you can't divide anything by zero.
#
# Try it:
# x = 10 / 0                # ❌ Undefined in math


# ------------------------------------------------------------
# 10. FileNotFoundError — File doesn't exist
# ------------------------------------------------------------
# You're trying to open a file Python can't find.
#
# Try it:
# open("file.txt")          # ❌ No such file exists


# ------------------------------------------------------------
# 11. ImportError / ModuleNotFoundError — Module not found
# ------------------------------------------------------------
# You're trying to import something that isn't installed.
#
# Try it:
# import blahblah           # ❌ Not a real module


# ------------------------------------------------------------
# 12. AssertionError — A condition you expected is False
# ------------------------------------------------------------
# assert is like saying "I'm sure this is true" — if not, it crashes.
#
# Try it:
# x = 5
# assert x > 10             # ❌ 5 is not greater than 10


# ------------------------------------------------------------
# 13. RuntimeError — Something went wrong while running
# ------------------------------------------------------------
# A general error raised when nothing else fits.
#
# Try it:
# raise RuntimeError("Oops, something broke!")


# ------------------------------------------------------------
# 14. OverflowError — Number is too large
# ------------------------------------------------------------
# The result of a calculation is beyond what Python can handle.
#
# Try it:
# import math
# math.exp(1000)            # ❌ Result is astronomically large


# ------------------------------------------------------------
# 15. MemoryError — Ran out of memory
# ------------------------------------------------------------
# You're asking Python to store more than your system can handle.
# WARNING: This may freeze/crash your computer. Read only!
#
# DO NOT run this:
# big_list = [1] * (10**10) # ❌ 10 billion items — way too much


# ============================================================
#   HOW TO HANDLE ERRORS  (so your program doesn't crash)
# ============================================================
#
# Use try...except to catch errors gracefully:
#
# try:
#     x = 10 / 0            # This will cause an error
# except ZeroDivisionError:
#     print("You can't divide by zero!")
#
# You can also catch ANY error like this:
#
# try:
#     int("hello")
# except Exception as e:
#     print("Something went wrong:", e)
#
# ============================================================
#   MOST COMMON ERRORS (you'll see these the most)
# ============================================================
#   1. SyntaxError     — typo or missing symbol in your code
#   2. NameError       — used a variable before creating it
#   3. TypeError       — mixed the wrong types together
#   4. IndexError      — asked for a list item that isn't there
#   5. KeyError        — asked for a dictionary key that isn't there
# ============================================================