#Gaussian random numbers. One way to generate a random number taken from the Gaussian distribution is to use the Box-Muller formula:
#Z = sin(2 π v) (-2 ln u)1/2
#where u and v are real numbers between 0 and 1 generated by the random.random() function. Compose a program that writes a standard Gaussian random variable.
import random
import math

#input

u = random.random() #uniform random number
v = random.random() #uniform random number

#process

w = math.sin(2*math.pi*v)*math.sqrt(-2*math.log(u))

#output

print ("The gaussian random number is", w)