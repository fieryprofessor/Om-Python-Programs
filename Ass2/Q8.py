flag = True

while flag:
    n=int(input("Enter the number:"))
    if n>=0:
        flag=False

if n%2==0:
    print(n*2)
else:
    print(n**2)