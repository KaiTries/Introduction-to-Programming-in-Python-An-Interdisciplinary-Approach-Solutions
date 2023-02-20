#Great circle. Compose a program that takes four float command-line arguments x1, y1, x2, and y2 (the latitude and longitude, in degrees, of two points on the earth) and writes the great-circle distance between them. The great-circle distance d (in nautical miles) is given by the formula derived from the law of cosines:
#
#d = 60 * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
#Note that this equation uses degrees, whereas Python's trigonometric functions use radians. Use math.radians() and math.degrees() to convert between the two. Use your program to compute the great-circle distance between Paris (48.87° N, -2.33° W) and San Francisco (37.8° N, 122.4° W).


#great circle

import math
import sys

#input

a1 = float(sys.argv[1]) #latitude1
b1 = float(sys.argv[2]) #longitude1
a2 = float(sys.argv[3]) #latitude2
b2 = float(sys.argv[4]) #longitude2

#process

a1d = math.degrees(a1)
b1d = math.degrees(b1)
a2d = math.degrees(a2)
b2d = math.degrees(b2)

d = (60 * math.acos((math.sin(a1d)) * math.sin(a2d) + math.cos(a1d) * math.cos(a2d) * math.cos(b1d - b2d)))

#output

print ("The distance is", d)

