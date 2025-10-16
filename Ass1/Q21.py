import math

h = float(input("Enter height (m): "))
vi = 0
a = 9.8

vf = math.sqrt(vi**2 + 2*a*h)
print("Final velocity:", vf, "m/s")

# Output:
# Enter height (m): 20
# Final velocity: 19.799748751599456 m/s