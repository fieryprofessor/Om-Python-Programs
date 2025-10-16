n = int(input("Enter number: "))
fact = 1
i = 1
while fact < n:
    i += 1
    fact *= i
if fact == n:
    print("Factorial number")
else:
    print("Not a factorial number")
