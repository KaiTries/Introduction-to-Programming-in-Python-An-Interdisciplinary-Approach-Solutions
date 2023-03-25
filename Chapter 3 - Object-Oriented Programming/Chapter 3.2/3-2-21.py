#mutable charges

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

stddraw.setXscale(-100,100)
stddraw.setYscale(-100,100)
MAX_GRAY_SCALE = 255

#initialize array
a = stdarray.create1D(3)
a[0] = Charge(.4, .6, 50)
a[1] = Charge(.5, .5, -5)
a[2] = Charge(.6, .6, 50)





# Create a Picture depicting potential values.
for t in range(100):
    pic = Picture()
    for col in range(pic.width()):
        for row in range(pic.height()):
            # Compute pixel color.
            x = 1.0 * col / pic.width()
            y = 1.0 * row / pic.height()
            v = 0.0
            for i in range(3):
                v += a[i].potentialAt(x, y)    
            v = (MAX_GRAY_SCALE / 2.0)  + (v / 2.0e10)
            if v < 0:
                grayScale = 0
            elif v > MAX_GRAY_SCALE:
                grayScale = MAX_GRAY_SCALE
            else:
                grayScale = int(v)            
            color = Color(grayScale, grayScale, grayScale)
            pic.set(col, pic.height()-1-row, color)
    a[1].increaseCharge(-2.0)
    # Draw the Picture.
    stddraw.picture(pic)
    stddraw.setXscale(-100,100)
    stddraw.setYscale(-100,100)
    stddraw.show(10)
    stddraw.clear


#-----------------------------------------------------------------------