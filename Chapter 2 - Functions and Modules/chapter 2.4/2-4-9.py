#using percplot with other functions
import stddraw
import math

def curve(x0, y0, x1, y1, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = math.sin(xm) + math.cos(10*ym)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve(x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve(xm, fxm, x1, y1)

stddraw.setXscale(0,2)
stddraw.setYscale(-1,2)
curve(0,0,1,1)
stddraw.show()