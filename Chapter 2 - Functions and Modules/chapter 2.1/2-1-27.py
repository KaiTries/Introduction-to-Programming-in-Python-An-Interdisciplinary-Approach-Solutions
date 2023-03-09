import math
import stdio
import stdarray
import sys

#gaussian formula

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

#-----------------------------------

def scholes(s,x,r,sigma,t):
    a = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)
    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)

s     = float(sys.argv[1])  
x     = float(sys.argv[2])  
r     = float(sys.argv[3])  
sigma = float(sys.argv[4])  
t     = float(sys.argv[5])          

print(scholes(s,x,r,sigma,t))