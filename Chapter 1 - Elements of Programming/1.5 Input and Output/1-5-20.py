import stddraw
import sys
import random
import math


stddraw.setPenRadius(0.0)
xd=[0.1,0.2,0.3,0.2]
yd=[0.2,0.3,0.2,0.1]
stddraw.polygon(xd,yd)
xd=[0.6,0.7,0.8,0.7]
yd=[0.7,0.8,0.7,0.6]
stddraw.polygon(xd,yd)
stddraw.filledCircle(0.65,0.75,0.075)
stddraw.filledCircle(0.75,0.75,0.075)
stddraw.filledCircle(0.8,0.2,0.075)
stddraw.filledCircle(0.7,0.2,0.075)
stddraw.filledCircle(0.75,0.3,0.075)
xd=[0.85,0.65,0.75]
yd=[0.05,0.05,0.2]
stddraw.polygon(xd,yd)
xd=[0.1,0.2,0.3,0.2]
yd=[0.7,0.8,0.7,0.6]
stddraw.polygon(xd,yd)
stddraw.filledCircle(0.15,0.65,0.075)
stddraw.filledCircle(0.25,0.65,0.075)
xd=[0.15,0.2,0.25]
yd=[0.55,0.7,0.55]
stddraw.polygon(xd,yd)
stddraw.show()