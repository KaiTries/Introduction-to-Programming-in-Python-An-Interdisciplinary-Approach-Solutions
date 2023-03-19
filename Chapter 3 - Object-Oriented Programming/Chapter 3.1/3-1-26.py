#picture filtering
#write() function takes a picture as argument
#and writes first its dimensions w h
#then the pixel color values as integers
#read() function takes such output and creates a picture

from instream import InStream
from outstream import OutStream
from picture import Picture
import stddraw
import stdio
from color import Color
#use darwin for testing

pic = Picture('darwin.jpg')


def write(pic=Picture):
    width = pic.width()
    height = pic.height()
    stdio.writeln(str(width) + ' ' + str(height))
    for col in range(width):
        for row in range(height):
            pixelcolor = pic.get(col,row)
            r = pixelcolor.getRed()
            g = pixelcolor.getGreen()
            b = pixelcolor.getBlue()            
            stdio.write(str(r) + " " + str(g) + " " + str(b) + " ")
        stdio.writeln()


def read():
    width = stdio.readInt()
    height = stdio.readInt()
    pic = Picture(width,height)
    for col in range(width):
        for row in range(height):
            r = stdio.readInt()
            g = stdio.readInt()
            b = stdio.readInt()
            c = Color(r,g,b)
            pic.set(col,row,c)
    return pic





picture = read()
stddraw.picture(picture)
stddraw.show()