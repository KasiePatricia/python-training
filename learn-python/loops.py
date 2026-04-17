# loops

# for loops
names = ["John", "Jane", "Jim", "Jill"]
for name in names:
    print("Hello", name)

for letter in "Python":
    print(letter)

for i in range(10):
    print("Hello", i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)
# while loops
count = 0
while count < 5:
    print("Counting:", count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

# nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# nested loops with break and continue
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)

