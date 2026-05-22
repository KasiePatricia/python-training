# PROMOTIONAL TASK 2 — Task 3: Inventory Restock Alert
#
# Requirements:
#   - Dictionary of items and stock quantities
#   - Function: check_stock_levels(inventory_dict)
#   - Loop: for item, qty in inventory_dict.items()
#   - Conditional: below 5 → "CRITICAL"; between 5 and 10 → "LOW"
#   - Exception: try/except TypeError if stock is text (e.g. "out of stock")

store_inventory = {
    "Bottled Water (24pk)": 3,
    "Instant Noodles": 7,
    "AAA Batteries": "out of stock",
    "Notebooks A4": 14,
    "Hand Sanitizer": 4,
    "Bananas": 9,
    "Pens": 2,
    "Gum": 10,
}


def check_stock_levels(inventory_dict):
    """Print a report for every item in the store."""
    print("\n" + "=" * 50)
    print("       Inventory Restock Report")
    print("=" * 50)

    for item, qty in inventory_dict.items():
        try:
            if qty < 5:
                status = "CRITICAL"
            elif qty <= 10:
                status = "LOW"
            else:
                status = "OK"

            print(f"  {item:<28} {qty:>4} units  |  {status}")

        except TypeError:
            print(
                f"  {item:<28}  ---------- |  "
                f"Invalid stock value recorded: '{qty}'."
            )

    print()


if __name__ == "__main__":
    check_stock_levels(store_inventory)
