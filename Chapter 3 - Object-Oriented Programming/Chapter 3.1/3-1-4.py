#name of a grayscale pic file as argument use stddraw to plot histogram of the frequency of occurence of the 256 grayscale intensities
#we use mandrill.jpg grayscale as test
from color import Color
from picture import Picture
import stddraw
import stdarray
import stdstats

image = Picture('mandrillGrey.jpg')

width = image.width()
height = image.height()

count = stdarray.create1D(256,0)


for col in range(width):
    for row in range(height):
        x = image.get(col,row)
        x = x.getBlue()
        count[x] += 1

stddraw.setXscale(0,len(count))
stddraw.setYscale(0,max(count))

for i in range(len(count)):
    stddraw.filledRectangle(1.5+i,0,0.75,count[i])


stddraw.show()

