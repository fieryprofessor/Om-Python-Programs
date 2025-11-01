def f(s):
    print(''.join(chr((ord(c)-96)%26+97)if c.isalpha()else c for c in s))
f('pythonzabc')
# Output: qzuipobbcd
