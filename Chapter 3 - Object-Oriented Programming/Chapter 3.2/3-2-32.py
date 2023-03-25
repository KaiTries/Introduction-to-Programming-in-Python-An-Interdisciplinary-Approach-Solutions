
#-----------------------------------------------------------------------
# mandelbrot.py
#-----------------------------------------------------------------------

import sys
import stddraw
from color import Color
from picture import Picture
from instream import InStream
#-----------------------------------------------------------------------

# Compute the Mandelbrot iteration sequence starting at z0, and 
# return the number of iterations for which the magnitude stays less
# than 2, up to the limit.

def mandel(z0, limit):
    z = z0
    for t in range(limit):
        if abs(z) > 2.0:
            return t
        z = z * z + z0
    return limit

#-----------------------------------------------------------------------

# Accept float command-line arguments xc, yc, and size that specify
# the center and size of a square region of interest. Make a digital
# image showing the result of sampling the Mandelbrot set in that
# egion at a 512*512 grid of equally spaced pixels. Color each pixel
# with a grayscale value that is determined by counting the number of
# iterations before the Mandelbrot sequence for the corresponding
# complex number grows past 2.0, up to 255.

MAX = 255

n = int(sys.argv[1])
xc = float(sys.argv[2])
yc = float(sys.argv[3])
size = float(sys.argv[4])

#make it colorful

colors = InStream('mandel.txt')
color_codes = []
while colors.hasNextLine():
    x = colors.readLine()
    x = x.split(' ')
    color_codes += [x]



pic = Picture(n, n)
for col in range(n):
    for row in range(n):
        x0 = xc - (size / 2) + (size * col / n)
        y0 = yc - (size / 2) + (size * row / n)
        z0 = complex(x0, y0)
        gray = MAX - mandel(z0, MAX)
        gray = color_codes[gray]
        color = Color(int(gray[0]), int(gray[1]), int(gray[2]))
        pic.set(col, n-1-row, color)

stddraw.setCanvasSize(n, n)
stddraw.picture(pic)
stddraw.show()


#-----------------------------------------------------------------------
