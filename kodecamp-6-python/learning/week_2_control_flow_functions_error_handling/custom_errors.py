# Raising custom errors
# Run: python3 custom_errors.py


class NegativeValueError(ValueError):
    """Custom exception type (inherits from ValueError)."""


def sqrt_positive(x: float) -> float:
    if x < 0:
        raise NegativeValueError("x must be non-negative")
    return x**0.5


try:
    print(sqrt_positive(9))
    print(sqrt_positive(-1))
except NegativeValueError as e:
    print("Caught:", e)
