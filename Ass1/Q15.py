p = 1000
r = 0.12

for n in [10, 20, 30]:
    a = p * (1 + r)**n
    print(f"After {n} years: Rs. {a:.2f}")

# Output:
# After 10 years: Rs. 3105.85
# After 20 years: Rs. 9646.29
# After 30 years: Rs. 29959.92