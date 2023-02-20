#Compose a program that takes three floats x0, v0, and t from the command line, evaluates x0 + v0t - Gt2 / 2, and writes the result. (Note: G is the constant 9.80665. 
#This value is the displacement in meters after t seconds when an object is thrown straight up from initial position x0 at velocity v0 meters per second.)

import sys
import stdio
import math

G = 9.80665

#input
x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])

#calculation
x = x0 + v0*t - G*t**2 / 2

#output
stdio.writeln(str(x) + ' meters. This value is the displacement in meters after' + str(t) + ' seconds when an object is thrown straight up from initial position ' + str(x0) + ' at velocity ' + str(v0) + ' meters per second')