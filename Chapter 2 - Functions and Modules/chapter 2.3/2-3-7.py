def gcd(p, q):
    if q == 0: return p
    return gcd(q, p%q)


def gcdlike(p,q):
    if q == 0: return p == 1
    return gcdlike(q, p % q)

#although similiar they are different in the base output: The first function will return the gcd, while the other will return a boolean value.
#this boolean value will be True if P is equal to 1, which is only the case if the numbers are coprime.
#so this checks if numbers are coprime

print(gcdlike(17,7))
#Output: True