# Function parameters — advanced (*args, **kwargs, keyword-only)
# Run after: function_parameters_and_returns.py
# Run: python3 function_parameters_and_returns_advanced.py


def describe(first: str, last: str, *, title: str = "Mr") -> str:
    """After *, title must be passed as title=... (keyword-only)."""
    return f"{title} {first} {last}"


def sum_many(*numbers: int) -> int:
    """*numbers collects extra positional arguments into a tuple."""
    total = 0
    for x in numbers:
        total += x
    return total


def build_profile(**fields: str) -> dict[str, str]:
    """**fields collects keyword arguments into a dict."""
    return dict(fields)


print(describe("Alan", "Turing", title="Dr"))
print(sum_many(1, 2, 3))
print(build_profile(name="Grace", role="engineer"))
