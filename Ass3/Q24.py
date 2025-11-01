import string
def f(s):
    return s.translate(str.maketrans('','',string.punctuation))
print(f('Hello, world!'))
# Output: Hello world
