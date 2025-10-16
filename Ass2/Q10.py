s = input("Enter the string:")
n = len(s)
for i in range(0,n):
    temp= ""
    for j in range(i,n):
        temp+=s[j]
        print(temp)