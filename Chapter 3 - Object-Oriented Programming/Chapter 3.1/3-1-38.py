#glass

from color import Color
from picture import Picture
import math
import stddraw
import stdrandom


image = Picture('mandrill.jpg')
width = image.width()
height = image.height()

pic = Picture(width, height)
for col in range(width):
    for row in range(height):
        ti = (width + col + stdrandom.uniformInt(-5,6))%width
        tj = (height + row + stdrandom.uniformInt(-5,6))%height
        cn = image.get(ti,tj)
        pic.set(col, row, cn)
stddraw.picture(pic)
stddraw.show()