#data point
import math


class Point:


    def __init__(self,x,y):
        self._x = x
        self._y = y


    def distanceTo(self,other):
        return math.sqrt((other._x - self._x)*(other._x - self._x) + (other._y - self._y) * (other._y - self._y))
    
    def __str__(self) -> str:
        return '(' + str(self._x) + ', ' + str(self._y) + ')'
    




one = Point(1,1)
print(one)