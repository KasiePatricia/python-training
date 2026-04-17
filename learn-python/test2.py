"""
Password Checker Practice Task
Section: Control Structures (if, for, break/continue)

Your task:
Write a program that checks if a password is strong based on these rules:
1. At least 8 characters long
2. Contains at least one digit (0-9)
3. Contains at least one uppercase letter (A-Z)

Steps:
1. Ask the user to enter a password using input()
2. Use len() to check the password length
3. Use a for loop to go through each character in the password
4. Use .isdigit() to check for digits
5. Use .isupper() to check for uppercase letters
6. Use boolean flags (e.g., has_digit = False) to track if conditions are met
7. After the loop, use an if statement to print:
   - "Strong password!" if all conditions are met
   - "Weak password!" otherwise

Bonus (optional):
- Add a check for at least one special character (!, @, #, $, etc.)
- Print which rules the password passed or failed

Good luck! You've learned everything you need for this.
"""

password = input("Enter your password: ")
lengthOfPassword = len(password)

has_digit = False
has_uppercase = False
has_special = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_uppercase = True
    if not char.isalnum():
        has_special = True

if lengthOfPassword >= 8 and has_digit and has_uppercase:
    print("Strong password!")
else:
    print("Weak password!")

if has_special:
    print("✓ Contains special character")
else:
    print("✗ No special character")

if not has_digit:
    print("Password must contain at least one digit.")
if not has_uppercase:
    print("Password must contain at least one uppercase letter.")

print(f"Password passed {lengthOfPassword} characters, {has_digit} digits, {has_uppercase} uppercase, {has_special} special characters.")