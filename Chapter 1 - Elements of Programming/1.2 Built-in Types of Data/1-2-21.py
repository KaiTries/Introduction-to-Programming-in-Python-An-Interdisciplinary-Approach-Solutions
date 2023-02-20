#Continuously compounded interest. Compose a program that calculates and writes the amount of money you would have if you invested it at a given interest rate compounded continuously, taking the number of years t, the principal P, and the annual interest rate r as commmand-line arguments. 
#The desired value is given by the formula pert.

import sys
import stdio
import math

t = int(sys.argv[1]) #number of years
P = int(sys.argv[2]) #principal
r = float(sys.argv[3]) #annual interest rate

sol = P * math.e**(r * t)

stdio.writeln("The amount is: ", sol)
