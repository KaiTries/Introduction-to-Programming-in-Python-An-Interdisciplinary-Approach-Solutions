#wave filter

from color import Color
from picture import Picture
import math
import stddraw

image = Picture('mandrill.jpg')
a = 20
b = 64
width = image.width()
height = image.height()
centerx = width//2
centery = height//2


pic = Picture(width, height)
for col in range(width):
    for row in range(height):
        cn = image.get(col,row)
        ti = col
        tj = int(row + a * math.sin(2 * math.pi * col / b))
        pic.set(ti, tj, cn)
stddraw.picture(pic)
stddraw.show()