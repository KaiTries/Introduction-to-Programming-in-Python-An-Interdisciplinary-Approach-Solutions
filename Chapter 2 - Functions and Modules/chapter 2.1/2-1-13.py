import math
import sys



def subtend(d1,a1,d2,a2):
    a = a2 - a1
    d = d2 - d1
    return 2*math.asin((math.sin(d/2)**2 + math.cos(d1)*math.cos(d2)*math.sin(a/2)**2)**(1/2))



print(subtend(45,120,22,60))