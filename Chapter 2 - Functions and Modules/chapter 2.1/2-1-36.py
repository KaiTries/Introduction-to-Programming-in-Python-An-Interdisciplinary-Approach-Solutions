import math
import sys
import stdio
import random
import stddraw
import stdarray
stddraw.setYscale(-1,1)
stddraw.setXscale(-1,25)
stddraw.setPenRadius(0.0)

print(math.radians(-10+0.04))
print(math.radians(9))
n = 5
t = math.radians(-10)
steps = 0.00
y = 0

def fourir(t,n):
    x = math.cos(t)
    for i in range (2,n):
        x += math.cos(i*t)
    return (x/n)





while steps < 20:
    x = fourir(t,n)
    stddraw.point(y,x)
    t += 0.04
    steps += 0.04
    y += 0.04

stddraw.show()
#from -10 to 10, we have 500 t points