def f(a,b):
    while b:a,b=b,a%b
    print(a)
f(48,18)
# Output: 6
