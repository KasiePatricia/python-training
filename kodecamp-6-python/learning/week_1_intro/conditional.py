# Conditional Statements (if, elif, else )

# if statement
age = 20
if age >= 18:
    print("You are an adult")

# if else statement
age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# if elif else statement
age = 20
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Comparison and logical operators
score = 75
has_attendance = True

if score >= 70 and has_attendance:
    print("You passed")
elif score >= 50 or has_attendance:
    print("You are close to passing")
else:
    print("You did not pass")