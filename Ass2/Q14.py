room = int(input("Enter the room type: Standard:1, Deluxe: 2, Suite:3"))
season = int(input("Enter the season: Peak:1, Off:2"))
loyalty = input("Are you a loyal member: (y/n)")
days = int(input("Enter the number of days you will stay:"))
bill = amt = 0

if room==1:
    amt=100
elif room==2:
    amt=150
else:
    amt=250

if season==1:
    amt = amt + (amt*(20/100))
elif season==2:
    amt = amt - (amt*(15/100))

amt *= days 
dis =0
if days>3 and days<=7:
    dis += 10
elif days>7:
    dis += 20

if loyalty=='y':
    dis += 5

bill = amt - (amt*(dis/100))
print("Your bill is:",bill)


