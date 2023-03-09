#coupon collect norm distr.
import math
import sys
from scipy import special
import stdio
import random
import stdarray


def binomial(n,k,p):
    binom_coeff = special.gammaln(n + 1) - special.gammaln(k + 1) - special.gammaln(n - k + 1)
    probs       = (k * math.log(p)) + ((n - k) * math.log(1-p))
    return math.exp(binom_coeff + probs)

def getcoupon(n,p=0.5):
    x = random.random()
    total = 0
    nmbr = 0
    for i in range(n):
        total += binomial(n,i,p)
        nmbr += 1
        if total > x:
            break

    return nmbr

a = []
for i in range(1000):
    a += [getcoupon(10)]

count = stdarray.create1D(10,0)
for i in range(10):
    for j in range(len(a)):
        if a[j] == i+1:
            count[i] += 1


print(count)