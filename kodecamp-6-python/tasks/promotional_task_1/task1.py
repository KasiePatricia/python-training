# The Greatest of Three
# Ask the user to input three different numbers.
# Logic: Use conditional statements to compare them and print which of the three numbers is the largest.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1} is the greatest of the three numbers")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} is the greatest of the three numbers")
else:
    print(f"{number3} is the greatest of the three numbers")
