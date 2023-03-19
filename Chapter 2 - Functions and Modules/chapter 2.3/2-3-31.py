#plasma clouds
import stddraw
import stdrandom
import math






def cloud(x0,y0,x1,y1,variance, scaleFactor):
    if (x1 - x0) < .01:
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledSquare(x0, x1, variance)
        return
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    cloud(x0, y0, xm, ym+delta, variance/scaleFactor, scaleFactor)
    cloud(xm, ym+delta, x1, y1, variance/scaleFactor, scaleFactor)    

hurstExponent = 0.5
stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)
scaleFactor = 2 ** (2.0 * hurstExponent)
cloud(0, .5, 1.0, .5, .01, scaleFactor)
stddraw.show()