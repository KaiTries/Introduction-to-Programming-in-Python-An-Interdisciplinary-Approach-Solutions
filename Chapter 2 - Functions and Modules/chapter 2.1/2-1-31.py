#binomial distribution

import math
import stdio
import stdarray
import sys
from scipy import special

def pdf(x, mu=0.0, sigma=1.0):
    x = float(x-mu)/sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma

def cdf(z, mu=0.0, sigma=1.0):
    z = float(z - mu) / sigma
    if z < -8.0: return 0.0
    if z > +8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / i
        i += 2
    return 0.5 + total * pdf(z)

def binomial(n,k,p):
    binom_coeff = special.gammaln(n + 1) - special.gammaln(k + 1) - special.gammaln(n - k + 1)
    probs       = (k * math.log(p)) + ((n - k) * math.log(1-p))
    return math.exp(binom_coeff + probs)


def norm_approx(n,k,p):
    return cdf(k + (1/2),n*p,math.sqrt((n*p)*(1-p))) - cdf(k - (1/2),n*p,math.sqrt((n*p)*(1-p)))

print(binomial(10,7,0.7))


n = int(sys.argv[1])
p = float(sys.argv[2])
total = 0
for i in range(n):
    total += binomial(n,i,p)
    diff = binomial(n,i,p) - norm_approx(n,i,p)
    #stdio.writef('%0.5f \n',diff)

print(total)