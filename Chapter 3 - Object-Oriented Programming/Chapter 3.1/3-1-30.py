#color study
import stddraw
from color import Color
from picture import Picture

#levels of blue and gray
#blue is 0,0,0-255
#grey is all of them same 0-255
width = 16
height = 16
stddraw.setXscale(-1,width)
stddraw.setYscale(-1,height)

t = 0
count = 0
for i in range(width-1,-1,-1):
    for j in range(width-1,-1,-1):
        c1 = Color(t,t,255)
        stddraw.setPenColor(c1)
        stddraw.filledSquare(j,i,0.5)
        count += 1
        t += +1
t = 0
for i in range(0,width):
    for j in range(width-1,-1,-1):
        c2 = Color(t,t,t)
        stddraw.setPenColor(c2)
        stddraw.filledSquare(i,j, .25)

        if t < 255:
            t += 1


stddraw.show()