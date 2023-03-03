import stddraw
import sys
import random
import math



n = int(sys.argv[1])
p = float(sys.argv[2])

radius = 0.25
centerX = 0.5
centerY = 0.5
theta = 2.0*math.pi/n
stddraw.setPenRadius(0.0)
a = []
for i in range(n):
    x = ( radius * math.cos(theta * i) + centerX )
    y = ( radius * math.sin(theta * i) + centerY )
    stddraw.point(x,y)
    a += [[x,y]]

for i in range(len(a)):
    r = random.random()
    if r < p:
        for j in range(i,len(a)):
            stddraw.line(a[i][0],a[i][1],a[j][0],a[j][1])



stddraw.show()
