n = int(input("Enter the number:"))

sum=0
for i in range(1,n):
    c=0
    j=1
    while j<=n:
        if(i%j==0):
            c +=1
        j +=1
    if c==2:
        sum+=i
print(sum)    