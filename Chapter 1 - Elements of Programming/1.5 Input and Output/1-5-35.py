#tile patterns

import stdio
import stddraw
import sys

n = int(sys.argv[1])


stddraw.setXscale(0,n)
stddraw.setYscale(0,n)

for i in range(n):
    for j in range(n):
        if ((i + j) % 2) != 0:
            stddraw.setPenColor(stddraw.WHITE)
        else:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledSquare(i + .5, j + .5, .5)
            xd = [j + 0,j + 0.5,j + 1,j +0.5]
            yd = [i + 0.5,i + 1,i + 0.5,i + 0]
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledPolygon(xd,yd)
            xd = [i + 0,i + 0.5,i + 1,i +0.5]
            yd = [j + 0.5,j + 1,j + 0.5,j + 0]
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledPolygon(xd,yd)
            xd = j + 0
            yd = j + 1
            stddraw.setPenColor(stddraw.DARK_GREEN)
            stddraw.filledCircle(xd,yd,0.25)
            stddraw.filledCircle(xd+2,yd,0.25)

stddraw.show()    




import stddraw


stddraw.setXscale(0,1)
stddraw.setYscale(0,1)

#first Design

stddraw.clear(stddraw.BLACK)
#diamond
xd = [0,0.5,1,0.5]
yd = [0.5,1,0.5,0]
stddraw.setPenColor(stddraw.GRAY)
stddraw.filledPolygon(xd,yd)
#triangle 1
xd = [0,0.25,0.25]
yd = [0.25,0.25,0]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
#triangle 2
xd = [0.75,0.75,1]
yd = [0,0.25,0.25]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
#triangle 3
xd = [0,0.25,0.25]
yd = [0.75,0.75,1]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
#triangle 4
xd = [0.75,0.75,1]
yd = [0.75,1,0.75]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
stddraw.show(5000)

stddraw.clear(stddraw.BLACK)
#second design
#diamond
xd = [0,0.5,1,0.5]
yd = [0.5,1,0.5,0]
stddraw.setPenColor(stddraw.GRAY)
stddraw.filledPolygon(xd,yd)
#rectangle 1
stddraw.setPenColor(stddraw.WHITE)
xd = [0,0.125,0.375,0.25]
yd = [0.25,0.375,0.125,0]
stddraw.filledPolygon(xd,yd)
#square 2
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledSquare(0.875,0.125,0.125)
#triangle 3
xd = [0,0.25,0.25]
yd = [0.75,0.75,1]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
#triangle 4
xd = [0.75,0.75,1]
yd = [0.75,1,0.75]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
stddraw.show(5000)

stddraw.clear(stddraw.BLACK)
#second design
#diamond
xd = [0,0.5,1,0.5]
yd = [0.5,1,0.5,0]
stddraw.setPenColor(stddraw.GRAY)
stddraw.filledPolygon(xd,yd)
#rectangle 1
stddraw.setPenColor(stddraw.WHITE)
xd = [0,0.125,0.375,0.25]
yd = [0.25,0.375,0.125,0]
stddraw.filledPolygon(xd,yd)
#suare 1
stddraw.setPenColor(stddraw.GRAY)
stddraw.filledSquare(0.125,0.125,0.125)
#square 2
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledSquare(0.875,0.125,0.125)
#triangle 3
xd = [0,0.25,0.25]
yd = [0.75,0.75,1]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
#triangle 4
xd = [0.75,0.75,1]
yd = [0.75,1,0.75]
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledPolygon(xd,yd)
stddraw.show(5000)
