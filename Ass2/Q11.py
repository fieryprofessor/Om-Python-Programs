while True:
    print("Enter two numbers:")
    x,y = map(int,input().split())
    print("Enter the operator:")
    op = input()
    if op=='+':
        print(x+y)
    elif op=='-':
        print(x-y)
    elif op=='*':
        print(x*y)
    elif op=='/':
        print(x/y)
    else:
        print("Invalid input") 
    s = input("Do you want to continue or exit:")
    if s=="exit":
        break