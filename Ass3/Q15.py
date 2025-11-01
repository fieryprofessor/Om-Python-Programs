def f(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    print(a)
f(7)
# Output: 8
