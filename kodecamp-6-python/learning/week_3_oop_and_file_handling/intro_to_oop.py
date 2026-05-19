# Introduction to Object-Oriented Programming (OOP)
# Run: python3 intro_to_oop.py
#
# OOP is a way to organize code around "things" (objects) that combine:
#   - data (what the thing knows)
#   - behavior (what the thing can do)

print("--- Without OOP: separate variables and functions ---")

student_name = "Ada"
student_grade = 95


def show_report(name, grade):
    print(f"{name}: {grade}%")


show_report(student_name, student_grade)

print()
print("--- With OOP: one object holds related data and actions ---")


class Student:
    def show_report(self):
        print(f"{self.name}: {self.grade}%")


ada = Student()
ada.name = "Ada"
ada.grade = 95
ada.show_report()

print()
print("--- Why OOP helps ---")
print("- Groups related data and functions together")
print("- Makes larger programs easier to read and change")
print("- You can create many objects from one class (e.g. many students)")
