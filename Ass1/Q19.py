meal_cost = float(input("Enter meal cost: "))
tax_rate = 0.05
tip_rate = 0.18

tax = meal_cost * tax_rate
tip = meal_cost * tip_rate
total = meal_cost + tax + tip

print(f"Tax: Rs.{tax:.2f}")
print(f"Tip: Rs.{tip:.2f}")
print(f"Total: Rs.{total:.2f}")

# Output:
# Enter meal cost: 1000
# Tax: Rs.50.00
# Tip: Rs.180.00
# Total: Rs.1230.00