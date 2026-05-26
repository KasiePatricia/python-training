# Error handling: try, except, finally
# Run: python3 error_handling.py

import importlib


def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    finally:
        # runs whether try succeeded or raised (before returning)
        print("(finally: cleanup or logging could go here)")


print(safe_divide(10, 2))
print(safe_divide(10, 0))

print()
print("--- Common exceptions (with try/except) ---")




# ZeroDivisionError: division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: cannot divide by zero")

# ValueError: invalid value for the operation
try:
    number = int("abc")
except ValueError:
    print("ValueError: 'abc' is not a valid integer")

# TypeError: wrong type (e.g. can't add str + int)
try:
    total = "hello" + 5
except TypeError:
    print("TypeError: cannot add str and int")

# NameError: variable or name does not exist
try:
    exec("print(undefined_variable)")
except NameError:
    print("NameError: name 'undefined_variable' is not defined")

# IndexError: list index out of range
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("IndexError: list index 10 is out of range")

# KeyError: dictionary key not found
try:
    user = {"name": "Ada"}
    print(user["age"])
except KeyError:
    print("KeyError: key 'age' not in dictionary")

# AttributeError: object has no such attribute or method
try:
    value = "hello".shout()
except AttributeError:
    print("AttributeError: str has no method 'shout'")

# ImportError: name not found inside a module you import from
try:
    from math import not_a_real_function
except ImportError:
    print("ImportError: cannot import name 'not_a_real_function' from math")

# ModuleNotFoundError: no module with that name
try:
    importlib.import_module("this_module_does_not_exist")
except ModuleNotFoundError:
    print("ModuleNotFoundError: no module named 'this_module_does_not_exist'")

# FileNotFoundError: file path does not exist
try:
    with open("no_such_file.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("FileNotFoundError: file 'no_such_file.txt' not found")
