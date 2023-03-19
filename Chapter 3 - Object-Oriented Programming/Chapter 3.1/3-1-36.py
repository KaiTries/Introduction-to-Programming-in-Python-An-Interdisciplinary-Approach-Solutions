#swirl
#same as rotation but different calculation

from color import Color
from picture import Picture
import math
import stddraw

image = Picture('mandrill.jpg')
width = image.width()
height = image.height()
centerx = width//2
centery = height//2


pic = Picture(width, height)
for col in range(width):
    for row in range(height):
        dCol = float(col) - centerx
        dRow = float(row) - centery
        r = math.sqrt(dCol*dCol + dRow*dRow)
        angle = math.pi / 256.0 * r
        cn = image.get(col, row)
        ti = int((col - centerx) * math.cos(angle) - (row - centery) * math.sin(angle) + centerx)
        tj = int((col - centerx) * math.sin(angle) + (row - centery) * math.cos(angle) + centery)
        pic.set(ti, tj, cn)
stddraw.picture(pic)
stddraw.show()