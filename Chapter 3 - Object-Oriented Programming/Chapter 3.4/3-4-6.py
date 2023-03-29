
#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
from body import Body 
from instream import InStream
from vector import Vector

#-----------------------------------------------------------------------

class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, +3*radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx   = instream.readFloat()
            ry   = instream.readFloat()
            vx   = instream.readFloat()
            vy   = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)

    # Simulate the passing of dt seconds in self.
    
    def increaseTime(self, dt):
        
        # Initialize the forces to zero.
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))
        
        # Compute the forces.
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)

        # Move the bodies.
        for i in range(n):
            self._bodies[i].move(f[i], dt)    

    # Draw self to standard draw.
    def draw(self,x):
        for body in self._bodies:
            body.draw(x)

#-----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.
stddraw.setCanvasSize(800,400)
def main():
    filename = 'universe.txt'
    filename2 = 'universe2.txt'
    dt = 20000
    universe = Universe(filename)
    universe2 = Universe(filename2)

    while True:
        universe.increaseTime(dt)
        universe2.increaseTime(dt)
        stddraw.clear()
        universe.draw(0)
        universe2.draw(2*1.25e11)
        stddraw.show(10)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------