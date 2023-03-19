#flip horizontally
#we use mandrill again for ease of testing
from picture import Picture
import stddraw

image = Picture('mandrill.jpg')

height = image.height()
width  = image.width()

target = Picture(width,height)

for col in range(width):
    for row in range(height):
        c = image.get(width-1-col,height-1-row)
        target.set(col,row,c)


stddraw.setCanvasSize(target.width(),target.height())
stddraw.picture(image)
stddraw.show(1000)
stddraw.picture(target)
stddraw.show()