def f(n):
    d=['zero','one','two','three','four','five','six','seven','eight','nine']
    print(' '.join(d[int(i)]for i in str(n)))
f(123)
# Output: one two three
