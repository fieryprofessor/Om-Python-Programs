import math
e_pi = math.e ** math.pi
pi_e = math.pi ** math.e

print("e^π =", e_pi)
print("π^e =", pi_e)

if e_pi > pi_e:
    print("ok")
else:
    print("ok anyway")

# Output:
# e^π = 23.140692632779263
# π^e = 22.459157718361045
# ok
