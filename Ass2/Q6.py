n = int(input("Enter the number:"))
c=0
i=1
while i<=n:
    if(n%i==0):
        c +=1
    i +=1
if c==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")