n = int(input("Enter number: "))
i = 2
print("Factors:", end=' ')
while n > 1:
    if n % i == 0:
        print(i, end=' ')
        n //= i
    else:
        i += 1
