# Basic Four-Function Calculator

# Ask for two numbers and then ask for an operation (+, -, *, /).
# Logic: Use if/elif to perform the specific math operation based on the user's choice and print the result.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "-":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operation == "/" and number2 != 0:
    print(f"{number1} / {number2} = {number1 / number2}")
elif operation == "/" and number2 == 0:
    print("Error: Can't divide by zero.")
else:
    print("Invalid operation.")