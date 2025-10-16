for i in range(1,6):
    for k in range(0,9-(i*2)):
        if i==1:
            print(' '*8,end="")
            break
        else:
            print(end=" ")
    if i==2 or i==3 or i==4:
        print('*'+" "*(i*4-3)+'*',end="")
    if i==1:
        print('*',end="")
    if i==5:    
        print('* '*9,end="")
    print()    