g = 7

p = 61

A = 30 # = g ^ a % 61

B = 17 # = g ^ b % 61

# s = g ^ (a * b) % 61

# s = 17 ^ a % 61

# s =  30 ^ b % 61

a = 0

b = 0

for x in range(1,50) :
    trial = (g ** x) % p
    if trial == A:
        a = x
        print("a = " + str(x))
    if trial == B:
        b = x
        print("b = " + str(x))
print ("s = " + str(g ** (a + b) % p))


