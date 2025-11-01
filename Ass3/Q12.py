from datetime import datetime,timedelta
def f(d,day,n):
    nd=datetime.fromisoformat(d)+timedelta(n)
    print('New date:',nd.date(),'New day:',nd.strftime('%A'))
f('2024-08-27','Tuesday',5)
# Output: New date: 2024-09-01 New day: Sunday
