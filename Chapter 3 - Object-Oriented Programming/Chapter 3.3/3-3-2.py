#date type 3 dimensional particle
from vector import Vector





class Particle:


    def __init__(self,x,y,z,m,vx,vy,vz):
        self._x  =  x
        self._y  =  y
        self._z  =  z
        self._m  =  m
        self._vx = vx     
        self._vy = vy     
        self._vz = vz     
        self._velocity = Vector([vx,vy,vz])

    def velocity(self):
        return 0.5 * self._m * self._velocity.dot(self._velocity)


    def __str__(self) -> str:
        return ''
    
