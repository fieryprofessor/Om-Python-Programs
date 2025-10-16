days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

total_seconds = days*86400 + hours*3600 + minutes*60 + seconds
print("Total seconds =", total_seconds)

# Output:
# Days: 1
# Hours: 1
# Minutes: 1
# Seconds: 1
# Total seconds = 90061