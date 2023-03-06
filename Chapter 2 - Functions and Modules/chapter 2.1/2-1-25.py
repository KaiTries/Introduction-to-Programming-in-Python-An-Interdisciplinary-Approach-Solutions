import random
import math
import sys
import stddraw
import stdarray

def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = -1.0 + 2.0 * random.random()
        y = -1.0 + 2.0 * random.random()
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r)/r)

def nmbrs(n):
    nmbrs = []
    for i in range(n):
        nmbrs += [gaussian()]
    return nmbrs

n = int(sys.argv[1])
x = nmbrs(n)

a = stdarray.create1D(20,0)
for i in range(len(a)):
    for j in range(len(x)):
        if x[j] >= i*0.05 and x[j] < (i+1)*0.05:
            a[i] += 1
print(a)




#plot the graph
stddraw.setXscale(0,len(a))
stddraw.setYscale(0,max(a))
stddraw.clear()
for k in range(len(a)):
    stddraw.filledRectangle(k + 0.25, 0.0, 0.5, a[k])
stddraw.show()