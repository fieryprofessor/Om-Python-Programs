def f(n):
    s=str(n)
    print(n==sum(int(i)**len(s)for i in s))
f(153)
# Output: True
