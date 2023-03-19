#triangle


import stddraw

def draw(n,x0,x1,y0,y1):
    if n == 0: return
    midx = (x0+x1)/2
    midy = (y0+y1)/2
    midx2 = (x0+midx)/2
    midx3 = (x1+midx)/2

    #outer triangle
    stddraw.line(x0,y0,x1,y0)
    stddraw.line(x0,y0,midx,y1)
    stddraw.line(midx,y1,x1,y0)
    #inner triangle
    stddraw.line(midx,y0,midx2,midy)
    stddraw.line(midx,y0,midx3,midy)
    stddraw.line(midx2,midy,midx3,midy)
    stddraw.show(100)
    draw(n-1,x0,midx,y0,midy)
    draw(n-1,midx,x1,y0,midy)
    draw(n-1,midx2,midx3,midy,y1)







n = 5
stddraw.setPenRadius(0.0)
draw(n,0,1,0,1)


stddraw.show()