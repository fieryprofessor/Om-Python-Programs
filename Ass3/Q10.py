from itertools import permutations
def f(s):
    print(set(''.join(p)for p in permutations(s)))
f('abc')
# Output: {'abc','acb','bac','bca','cab','cba'}
