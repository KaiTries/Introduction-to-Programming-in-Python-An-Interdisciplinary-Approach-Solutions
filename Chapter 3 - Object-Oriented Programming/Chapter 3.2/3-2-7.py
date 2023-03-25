#fractions
import math

def gcd(p,q):
    if q == 0: return p
    return gcd(q, p % q)

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


class Fraction:



    def __init__(self,x,y):
        self._x = x / gcd(x,y)
        self._y = y / gcd(x,y)

    def __add__(self,other):
        bot = self._y * other._y
        top = (self._x * other._y) + (other._x * self._y)
        return Fraction(top,bot)
    
    def __sub__(self,other):
        bot = self._y * other._y
        top = (self._x * other._y) - (other._x * self._y)
        return Fraction(top,bot)

    def __mul__(self,other):
        top = self._x * other._x
        bot = self._y * other._y
        return Fraction(top,bot)

    def __abs__(self,other):
        top = abs(self._x)
        bot = abs(self._y)
        return Fraction(top,bot)

    def __str__(self):
        return str(self._x) + '/' + str(self._y)




one = Fraction(1,3)
two = Fraction(2,6)

print(two + two + one + two)
print(one * two)