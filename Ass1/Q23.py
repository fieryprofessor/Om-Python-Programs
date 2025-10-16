n = int(input("Enter a 4-digit number: "))
total = sum(int(d) for d in str(n))
print("Sum of digits =", total)

# Output:
# Enter a 4-digit number: 1234
# Sum of digits = 10