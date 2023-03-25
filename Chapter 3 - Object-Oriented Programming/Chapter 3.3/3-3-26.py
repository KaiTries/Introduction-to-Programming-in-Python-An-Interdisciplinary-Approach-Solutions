#vector field
#input grid size n
#with point charges as in potential.py
#compute vector associated with potential at every point
from vector import Vector
from charge import Charge
import stdarray
import stdio
import random
# Read charges from standard input into an array.
#-----------------------------------------------------------------------
# potential.py
#-----------------------------------------------------------------------

import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture

# Read values from standard input to create an array of charged
# particles. Set each pixel color in an image to a grayscale value
# proportional to the total of the potentials due to the particles at
# corresponding points. Draw the resulting image to standard draw.
grid = 3
# Read charges from standard input into an array.
n = 2
charges = stdarray.create1D(n)
for i in range(n):
    x0 = random.randint(0,2)
    y0 = random.randint(0,2)
    q0 = 4e-09
    charges[i] = Charge(x0, y0, q0)

# Create a Picture depicting potential values.
gridd = stdarray.create2D(grid,grid,0)
for x in range(grid):
    for y in range(grid):
        # Compute pixel color.
        x = x
        y = y
        v = 0.0
        for i in range(n):
            v += charges[i].potentialAt(x, y)    
        gridd[x][y] = v

print(gridd)



#-----------------------------------------------------------------------