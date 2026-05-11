# Secret Number Guessing Game

# Hardcode a "secret" number (like 7) at the top of your code. Ask the user to guess it.
# The Task:
# If the guess is too high, print "Lower!"
# If the guess is too low, print "Higher!"
# If they get it right, print "You win!"

secret_number = 39
guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("You win!")
elif guess > secret_number:
    print("Lower!")
else:
    print("Higher!")