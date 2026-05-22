# Promotional Task 2 — Stage 2 (100 points)

Four separate programs (one file each). Run any task on its own:

```bash
cd kodecamp-6-python/tasks/promotional_task_2
python3 task1.py
```

## Tasks

| File | What you build |
| --- | --- |
| `task1.py` | **ATM Simulator** — `deposit`, `withdraw`, menu `while` loop, balance check, custom exceptions |
| `task2.py` | **Theater booking** — 10 seats (`False`/`True`), `book_seat`, loop until `0`, `IndexError` message |
| `task3.py` | **Inventory alert** — `check_stock_levels`, `.items()` loop, CRITICAL / LOW, `TypeError` for bad data |
| `task4.py` | **Quiz grader** — 5-question key, `grade_quiz`, `range()` loop, `IndexError` for skipped answers |

Each file lists the full requirements at the top and uses `if __name__ == "__main__":` so only that program runs.

## Concepts used (Week 2)

- **Functions** — logic in named blocks; main code calls `run_atm()`, `book_seat()`, etc.
- **Loops** — `while True` menus; `for` over inventory or quiz questions
- **Conditionals** — `if` / `elif` for menu, stock levels, correct answers
- **Exceptions** — `try` / `except` for bad input and custom `raise` where needed
