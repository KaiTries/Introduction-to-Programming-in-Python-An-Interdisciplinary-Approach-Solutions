#Color conversion. Several different formats are used to represent color. For example, the primary format for LCD displays, digital cameras, and web pages, known as the RGB format, 
#specifies the level of red (R), green (G), and blue (B) on an integer scale from 0 to 255. The primary format for publishing books and magazines, known as the CMYK format, 
#specifies the level of cyan (C), magenta (M), yellow (Y), and black (K) on a real scale from 0.0 to 1.0. Compose a program that converts RGB to CMYK. 
#Accept three integers —r, g, and b —from the command line and write the equivalent CMYK values. If the RGB values are all 0, then the CMY values are all 0 and the K value is 1; 
#otherwise, use these formulas:
#
#w = max(r/255, g/255, b/255)
#c = (w - r/255) / w
#m = (w - g/255) / w
#y = (w - b/255) / w
#k = 1 - w
#Here's an example run:
#
#$ python rgbtocmyk.py 75 0 130       # indigo
#cyan    = 0.4230769230769229
#magenta = 1.0
#yellow  = 0.0
#black   = 0.4901960784313726

import sys
import math

#input

r = float(sys.argv[1]) #red
g = float(sys.argv[2]) #green
b = float(sys.argv[3]) #blue

#process

w = max (r / 255, g / 255, b / 255)

if w == 0:
    c = 0
    m = 0
    y = 0
    k = 1
else:
    c = (w - (r / 255)) / w
    m = (w - (g / 255)) / w
    y = (w - (b / 255)) / w
    k = 1 - w

#output
print ("The color is", c, m, y, k)