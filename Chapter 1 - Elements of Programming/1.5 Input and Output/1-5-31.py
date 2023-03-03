import stdio
import stddraw
import math
import sys



stddraw.setPenRadius(0.0)

Ax = float(sys.argv[1])
Ay = float(sys.argv[2])
vx = float(sys.argv[3])
vy = float(sys.argv[4])
Ox = math.degrees(float(sys.argv[5]))
Oy = math.degrees(float(sys.argv[6]))
stddraw.setXscale(-Ax,Ax)
stddraw.setYscale(-Ay,Ay)

t = 0
while True:
    x = Ax * math.sin((vx*t) + Ox)
    y = Ay * math.sin((vy*t) + Oy)
    t += 0.01
    stddraw.point(x,y)
    stddraw.show(1)