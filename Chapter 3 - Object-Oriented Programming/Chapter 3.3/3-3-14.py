#improved gcd
#return (d,a,b)
#d = gcd and a*p + b*q == d



def gcd(p,q):
    if q == 0: return (p,1,0)
    (d,a,b) = gcd(q,p%q)
    return (d,b, a - (p % q)*b)

