#write coordinates of random point (a,b,c) on the surface of a sphere

import random
import math
import stdio

while True:
    x = random.random()
    y = random.random()
    if (x*x + y*y) <= 1:
        break

stdio.writeln(str(x) + " " + str(y))

#process

a = 2*x*math.sqrt(1-x*x-y*y)
b = 2*math.sqrt(1-x*x-y*y)
c = 1- 2*(x*x+y*y)

stdio.writeln(str(a) + " " + str(b) + " " + str(c))