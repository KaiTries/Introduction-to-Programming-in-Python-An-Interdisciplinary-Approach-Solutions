#split image into red blue and green
#use mandrill again for ease of testing
from picture import Picture
from color import Color
import stddraw

image = Picture('mandrill.jpg')

width = image.width()
height = image.height()
c = Color()
targetBlue = Picture(width,height)
targetRed = Picture(width,height)
targetGreen = Picture(width,height)

for col in range(width):
    for row in range(height):
        x = image.get(col,row)
        b = x.getBlue()
        cb = Color(0,0,b)
        r = x.getRed()
        cr = Color(r,0,0)
        g = x.getGreen()
        cg = Color(0,g,0)
        targetRed.set(col,row,cr)
        targetGreen.set(col,row,cg)
        targetBlue.set(col,row,cb)


stddraw.setCanvasSize(image.width(),image.height())
stddraw.picture(targetRed)
stddraw.show(1000)
stddraw.picture(targetGreen)
stddraw.show(1000)
stddraw.picture(targetBlue)
stddraw.show()