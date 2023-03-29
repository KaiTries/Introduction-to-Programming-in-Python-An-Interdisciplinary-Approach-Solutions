
#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
from body import Body 
from instream import InStream
from vector import Vector
from randomBody import RandomBody

#-----------------------------------------------------------------------

class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, n):

        n = n
        radius =  1.25e12 
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            self._bodies[i] = RandomBody()
        self._bodies +=[Body(Vector([0,0]),Vector([0,0]),1.25e28)]
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
                    f[i] += bodyi.forceFrom(bodyj)

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
    dt = 200000
    universe = Universe(4)
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------
