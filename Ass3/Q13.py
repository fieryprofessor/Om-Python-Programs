def f(s):
    v={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n=0
    for i in range(len(s)-1):
        n+=-v[s[i]]if v[s[i]]<v[s[i+1]]else v[s[i]]
    print(n+v[s[-1]])
f('XIV')
# Output: 14
