
#-----------------------------------------------------------------------
# bouncingball.py -> make it object oriented
#-----------------------------------------------------------------------

import stddraw
import random
from vector import Vector
import stdarray

class Ball:


    def __init__(self):
        self._radius = 0.01
        self._x = random.uniform(-1,1)
        self._y = random.uniform(-1,1)
        self._vx = random.uniform(-1,1)/1000
        self._vy = random.uniform(-1,1)/1000


    def move(self):
        if abs(self._x) + abs(self._vx) + self._radius > 1:
            self._vx = - self._vx
        if abs(self._y) + abs(self._vy) + self._radius > 1:
            self._vy = - self._vy
        self._x = self._x + self._vx
        self._y = self._y + self._vy

    def draw(self):
        stddraw.setPenRadius(self._radius)
        stddraw.point(self._x,self._y)

# Draw a bouncing ball to standard draw.


def main():
    n = 10
    balls = stdarray.create1D(n,0)
    for i in range(n):
        balls[i] = Ball()
    stddraw.setXscale(-1,1)
    stddraw.setYscale(-1,1)
    while True:
        stddraw.clear(stddraw.GRAY)
        for i in range(n):
            balls[i].draw()
            balls[i].move()
        stddraw.show(1)
    

if __name__ == '__main__': main()