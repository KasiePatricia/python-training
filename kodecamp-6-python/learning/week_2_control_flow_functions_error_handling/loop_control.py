# Loop control: break, continue, pass
# Run: python3 loop_control.py

print("--- break (exit loop early) ---")
for i in range(10):
    if i == 3:
        break
    print(i, end=" ")
print()

print("--- continue (skip rest of iteration) ---")
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
print()

# pass: placeholder (no-op); useful for stubs or empty blocks syntactically

# while loop
n = 0
while n < 3:
    print(n)
    n += 1