for i in range(1,8):
    if i>4:
        r1= i-4
    else:
        r1=4-i
    for k in range(0,r1):
        print(end=" ")
    if i==1 or i==7:
        print('*')
        continue
    if i<4:
        r2= 2*i-3
    else:
        r2 = 13-2*i
    print('*'+' '*(r2)+'*',end="")
    print()