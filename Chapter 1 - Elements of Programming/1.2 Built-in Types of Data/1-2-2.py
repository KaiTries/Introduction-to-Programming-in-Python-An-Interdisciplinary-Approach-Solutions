#Compose a program that uses math.sin() and math.cos() to check that the value of sin^2(x) + cos^2(x) is approximately 1 for any x entered as a command line argument. 
#just write the value. Why are the values not always exactly 1.0?

import math
import sys
import stdio

x = float(sys.argv[1])

stdio.writeln(math.sin(x)**2 + math.cos(x)**2)