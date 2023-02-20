#Order check. Compose a program that takes three floats x, y, and z as command-line arguments 
#and writes True if the values are strictly ascending or descending (x < y < z or x > y > z), and False otherwise.

import math
import sys
import random

#order check ascending or descending

#input

a = float(sys.argv[1]) #first number
b = float(sys.argv[2]) #second number
c = float(sys.argv[3]) #third number

#process

d = (a < b < c) or (a > b > c) #ascending or descending

#output

print ("The numbers are in order", d)
