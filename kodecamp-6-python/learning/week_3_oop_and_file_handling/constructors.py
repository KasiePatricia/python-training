# Constructors: __init__
# Run: python3 constructors.py
#
# __init__ runs automatically when you create a new object.
# Use it to set starting values instead of setting attributes by hand later.

print("--- __init__ sets up new objects ---")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


book1 = Book("1984", "George Orwell", 328)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(book1.summary())
print(book2.summary())

print()
print("--- Default values in __init__ ---")


class User:
    def __init__(self, username, role="member"):
        self.username = username
        self.role = role

    def greet(self):
        print(f"Hello, {self.username} ({self.role})")


admin = User("kassy", "admin")
guest = User("visitor")

admin.greet()
guest.greet()
