row = int(input("Enter row number:"))
col = input("Enter column number:")
if col=='a'or col=='c' or col=='e' or col=='g':
    col=1
else:
    col=0
if (row+col)%2==0:
    print("Black")
else:
    print("White")