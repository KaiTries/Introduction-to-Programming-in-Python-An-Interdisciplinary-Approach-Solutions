#Improve your solution to the "wind chill" exercise from Section 1.2 by adding code to check that the values of the command-line arguments fall within the ranges of validity of the formula, and also adding code to write an error message if that is not the case.

#code for wind chill
import math
import sys

#input

t = float(sys.argv[1]) #temperature
v = float(sys.argv[2]) #wind speed

#process
if t > 50 or v > 120 or v < 3:
    print ("The values of t and v are not valid")
else:
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
    print ("The wind chill in Fahrenheit is", w)



#code for checking validity of input
if t > 50 or v > 120 or v < 3:
    print ("The values of t and v are not valid")
