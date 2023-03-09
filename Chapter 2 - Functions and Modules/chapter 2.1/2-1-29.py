import math
import stdarray
import stdio
import sys

def evaluate(x,a):
    total = 0.0
    for i in range(len(a)-1,-1,-1):
        total = a[i] + (x * total)
    return total

def exp(n,x):
    a    = stdarray.create1D(n,0)
    a[0] = 1
    for i in range(1,n):
        a[i] = a[i-1] / float(i)
    return evaluate(x,a)


x = float(sys.argv[1])
n = int(sys.argv[2])

print(exp(n,x))
print(math.exp(x))