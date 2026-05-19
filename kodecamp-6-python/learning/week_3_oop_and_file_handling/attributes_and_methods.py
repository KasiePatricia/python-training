# Attributes and methods
# Run: python3 attributes_and_methods.py
#
# Attribute = data stored on an object (e.g. name, age)
# Method = function defined inside a class (behavior)

print("--- Attributes and methods on a class ---")


class BankAccount:
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show_balance(self):
        print(f"Balance: ${self.balance:.2f}")


account = BankAccount()
account.balance = 100.0  # attribute

account.deposit(50)  # method
account.show_balance()

account.withdraw(30)
account.show_balance()

print()
print("--- Class attribute (shared by all objects) ---")


class Counter:
    step = 1  # same for every Counter unless changed on one object

    def tick(self):
        self.value = self.value + self.step


a = Counter()
a.value = 0
b = Counter()
b.value = 10

a.tick()
b.tick()
print("a.value:", a.value)
print("b.value:", b.value)
