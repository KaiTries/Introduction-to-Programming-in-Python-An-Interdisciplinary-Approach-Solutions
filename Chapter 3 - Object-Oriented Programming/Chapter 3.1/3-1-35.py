#rotation filter


#name of picture and real number theta
from color import Color
from picture import Picture
import math
import stddraw

image = Picture('mandrill.jpg')
theta = 0.05
width = image.width()
height = image.height()
centerx = width//2
centery = height//2


pic = Picture(width, height)
for t in range(11):
    for col in range(width):
        for row in range(height):
            cn = image.get(col, row)
            ti = int((col - centerx) * math.cos(theta) - (row - centery) * math.sin(theta) + centerx)
            tj = int((col - centerx) * math.sin(theta) + (row - centery) * math.cos(theta) + centery)
            pic.set(ti, tj, cn)
    stddraw.picture(pic)
    stddraw.show()