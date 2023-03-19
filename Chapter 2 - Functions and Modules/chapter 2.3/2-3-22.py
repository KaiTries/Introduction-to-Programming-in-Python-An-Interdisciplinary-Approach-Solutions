import stddraw






def draw(n, size, x, y):
    CONST = 2.2
    if n == 0: return
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.filledSquare(x,y,size)
    
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.square(x,y,size)



    draw(n-1,size/CONST,x+size,y+size)
    draw(n-1,size/CONST,x-size,y+size)
    draw(n-1,size/CONST,x+size,y-size)
    draw(n-1,size/CONST,x-size,y-size)

n = 3
stddraw.setPenRadius(0.0)
draw(n, 0.2, 0.5, 0.5)
stddraw.show()

