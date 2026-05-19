# Automated ATM Simulator
# Create a command-line bank account with deposit/withdraw, a menu loop,
# balance checks before withdrawal, and error handling for invalid input.

balance = 0.0


class InvalidAmountError(Exception):
    """Raised when deposit or withdrawal amount is negative."""


def deposit(amount):
    if amount < 0:
        raise InvalidAmountError("Deposit amount cannot be negative.")
    global balance
    balance += amount
    print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")


def withdraw(amount):
    if amount < 0:
        raise InvalidAmountError("Withdrawal amount cannot be negative.")
    global balance
    if amount > balance:
        print("Insufficient funds.")
        return
    balance -= amount
    print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")


def read_amount(action):
    try:
        amount = float(input(f"Enter amount to {action}: "))
    except ValueError:
        print("Please enter a valid number.")
        return None
    return amount


while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your balance is: ${balance:.2f}")

    elif choice == "2":
        amount = read_amount("deposit")
        if amount is None:
            continue
        try:
            deposit(amount)
        except InvalidAmountError as e:
            print(e)

    elif choice == "3":
        amount = read_amount("withdraw")
        if amount is None:
            continue
        try:
            withdraw(amount)
        except InvalidAmountError as e:
            print(e)

    elif choice == "4":
        print("Thank you. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
