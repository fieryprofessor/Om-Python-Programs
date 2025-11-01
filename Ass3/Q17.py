def f(s):
    return ''.join(c for c in s if c.lower() not in'aeiou')
print(f('python'))
# Output: pythn
