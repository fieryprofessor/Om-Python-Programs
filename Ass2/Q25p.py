for i in range(1,6):
    for k in range(0,10-2*i):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for k in range(2,i+1):
        print(k,end=" ")
    print()