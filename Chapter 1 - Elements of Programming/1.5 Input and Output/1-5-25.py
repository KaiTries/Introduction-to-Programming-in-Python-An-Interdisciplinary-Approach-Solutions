import stddraw
import random
import sys

stddraw.setXscale(0,1)
stddraw.setYscale(0,1)

n = int(sys.argv[1])
P = float(sys.argv[2])
minr = float(sys.argv[3])
maxr = float(sys.argv[4])
stddraw.setPenRadius(0.0)

for i in range(n):
    p = random.random()
    x = random.random()
    y = random.random()
    r = random.uniform(minr,maxr)
    if p < P:
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledCircle(x,y,r)
    else:
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledCircle(x,y,r)        

stddraw.show()