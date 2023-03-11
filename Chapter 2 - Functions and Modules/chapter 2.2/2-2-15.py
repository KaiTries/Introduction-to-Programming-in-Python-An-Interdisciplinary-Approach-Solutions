#craps

import stdrandom
import stdarray
import stdstats
import stdio
import math
import sys

#----functions

def twoDice():                          
    d1 = [1,2,3,4,5,6]
    d2 = [1,2,3,4,5,6]
    r1 = stdrandom.uniformInt(0,6)
    r2 = stdrandom.uniformInt(0,6)
    x = d1[r1] + d2[r2]
    return x

def twoDiceRigged(p):
    prest = (1-p)/5   
    d1 = [1,2,3,4,5,6]
    d2 = [1,2,3,4,5,6]
    pr = [p,prest,prest,prest,prest,prest]
    r1 = stdrandom.discrete(pr)
    r2 = stdrandom.discrete(pr)
    x = d1[r1] + d2[r2]
    return x


def passBet(p):
    x = twoDiceRigged(p)
    if x == 7 or x == 11:
        return True
    elif x == 2 or x == 3 or x == 12:
        return False
    else:
        t = twoDiceRigged(p)
        while t != x and t != 7:
            t =  twoDiceRigged(p)
    if t == x:
        return True
    else:
        return False
    

def chances(n,p):               #take n as how often you want to play the game, p is the probability landing on 1
    a = 0
    for i in range(n):
        if passBet(p):
            a += 1
    return a/n                  #return the average times you have won
