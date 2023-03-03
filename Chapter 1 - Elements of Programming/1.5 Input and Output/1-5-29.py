import stddraw
import stdio
import sys
import math

R = float(sys.argv[1])
r = float(sys.argv[2])
a = float(sys.argv[3])

stddraw.setXscale(-10,10)
stddraw.setYscale(-10,10)
stddraw.setPenRadius(0.0)
t = 0
while t < 3600:
    x = (R+r)*math.cos(t) - (r+a)*math.cos((R+r)*t/r)
    y = (R+r)*math.sin(t) - (r+a)*math.sin((R+r)*t/r)
    t += 0.01
    stddraw.point(x,y)
    stddraw.show(10)

stddraw.show()
