#tree
import stddraw



def tree(n,x0,x1,y0,y1):
    if n == 0:
        return
    midyx = (y1+x1)/2
    stddraw.line(x0,y0,x1,y1)
    stddraw.line(x0,y1,x1+midyx,y1+midyx)

n = 1
stddraw.setPenRadius(0.0)
tree(n,0.5,0.5,0,0.5)
stddraw.show()