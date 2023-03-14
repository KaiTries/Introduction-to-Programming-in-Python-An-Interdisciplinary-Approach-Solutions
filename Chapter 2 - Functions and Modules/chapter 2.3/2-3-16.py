#a4 paper
import sys
import stddraw

def draw(n,x0,x1,y0,y1):
    if n == 0: return
    stddraw.line(x0, y0, x1, y0)        #horizontal

    stddraw.line(x1/2, y0, x1/2, y1)        #vertical
    diff = (y1-y0)/2
    draw(n-1,x0,x1/2,y0+diff,y1)
    return



n = 5
stddraw.setPenRadius(0.0)
draw(n, 0, 1, 0.5,1)
stddraw.show()