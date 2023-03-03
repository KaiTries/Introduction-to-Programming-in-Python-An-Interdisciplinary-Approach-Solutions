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
