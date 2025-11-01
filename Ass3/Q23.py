def f(s):
    for i,c in enumerate(s):
        if c.lower() in'aeiou':print(i,end=' ')
f('education')
# Output: 0 2 4 6 8
