# Error handling: try, except, finally
# Run: python3 error_handling.py


def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    finally:
        # runs whether try succeeded or raised (before returning)
        print("(finally: cleanup or logging could go here)")


print(safe_divide(10, 2))
print(safe_divide(10, 0))
