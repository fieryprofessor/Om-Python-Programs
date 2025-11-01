def f(n):
    s=sorted(set(str(n)),reverse=True)
    print(*s[:3])
f(6328)
# Output: 8 6 3
