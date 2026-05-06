# User Input and Output

# User input
name = input("Enter your name: ")
age = input("Enter your age: ")

# User output
print("Hello, " + name + "! You are " + age + " years old.")

# every output is a string
print(type(name))
print(type(age))

# convert input to Numbers
age = int(age)
print(type(age))

# convert input to Floats
age = float(age)
print(type(age))