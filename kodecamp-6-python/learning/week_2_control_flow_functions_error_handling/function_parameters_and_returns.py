# Function parameters and return values (beginner)
# Run: python3 function_parameters_and_returns.py
#
# A function can take inputs (parameters) and send a value back with return.

print("--- 1. Parameters and return ---")


def add(a, b):
    return a + b


print("2 + 3 =", add(2, 3))

print()
print("--- 2. Save the return value in a variable ---")


def double(n):
    return n * 2


answer = double(5)
print("double(5) =", answer)

print()
print("--- 3. Default parameter (optional argument) ---")


def power(base, exp=2):
    # If you call power(3) only, exp is 2 (square).
    return base**exp


print("3 squared =", power(3))  # uses default exp=2 → 9
print("3 cubed =", power(3, 3))  # pass exp yourself → 27

print()
print("--- 4. Pass arguments by name ---")


def describe(first, last, title="Mr"):
    return f"{title} {first} {last}"


print(describe("Alan", "Turing"))
print(describe("Alan", "Turing", title="Dr"))
