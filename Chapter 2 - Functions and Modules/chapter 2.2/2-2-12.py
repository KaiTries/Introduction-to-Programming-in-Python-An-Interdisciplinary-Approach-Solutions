#adding function exp() to stdrandom

import stdrandom
import random
import math

def exp(y):
    x = random.random()
    return -math.log(x / y)
