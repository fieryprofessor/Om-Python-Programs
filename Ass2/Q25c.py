for i in range(4,0,-1):
    for k in range(4-i,0,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()