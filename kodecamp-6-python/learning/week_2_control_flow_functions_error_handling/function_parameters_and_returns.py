# Function parameters and return values
# Run: python3 function_parameters_and_returns.py


def add(a: int, b: int) -> int:
    return a + b


def power(base: float, exp: float = 2) -> float:
    """Default parameter: exp defaults to 2 if omitted."""
    return base**exp


def describe(first: str, last: str, *, title: str = "Mr") -> str:
    """Keyword-only parameter after *: must call as title=..."""
    return f"{title} {first} {last}"


def sum_many(*numbers: int) -> int:
    """*args: collect extra positional arguments into a tuple."""
    total = 0
    for x in numbers:
        total += x
    return total


def build_profile(**fields: str) -> dict[str, str]:
    """**kwargs: collect keyword arguments into a dict."""
    return dict(fields)


print(add(2, 3))
print(power(3))  # 9
print(power(3, 3))  # 27
print(describe("Alan", "Turing", title="Dr"))
print(sum_many(1, 2, 3))
print(build_profile(name="Grace", role="engineer"))
