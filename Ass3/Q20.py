def f():
    for i in range(2,101):
        if all(i%j for j in range(2,int(i**0.5)+1)):print(i,end=' ')
f()
# Output: 2 3 5 7 11 13 ... 97
