# Scope: local vs global variables
# Run: python3 scope.py

counter = 0  # global (module-level)


def bump_local() -> None:
    counter = 10  # local: shadows the global name inside this function
    print("inside bump_local:", counter)


def bump_global() -> None:
    global counter
    counter += 1
    print("inside bump_global:", counter)


print("counter before:", counter)
bump_local()
print("counter after bump_local:", counter)  # still 0
bump_global()
print("counter after bump_global:", counter)
