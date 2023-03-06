import math
import stdio
import stdarray

def rescale(a):
    if min(a) < 0:
        return stdio.writeln("array must be strictly positive")
    else:
        dif = max(a) - min(a)
        for i in range(len(a)):
            a[i] = (a[i] - min(a))/dif
    return a
