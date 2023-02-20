#Compose a program that takes a float t from the command line and writes the value of sin(2t) + sin(3t).

import sys
import stdio
import math

t = float(sys.argv[1])

stdio.writeln(math.sin(2*t) + math.sin(3*t))