#Mercator projection. The Mercator projection is a conformal (angle preserving) projection that maps latitude φ and longitude λ to rectangular coordinates (x, y). It is widely used — for example, in nautical charts and in the maps that you print from the web. The project is defined by the equations:
#
#x = λ - λ0 y = 1/2 * ln((1 + sin(φ)) / (1 - sin(φ)))
#where λ0 is the longitude of the point in the center of the map. Compose a program that accepts λ0 and the latitude and longitude of a point from the command line and writes its projection.

import math
import sys


#input

y0 = float(sys.argv[1]) #longitudecenter
longi = float(sys.argv[2]) #longitude
lat = float(sys.argv[3]) #latitude

#process

x = longi - y0
y = (1/2) * math.log((1 + math.sin(lat)) / (1 - math.sin(lat)))

#output

print ("The mercator projection is", x, y)
