#rectangle with interval

#test client
import stddraw
import stdrandom
import stdio    
from interval import Interval

class Rectangle:

    #creates rectangle with center x,y and widht w and height h
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    #area of self
    def area(self):
        return self._w * self._h
    
    #perimiter of self
    def perimeter(self):
        return 2*self._w + 2*self._h
    
    #True if self intersects other; false otherwise
    def intersects(self, other):
        sel_finterval_x = Interval(self._x - self._w/2,self._x + self._w/2)
        sel_finterval_y = Interval(self._y - self._h/2,self._y + self._h)
        other_interval_x = Interval(other._x - other._w/2,other._x + other._w/2)
        other_interval_y = Interval(other._y - other._h/2,other._y + other._h)
        if sel_finterval_x.intersects(other_interval_y) or sel_finterval_y.intersects(other_interval_y):
            return True
        return False

    #True if selc contains other; false otherwise
    def contains(self, other):
        sel_finterval_x = Interval(self._x - self._w/2,self._x + self._w/2)
        sel_finterval_y = Interval(self._y - self._h/2,self._y + self._h)
        other_interval_x = Interval(other._x - other._w/2,other._x + other._w/2)
        other_interval_y = Interval(other._y - other._h/2,other._y + other._h/2)
        if sel_finterval_x.contains(other_interval_x) and sel_finterval_y.contains(other_interval_y):
            return True
        return False

    #draw self to stddraw
    def draw(self):
        x = self._x - (self._w / 2)
        y = self._y - (self._h / 2)
        stddraw.rectangle(x,y,self._w,self._h)




def main():
    stddraw.setXscale(-1,1)
    stddraw.setYscale(-1,1)
    n = 2
    lo = 1
    hi = 10


    rectangles_Original = []
    rectangles_unit = []
    for i in range(n):
        w = stdrandom.uniformFloat(lo,hi)
        h = stdrandom.uniformFloat(lo,hi)
        rectangle = Rectangle(0,0,w,h)
        rectangles_Original += [rectangle]
        rectangle_unit = Rectangle(0,0,w/hi,h/hi)
        rectangles_unit += [rectangle_unit]

    area = 0
    perimeter = 0
    for i in range(len(rectangles_unit)):
        rectangles_unit[i].draw()
        area += rectangles_Original[i].area()
        perimeter += rectangles_Original[i].perimeter()

    intersects = 0
    contains = 0
    for i in range(len(rectangles_unit)):
        for j in range(i+1,len(rectangles_unit)):
            if rectangles_unit[i].intersects(rectangles_unit[j]):
                intersects += 1
            if rectangles_unit[i].contains(rectangles_unit[j]):
                contains += 1

    print(area/n, perimeter/n)
    print(intersects, contains)
    stddraw.show()


if __name__ == '__main__': main()