#minimize potential
#function that takes an array of charge objects with positive potential
#find a point so that the potential of that point is within 1% of hte minimum potential anywhere
#constraints: within unit square 
#compose a test client
import random
import stdrandom
import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture

# Read charges from standard input into an array.
#creates an array of n strictly positive charge objects in the unit square
def createCharges(n):
    charges = stdarray.create1D(n)
    for i in range(n):
        x0 = random.random()
        y0 = random.random()
        q0 = random.random()
        charges[i] = Charge(x0, y0, q0)
    return charges

#creates a list of the potentials at a given x,y value and gives the sum -> Potential of that point with respect to all charges

def potentialCharges(x,y,charges):
    potential = stdarray.create1D(n)
    for i in range(n):
        potential[i] = charges[i].potentialAt(x,y)
    potentialsum = sum(potential)
    return potentialsum

#find the minimum:
n = 2
y = 0
x = 0
charges = createCharges(n)
minimumpotential = potentialCharges(x,y,charges)
miny = 0
minx = 0

for i in range(1000):
    y = i/1000
    for j in range(1000):
        x = j/1000
        if potentialCharges(x,y,charges) < minimumpotential:
            print(potentialCharges(x,y,charges))
            minimumpotential = potentialCharges(x,y,charges)
            miny = y
            minx = x

print(x,y)