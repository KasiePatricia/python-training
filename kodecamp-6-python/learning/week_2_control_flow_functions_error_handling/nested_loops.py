# Nested loops
# Run: python3 nested_loops.py

print("--- nested loops (rows x cols) ---")
for row in range(2):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()
