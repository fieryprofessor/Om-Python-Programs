import math
#a.
x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum1 = 0
sign = 1

for i in range(0, 2*n + 1, 2):
    sum1 += sign * (x**i) / math.factorial(i)
    sign *= -1

print("Sum of series (a):", sum1)

#b.
sum2 = sum((x**i)/math.factorial(i) for i in range(n+1))
print("Sum of series (b):", sum2)

#c.
sum3 = 0
sign = 1
for i in range(1, 2*n, 2):
    sum3 += sign * i
    sign *= -1
print("Sum of series (c):", sum3)

