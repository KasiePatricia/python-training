# Classes and objects
# Run: python3 classes_and_objects.py
#
# A class is a blueprint. An object is one thing built from that blueprint.

print("--- Define a class ---")


class Dog:
    pass  # empty for now; we'll add details in later files


print("Dog is a class (blueprint):", Dog)

print()
print("--- Create objects (instances) ---")


buddy = Dog()
luna = Dog()

print("buddy:", buddy)
print("luna:", luna)
print("Same class?", type(buddy) is Dog)
print("Same object?", buddy is luna)

print()
print("--- Each object is its own thing ---")

buddy.name = "Buddy"
luna.name = "Luna"

print(buddy.name)
print(luna.name)
