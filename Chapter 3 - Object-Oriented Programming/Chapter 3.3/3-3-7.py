#vector2d

#-----------------------------------------------------------------------
# vector.py
#-----------------------------------------------------------------------

import math
import stdio
import stdarray

#-----------------------------------------------------------------------

class Vector2D:

    # Construct a new Vector object with numeric Cartesian coordinates
    # given in array a.
    def __init__(self, x, y):
        a = [x,y]
        # Make a defensive copy to ensure immutability.
        self._coords = a[:]   # Cartesian coordinates
        self._n = len(a) # Dimension.

    # Return the ith Cartesian coordinate of self.
    def __getitem__(self, i):
        return self._coords[i]

    # Return the sum of self and Vector object other.
    def __add__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector2D(result[0],result[1])

    # Return the difference of self and Vector object other.
    def __sub__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] - other._coords[i]
        return Vector2D(result[0],result[1])

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector2D(result[0],result[1])

    # Return the inner product of self and Vector object other.
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    def __str__(self):
        return str(self._coords)
        
    # Return the dimension of self.
    def __len__(self):
        return self._n
        
#-----------------------------------------------------------------------

# For testing.
# Create and use some Vector objects.

def main():

    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector2D(2,1)
    y = Vector2D(5,7)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------