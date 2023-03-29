
#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
from body import Body 
from instream import InStream
from vector import Vector
from vector2 import Vector2
#-----------------------------------------------------------------------

class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, filename,d):
        self._d = d
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx = []
            vx = []
            for j in range(d):
                rx  += [instream.readFloat()]
            for j in range(d):
                vx  += [instream.readFloat()]
            mass = instream.readFloat()
            r = Vector(rx)
            v = Vector(vx)
            self._bodies[i] = Body(r, v, mass)
            print(r,v)

    # Simulate the passing of dt seconds in self.
    
    def increaseTime(self, dt):
        
        # Initialize the forces to zero.
        n = len(self._bodies)
        array = []
        for i in range(self._d):
            array += [0]
        f = stdarray.create1D(n, Vector(array))
        
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
    def draw(self):
        for body in self._bodies:
            body.draw(0)

#-----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.

def main():
    filename = 'universe.txt'
    dt = 20000
    universe = Universe(filename,3)
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------
