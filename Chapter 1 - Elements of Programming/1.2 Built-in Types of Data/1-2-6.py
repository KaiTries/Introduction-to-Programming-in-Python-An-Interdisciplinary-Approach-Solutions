#Explain how to use quadratic.py to find the square root of a number.
#
#Solution: To find the square root of c, find the roots of x2 + 0x - c.

#code for quadratic.py
import stdio
import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

discriminant = b*b - 4*a
c = math.sqrt(discriminant)
stdio.writeln((-b + c) / (2*a))
stdio.writeln((-b - c) / (2*a))
