for i in range(1,5):
    for k in range(0,4-i):
        print(end=" ")
    for j in range(1,i*2):
        print('*',end="")
    print()

for i in range(3,0,-1):
    for k in range(0,3-(i-1)):
        print(end=" ")
    for j in range(1,i*2):
        print('*',end="")
    print()