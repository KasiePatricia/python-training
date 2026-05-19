# Inventory Restock Alert
# Flag items as CRITICAL (< 5) or LOW (5-10). Handle non-integer stock with try/except.

inventory = {
    "milk": 3,
    "bread": 8,
    "eggs": 12,
    "butter": "out of stock",
    "rice": 6,
    "soap": 2,
}


def check_stock_levels(inventory_dict):
    print("\n--- Stock Report ---")
    for item, stock in inventory_dict.items():
        try:
            quantity = int(stock)
        except (TypeError, ValueError):
            print(f"{item}: ERROR — stock must be a number (got {stock!r})")
            continue

        if quantity < 5:
            status = "CRITICAL"
        elif quantity <= 10:
            status = "LOW"
        else:
            status = "OK"

        print(f"{item}: {quantity} units — {status}")


check_stock_levels(inventory)
