#implement more into complex api
#add theta, conjugate, subtraction, division and power
#-----------------------------------------------------------------------
# complex.py
#-----------------------------------------------------------------------

import stdio
import math

# A Complex object is a complex number.

# A Complex object is immutable.  So once you create and initialize
# a Complex object, you cannot change it.

class Complex:

    # Construct self with real part real and imaginary
    # part imag. real defaults to 0.0. imag also defaults to 0.0.
    def __init__(self, re=0.0, im=0.0):
        self._re = re
        self._im = im

    # Return the real part of self.
    def re(self):
        return self._re

    # Return the imaginary part of self.
    def im(self):
        return self._im

    # Return the conjugate of self.
    def conjugate(self):
        return Complex(self._re, -self._im)

    # Return a new Complex object which is the sum of self and 
    # Complex object other.
    def __add__(self, other):
        re = self._re + other._re
        im = self._im + other._im
        return Complex(re, im)
    
    def __sub__(self, other):
        re = self._re - other._re
        im = self._im - other._im
        return Complex(re, im)

    # Return a new Complex object which is the product of self and
    # Complex object other.
    def __mul__(self, other):
        re = self._re * other._re - self._im * other._im
        im = self._re * other._im + self._im * other._re
        return Complex(re, im)

    def __truediv__(self, other):
        polar_self = self.theta()
        polar_other = other.theta()
        re_self = polar_self.re()
        im_self = polar_self.im()
        re_other = polar_other.re()
        im_other = polar_other.im()
        real = re_self / re_other
        im = im_self - im_other
        return Complex(real, im).thetaReverse()     

    def __pow__(self,other):
        #Hence, (a+ib)**c+id=e**ln(r)(c+id)+iθ(c+id)
        return
    # Return True if self and Complex object other are equal, and
    # False otherwise.
    def __eq__(self, other):
        return (self._re == other._re) and (self._im == other._im)

    # Return True if self and Complex object other are unequal, and
    # False otherwise.
    def __ne__(self, other):
        return not self.__eq__(other)

    # Return the absolute value of self.
    def __abs__(self):
        return math.sqrt(self._re*self._re + self._im*self._im)
        # Alternative: return math.hypot(self._re, self._im)
        # Alternative: return self.__mul__(self.conjugate())

    def theta(self):
        r = abs(self)
        O = math.degrees(math.atan(self._im / self._re))
        return Complex(r,O)
    
    def thetaReverse(self):
        real = self._re * math.cos(math.radians(self._im))
        imaginary = self._re * math.sin(math.radians(self._im))
        return Complex(real,imaginary)

    # Return a string representation of self.
    def __str__(self):
        if self._re == 0:
            return str(self._im) + 'i'
        if self._re == int(self._re) and self._im == int(self._im):
            return str(int(self._re)) + ' + ' + str(int(self._im)) + 'i'
        if self._re == int(self._re) and not self._im == int(self._im):
            return str(int(self._re)) + ' + ' + str(self._im) + 'i'
        if not self._re == int(self._re) and self._im == int(self._im):
            return str(self._re) + ' + ' + str(int(self._im)) + 'i'
        if self._im == 0:
            return str(self._re) 
        return str(self._re) + ' + ' + str(self._im) + 'i'

#-----------------------------------------------------------------------

# For testing.
# Create and use some Complex objects.

def main():

    z0 = Complex(4,3)
    stdio.writeln(z0)
    z1 = z0.theta()
    print(z1)
    z2 = z1.thetaReverse()
    print(z2)


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------
