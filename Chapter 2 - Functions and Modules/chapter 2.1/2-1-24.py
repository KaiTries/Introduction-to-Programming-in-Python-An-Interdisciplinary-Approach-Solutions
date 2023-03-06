import math
import sys
import stdio
import stdarray
import sympy


def harmonicSmall(n):
    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / i
    return total


def harmonicLarge(n):
    return math.log(n) + sympy.EulerGamma.evalf() + 1/(2*n) - 1/(12*n**2) + 1/(120*n**4)

def harmonic(n):
    if n < 100:
        return harmonicSmall(n)
    else:
        return harmonicLarge(n)


n = int(sys.argv[1])
result = harmonic(n)
stdio.write(result)