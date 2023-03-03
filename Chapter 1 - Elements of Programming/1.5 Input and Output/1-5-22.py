import stddraw
import sys


string = str(sys.argv[1])
n = float(sys.argv[2])
stddraw.setXscale(0, 1.0)
stddraw.setYscale(0, 1.0)

# Set the font.
stddraw.setFontFamily('Arial') 
stddraw.setFontSize(60)
stddraw.setPenColor(stddraw.BLACK)

i = 0.0
while True:
    stddraw.clear()
    stddraw.text((i % 1.0),       0.5, string)
    stddraw.text((i % 1.0) - 1.0, 0.5, string)
    stddraw.text((i % 1.0) + 1.0, 0.5, string)
    stddraw.show(n)
    i += 0.01
    

