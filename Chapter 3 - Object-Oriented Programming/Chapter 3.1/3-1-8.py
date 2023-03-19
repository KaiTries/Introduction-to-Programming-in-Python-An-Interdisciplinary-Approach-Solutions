#read name of picture file
#given pixel coordinates of rectangle within image
#read a list of color values
#we need to give the color values for which all pixels in the rectangle are compatible
#eg a diff of atleast 128 on the luminance scale

#load picture
#the iterate through the picture only in the rectangle space
#discard the color value if it is not comatible and start with a new one

from picture import Picture
from color import Color
import stddraw
from instream import InStream
import luminance
import sys
#we give an arbitrary rectangle 
top_left = 100,200
bottom_right = 150,150
#these pixels make the rectangle we iterate through

def compatible(c,image):
    for x in range(100,151):            
        for y in range(200,149,-1): 
            c1 = image.get(x,y)
            if not luminance.areCompatible(c1,c):
                return False
    return True

image = Picture('mandrill.jpg')     #this should be sys.argv[1] if you want to feed the image through standard input
width = image.width()
height = image.height()

acceptable = []

instream = InStream('in1.txt')      #input format is 3 integers per line and using a space between them
while instream.hasNextLine():
    x = instream.readLine()
    x = x.split()
    r = int(x[0])
    g = int(x[1])
    b = int(x[2])
    c = Color(r,g,b)
    if compatible(c,image):
            acceptable += [c]

print(acceptable)