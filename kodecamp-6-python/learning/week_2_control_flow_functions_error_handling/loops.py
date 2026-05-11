# Loops: for and while
# Run: python3 loops.py

# for: iterate over a sequence (or anything iterable)
print("--- for loop (range) ---")
for i in range(3):
    print(i)  # 0, 1, 2

print("--- for loop (list) ---")
for fruit in ["apple", "banana"]:
    print(fruit)

# while: repeat while a condition is True
print("--- while loop ---")
n = 0
while n < 3:
    print(n)
    n += 1
