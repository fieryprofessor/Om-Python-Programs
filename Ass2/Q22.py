n = int(input("Enter number: "))
while n >= 10:
    n = sum(int(d) for d in str(n))
print("Single digit sum:", n)
