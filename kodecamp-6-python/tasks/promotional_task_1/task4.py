# The Multi-Discount Shop

# Ask the user for their total bill amount.
# The Task:
# If the bill is over $100, apply a 20% discount.
# If it's over $50, apply a 10% discount.
# Otherwise, no discount. Print the final total.

bill = float(input("Enter your total bill amount: "))

if bill > 100:
    discount = bill * 0.2
    final_total = bill - discount
    print(f"Your final total after 20% discount is ${final_total:.2f}")
elif bill > 50:
    discount = bill * 0.1
    final_total = bill - discount
    print(f"Your final total after 10% discount is ${final_total:.2f}")
else:
    print(f"No discount applied. Your final total is ${bill:.2f}")