import stddraw

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
    def perimiter(self):
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





rectangle = Rectangle(0,0,7,9)
rectangle2 = Rectangle(3,3,1,1)
print(rectangle.intersects(rectangle2))
print(rectangle.contains(rectangle2))
stddraw.setXscale(-5,5)
stddraw.setYscale(-5,5)

rectangle.draw()
rectangle2.draw()
stddraw.show()

