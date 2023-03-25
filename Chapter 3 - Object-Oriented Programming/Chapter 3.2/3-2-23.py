#quaternions
import math




class Quaternion:



    def __init__(self,a0,a1,a2,a3):
        self._a0 = a0
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3

    def __abs__(self):
        return math.sqrt(self._a0**2 + self._a1**2 + self._a2**2 + self._a3**2)
    
    def conjugate(self):
        return Quaternion(self._a0, -self._a1, -self._a2, -self._a3)
    
    def inverse(self):
        return Quaternion(self._a0 / abs(self)**2, -self._a1 / abs(self)**2, -self._a2 / abs(self)**2, -self._a3 / abs(self)**2)
    
    def __add__(self,other):
        return Quaternion(self._a0 + other._a0, self._a1 + other._a1, self._a2 + other._a2, self._a3 + other._a3)
    
    def __mul__(self,other):
        return Quaternion(self._a0 * other._a0 - self._a1 * other._a1 - self._a2 * other._a2 - self._a3 * other._a3, \
                          self._a0 * other._a1 - self._a1 * other._a0 + self._a2 * other._a3 - self._a3 * other._a2, \
                          self._a0 * other._a2 - self._a1 * other._a3 + self._a2 * other._a0 + self._a3 * other._a1, \
                          self._a0 * other._a3 + self._a1 * other._a2 - self._a2 * other._a1 + self._a3 * other._a0)
    
    def __truediv__(self,other):
        return self * other.inverse()
    
    def __str__(self):
        return str(self._a0) + ',' + str(self._a1)+ ',' +str(self._a2) + ',' + str(self._a3)



def main():
    quat1 = Quaternion(2,3,1,5)
    quat2 = Quaternion(2,2,2,2)

    print(quat1 + quat2)
    print(quat1 * quat2)
    print(quat1 / quat2)



if __name__ == '__main__': main()