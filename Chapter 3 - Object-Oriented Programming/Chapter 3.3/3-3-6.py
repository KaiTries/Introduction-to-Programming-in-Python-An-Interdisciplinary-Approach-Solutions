
import math
import stdio
import stdarray

#-----------------------------------------------------------------------

class Vector:

    # Construct a new Vector object with numeric Cartesian coordinates
    # given in array a.
    def __init__(self, a):
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
        return Vector(result)

    # Return the difference of self and Vector object other.
    def __sub__(self, other):
        return self + (other * -1.0)

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

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
        