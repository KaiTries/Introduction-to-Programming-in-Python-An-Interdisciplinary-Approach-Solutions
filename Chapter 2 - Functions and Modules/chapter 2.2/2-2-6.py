#Boltzmann function
#add this to your stdrandom i guess
import gaussian
import random
import math

def maxwellBoltzmann(o):
    sum = 0
    for i in range(3):
        r = random.random()
        x = gaussian.pdf(r,0,o)
        x = x*x
        sum += x
    return math.sqrt(sum)

print(maxwellBoltzmann(1))