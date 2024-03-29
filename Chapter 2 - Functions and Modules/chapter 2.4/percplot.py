#-----------------------------------------------------------------------
# percplot.py
#-----------------------------------------------------------------------

import sys
import stddraw
import estimate

#-----------------------------------------------------------------------

# Plot to standard draw a graph within the interval [x0, x1] from
# (x0, y0) to (x1, y1) that relates site vacancy probabilities to
# percolation probabilities.

def curve(n, x0, y0, x1, y1, trials=10000, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluate(n,n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve(n, xm, fxm, x1, y1)
    
def curveD(n, x0, y0, x1, y1, trials=10000, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluateD(n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curveD(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curveD(n, xm, fxm, x1, y1)
#-----------------------------------------------------------------------
def curveFast(n, x0, y0, x1, y1, trials=10000, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluateFast(n,n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curveFast(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curveFast(n, xm, fxm, x1, y1)
#-----------------------------------------------------------------------
def curve3D(n, x0, y0, x1, y1, trials=10000, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluate3D(n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve3D(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve3D(n, xm, fxm, x1, y1)
#-----------------------------------------------------------------------
# Accept integer n as a command-line argument. Plot to standard draw
# a graph that relates site vacancy probability (control variable) to
# percolation probability (experimental observations) for a
# n-by-n system.
