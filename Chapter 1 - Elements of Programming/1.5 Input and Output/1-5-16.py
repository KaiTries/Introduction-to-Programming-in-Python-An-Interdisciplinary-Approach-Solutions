import stdio
import math
import sys




a = []
while not stdio.isEmpty():
    x = stdio.readFloat()
    y = stdio.readFloat()
    m = stdio.readFloat()
    a += [[x,y,m]]


mbig = 0
xbig = 0
ybig = 0
for i in range(len(a)):
    mbig += a[i][2]
    xbig += (a[i][2]*a[i][0])
    ybig += (a[i][2]*a[i][1])

xbig = xbig/mbig
ybig = ybig/mbig

stdio.writef('The centroid mass is %3.0f positioned at x %.3f and y %.3f',mbig,xbig,ybig)