n = input("Enter the number:")
x=0
if n.isdigit():
    x=1
    n= int(n)

match x:
    case 1: print(n%5)
    case _: print("Invalid input")