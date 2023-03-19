#slide show
#names of several pictures as command line arguments
#slideshow:
#every two seconds new pic
#fade effect to black and then black to new picture
from color import Color
from picture import Picture
from instream import InStream
import sys
import stddraw
# Return a new Color object which blends Color objects c1 and c2 using
# alpha as the blending factor.

def blend(c1, c2, alpha):
    r = (1-alpha)*c1.getRed()   + alpha*c2.getRed()
    g = (1-alpha)*c1.getGreen() + alpha*c2.getGreen()
    b = (1-alpha)*c1.getBlue()  + alpha*c2.getBlue()
    return Color(int(r), int(g), int(b))


#fade to black
def fadeBlack(source,width,height):
    pic = Picture(width, height)
    for t in range(11):
        for col in range(width):
            for row in range(height):
                c0 = source.get(col, row)
                cn = Color(0,0,0)
                alpha = float(t) / float(10)
                c = blend(c0, cn, alpha)
                pic.set(col, row, c)
        stddraw.picture(pic)
        stddraw.show(100.0)

#fade from black
def fadePic(source,width,height):
    pic = Picture(width, height)
    for t in range(11):
        for col in range(width):
            for row in range(height):
                cn = source.get(col, row)
                c0 = Color(0,0,0)
                alpha = float(t) / float(10)
                c = blend(c0, cn, alpha)
                pic.set(col, row, c)
        stddraw.picture(pic)
        stddraw.show(100.0)

input = sys.argv[1:]
print(input)
source = Picture(input[0])
width = source.width()
height = source.height()
stddraw.setCanvasSize(width, height)

for i in range(len(input)):
    i = Picture(input[i])
    fadePic(i,width,height)
    stddraw.picture(i)
    stddraw.show(2000)
    fadeBlack(i,width,height)


stddraw.show()
