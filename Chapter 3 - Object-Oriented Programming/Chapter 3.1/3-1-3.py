import sys
import stddraw
from color import Color

#-----------------------------------------------------------------------

# Accept integers r1, g1, b1, r2, g2, and b2 as command-line arguments.
# Draw to standard draw Albers squares using colors (r1, g1, b1) and
# (r2, g2, b2).
r1 = 123
g1 = 32
b1 = 200
c1 = Color(r1, g1, b1)

r2 = 3
g2 = 90
b2 = 5
c2 = Color(r2, g2, b2)

r3 = 199
g3 = 12
b3 = 154
c3 = Color(r3, g3, b3)

stddraw.setCanvasSize(2*512, 2*256)
stddraw.setYscale(0,1)
stddraw.setXscale(0,2)

#C1 big
stddraw.setPenColor(c1)
stddraw.filledSquare(.25, .25, .2)

stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .25, .1)

stddraw.setPenColor(c1)
stddraw.filledSquare(1, .25, .2)

stddraw.setPenColor(c3)
stddraw.filledSquare(1, .25, .1)

#C2 big
stddraw.setPenColor(c2)
stddraw.filledSquare(1.75, .25, .2)

stddraw.setPenColor(c1)
stddraw.filledSquare(1.75, .25, .1)

stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .75, .2)

stddraw.setPenColor(c3)
stddraw.filledSquare(.25, .75, .1)

#C3 big

stddraw.setPenColor(c3)
stddraw.filledSquare(1, .75, .2)

stddraw.setPenColor(c2)
stddraw.filledSquare(1, .75, .1)

stddraw.setPenColor(c3)
stddraw.filledSquare(1.75, .75, .2)

stddraw.setPenColor(c1)
stddraw.filledSquare(1.75, .75, .1)
stddraw.show()
