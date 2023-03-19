import sys
import math
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Draw a Brownian bridge from (x0, y0) to (x1, y1) with the given
# variance and scaleFactor.

def midpoint(x0, y0, x1, y1, var, n):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    xmid = 0.5 * (x0 + x1) + stdrandom.gaussian(0, math.sqrt(var))
    ymid = 0.5 * (y0 + y1) + stdrandom.gaussian(0, math.sqrt(var))

    midpoint(x0, y0, xmid, ymid, var / 2.7, n-1)
    midpoint(xmid, ymid, x1, y1, var / 2.7, n-1)


def main():
    var = 0.3
    n = 10
    stddraw.setXscale(-1, +1)
    stddraw.setYscale(-1, +1)
    stddraw.setPenRadius(0.0)
    midpoint(0, 0, 0, 0, var / math.sqrt(2), n)
    stddraw.show()

if __name__ == '__main__':
    main()
