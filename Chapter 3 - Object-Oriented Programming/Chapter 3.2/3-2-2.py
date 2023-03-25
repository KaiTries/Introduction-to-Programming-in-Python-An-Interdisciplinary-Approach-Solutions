#test client
import stddraw
import stdrandom
import stdio    


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
        max_dist_x = abs(self._x - other._x)
        max_dist_y = abs(self._y - other._y)
        if ((self._w / 2) + (other._w / 2)) < max_dist_x:
            return False
        if ((self._h / 2) + (other._h / 2)) < max_dist_y:
            return False
        if self.contains(other):
            if self._x + self._w/2 == other._x + other._w/2 or self._y + self._h/2 == other._y + other._h/2:
                return True
            else:
                return False
        return True

    #True if selc contains other; false otherwise
    def contains(self, other):
        if self._x + self._w/2 < other._x + other._w/2:
            return False
        if self._y + self._h/2 < other._y + other._h/2:
            return False
        return True

    #draw self to stddraw
    def draw(self):
        x = self._x - (self._w / 2)
        y = self._y - (self._h / 2)
        stddraw.rectangle(x,y,self._w,self._h)




def main():
    stddraw.setXscale(-1,1)
    stddraw.setYscale(-1,1)
    n = 3
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