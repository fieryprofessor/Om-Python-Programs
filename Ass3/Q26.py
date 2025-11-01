def f(s):
    return ''.join('*'if c.lower() in'aeiou'else c for c in s)
print(f('hello'))
# Output: h*ll*
