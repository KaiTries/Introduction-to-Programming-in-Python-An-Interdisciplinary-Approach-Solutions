import stdarray
import math
import stdio
import random

def arr(m):
    r = random.randint(1,50)
    x = stdarray.create1D(r,0)
    for i in range(len(x)):
        t = random.randint(0,m-1)
        x[i] = t
    return x



def histogram(m):
    x = arr(m)
    u = stdarray.create1D(m,0)
    for i in range(m):
        for j in range(len(x)):
            if x[j] == i:
                u[i] += 1
    return len(x) == sum(u), u


print(histogram(9))
