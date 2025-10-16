a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

mn = min(a,b,c)
mx = max(a,b,c)
mid = (a+b+c) - mn - mx

print("Sorted:", mn, mid, mx)

# Output:
# Enter first: 30
# Enter second: 10
# Enter third: 20
# Sorted: 10 20 30
