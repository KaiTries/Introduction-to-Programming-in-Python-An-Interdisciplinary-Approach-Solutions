#implement shuffle() in stdrandom

import stdrandom
import random

def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randrange(i, n)
        temp = a[r]
        a[r] = a[i]
        a[i] = temp   
    return a
