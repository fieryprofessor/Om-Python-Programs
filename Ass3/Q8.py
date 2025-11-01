def f(m):
    d={'feb':'28/29','apr':'30','jun':'30','sep':'30','nov':'30'}
    print('No. of days:',d.get(m[:3].lower(),'31'))
f('February')
# Output: No. of days: 28/29
