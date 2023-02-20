#Wind chill. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), 
#the National Weather Service defines the effective temperature (the wind chill) to be:
#w = 35.74 + 0.6215 t + (0.4275 t - 35.75) v0.16
#Compose a program that takes two floats t and v from the command-line and writes the wind chill. 
#Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 (you may assume that the values you get are in that range).


import math
import sys

#calculate wind chill

#input

t = float(sys.argv[1]) #temperature
v = float(sys.argv[2]) #wind speed

#process

w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16

#output

print ("The wind chill in Fahrenheit is", w)