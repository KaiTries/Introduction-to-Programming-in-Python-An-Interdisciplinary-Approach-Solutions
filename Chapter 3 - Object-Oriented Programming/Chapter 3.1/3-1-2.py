from color import  Color
from picture import Picture
import stddraw

r = 123
g = 32
b = 200
c = Color(r,g,b)
pic = Picture(256,256)

for col in range(pic.width()):
    for row in range(pic.height()):
        pic.set(col,row,c)

stddraw.setCanvasSize(pic.width(),pic.height())
stddraw.picture(pic)
stddraw.show()