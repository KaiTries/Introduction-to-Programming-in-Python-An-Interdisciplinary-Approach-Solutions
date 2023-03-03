import stddraw
import stdaudio
import math
import scipy
from scipy import constants

# Draw a bouncing ball to standard draw.

RADIUS = .05
DT = 20.0
G = constants.g

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .480
ry = .860
vx = .015
vy = .023
print(G)
while True:
    # Update ball position and draw it there.
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
        #stdaudio.playFile('1')
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
        #stdaudio.playFile('2')        
    rx = rx + vx
    ry = ry + (vy*-G)

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
    