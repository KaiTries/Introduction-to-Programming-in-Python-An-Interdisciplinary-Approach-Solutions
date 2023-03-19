#bounding box
#idea to first scan from top and break when we dont get a full line of white space => where color is not 0 0 0
#then scan from the left to right full height stopping same
#then doing it backwards as well
#chosing the bigger values at the end to creat the box
from picture import Picture
from color import Color
import stddraw

#always chose mandril for testing

image = Picture('mandrill.jpg')

width = image.width()
height = image.height()

x1 = 0
x2 = 0
x3 = 0

for row in range(width):
    for col in range(height):
        clr = image.get(row,col)
        if clr.getBlue() != 0 or clr.getGreen() != 0 or clr.getRed() != 0:
            x1 = [row,col]
            break

for col in range(height):
    for row in range(width):
        clr = image.get(row,col)
        if clr.getBlue() != 0 or clr.getGreen() != 0 or clr.getRed() != 0:
            x2 = [row,col]
            break


for col in range(height-1,-1,-1):
    for row in range(width-1,-1,-1):
        clr = image.get(row,col)
        if clr.getBlue() != 0 or clr.getGreen() != 0 or clr.getRed() != 0:
            x3 = [row,col]
            break

print(x1)
print(x2)
print(x3)

#for this picture it makes sense that it is at the outermost pixels e.g  297 for x and 0 for y or the inverse