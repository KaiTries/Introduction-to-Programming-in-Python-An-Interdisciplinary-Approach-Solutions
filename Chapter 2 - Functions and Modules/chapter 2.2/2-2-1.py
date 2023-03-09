#hyperbolic

import sys
import math
import stdio

def sinh(x):
    return (math.exp(x)-math.exp(-x))/2

def cosh(x):
    return (math.exp(x)+math.exp(-x))/2

def tanh(x):
    return sinh(x) / cosh(x)

def coth(x):
    return cosh(x) / sinh(x)

def sech(x):
    return 1 / cosh(x)

def csch(x):
    return 1 / sinh(x)



def main():
    x = float(sys.argv[1])
    stdio.writeln(sinh(x))
    stdio.writeln(cosh(x))
    stdio.writeln(tanh(x))
    stdio.writeln(coth(x))
    stdio.writeln(sech(x))
    stdio.writeln(csch(x))


if __name__ == '__main__': main()