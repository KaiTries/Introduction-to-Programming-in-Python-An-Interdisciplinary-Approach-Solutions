#tile 
from picture import Picture
from outstream import OutStream
import stddraw


image = Picture('mandrill.jpg')



m = 2
n = 2

width = image.width()
height = image.height()
stddraw.setCanvasSize(width,height)


width2 = width//m
height2 = height//n

crop = Picture(width2,height2)
for col in range(width2):
    for row in range(height2):
        x = image.get(col,row)
        crop.set(col,row,x)


stddraw.picture(crop)
stddraw.show()