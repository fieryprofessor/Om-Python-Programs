from collections import Counter
def f(s):
    c=Counter(s)
    print(sum(v%2 for v in c.values())<=1)
f('civic')
# Output: True
