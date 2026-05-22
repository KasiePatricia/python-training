# PROMOTIONAL TASK 2 — Task 1: Automated ATM Simulator
#
# Requirements:
#   - Function: deposit(amount) and withdraw(amount)
#   - Loop: while loop with menu (1 Check Balance, 2 Deposit, 3 Withdraw, 4 Exit)
#   - Conditional: check enough funds before withdrawal
#   - Exception: custom exception + try/except for negative amounts and non-numeric input

# --- Custom exceptions ---
class InsufficientFundsError(Exception):
    """Raised when withdrawal is more than the balance."""


class InvalidAmountError(Exception):
    """Raised when amount is zero, negative, or invalid."""


# --- Account ---
balance = 1000.0


def deposit(amount):
    """Add money to the balance."""
    global balance
    if amount <= 0:
        raise InvalidAmountError("Deposit amount must be greater than zero.")
    balance += amount
    print(f"  Deposited ${amount:.2f}. New balance: ${balance:.2f}")


def withdraw(amount):
    """Take money out if there are enough funds."""
    global balance
    if amount < 0:
        raise InvalidAmountError("Withdrawal amount cannot be negative.")
    if amount == 0:
        raise InvalidAmountError("Withdrawal amount must be greater than zero.")
    if amount > balance:
        raise InsufficientFundsError(
            f"Insufficient funds. You tried ${amount:.2f} but balance is ${balance:.2f}."
        )
    balance -= amount
    print(f"  Withdrew ${amount:.2f}. New balance: ${balance:.2f}")


def run_atm():
    """LOOP: menu runs until user picks 4 (Exit)."""
    print("\n" + "=" * 50)
    print("       Welcome to KassyBank ATM")
    print("=" * 50)

    try:
        while True:
            print(f"\n  Balance: ${balance:.2f}")
            print("  1. Check Balance")
            print("  2. Deposit")
            print("  3. Withdraw")
            print("  4. Exit")

            choice = input("\n  Choose an option (1-4): ").strip()

            if choice == "1":
                print(f"\n  Your current balance is: ${balance:.2f}")

            elif choice == "2":
                try:
                    amount = float(input("  Enter deposit amount: $"))
                    deposit(amount)
                except ValueError:
                    print("  Error: Please enter a valid number.")
                except InvalidAmountError as e:
                    print(f"  Error: {e}")

            elif choice == "3":
                try:
                    amount = float(input("  Enter withdrawal amount: $"))
                    withdraw(amount)
                except ValueError:
                    print("  Error: Please enter a valid number.")
                except (InvalidAmountError, InsufficientFundsError) as e:
                    print(f"  Error: {e}")

            elif choice == "4":
                print("\n  Thank you for using KassyBank. Goodbye!\n")
                break

            else:
                print("  Invalid option. Please choose 1, 2, 3, or 4.")

    except KeyboardInterrupt:
        # Ctrl+C — not a bug; Python stops the program this way
        print("\n\n  Session ended. Goodbye!\n")


if __name__ == "__main__":
    run_atm()
