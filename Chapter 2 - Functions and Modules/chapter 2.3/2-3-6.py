

def gcd(p, q):
    if q == 0: return p
    return gcd(q, p%q)

a = 25
b = 90
c = 65
d = 70

print(gcd(gcd(a,b),gcd(c,d)))

#this is just the gcd of the gcds given by the 4 params.
#it will most likely be a low number.
#  