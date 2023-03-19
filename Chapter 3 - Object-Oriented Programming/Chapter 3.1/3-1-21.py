#-----------------------------------------------------------------------
# potential.py
#-----------------------------------------------------------------------
import random
import stdrandom
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
stddraw.setXscale(-100,100)
stddraw.setYscale(-100,100)
MAX_GRAY_SCALE = 255

# Read charges from standard input into an array.
n = 1
charges = stdarray.create1D(n)
for i in range(n):
    x0 = random.random()
    y0 = random.random()
    q0 = stdrandom.gaussian(50,10)
    charges[i] = Charge(x0, y0, q0)


# Create a Picture depicting potential values.
pic = Picture()
for col in range(pic.width()):
    for row in range(pic.height()):
        # Compute pixel color.
        x = 1.0 * col / pic.width()
        y = 1.0 * row / pic.height()
        v = 0.0

        for i in range(n):
            v += charges[i].potentialAt(x, y)    
        v = (MAX_GRAY_SCALE / 2.0)  + (v / 2.0e10)
        if v < 0:
            grayScale = 0
        elif v > MAX_GRAY_SCALE:
            grayScale = MAX_GRAY_SCALE
        else:
            grayScale = int(v)            
        color = Color(grayScale, grayScale, grayScale)
        pic.set(col, pic.height()-1-row, color)

# Draw the Picture.
stddraw.setXscale(-100,100)
stddraw.setYscale(-100,100)
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.setXscale(-100,100)
stddraw.setYscale(-100,100)
stddraw.picture(pic)
stddraw.setXscale(-100,100)
stddraw.setYscale(-100,100)
stddraw.show()


#-----------------------------------------------------------------------