#vector field
import math



class ForceVector:

    """
    Data type for force vectors, input are the force (in Newton) and the angle (measured from positive x axis)
    """

    def __init__(self,Force,angle):
        self._force = Force
        self._angle = angle
        self._xforce = self._force * math.cos(math.radians(angle))
        self._yforce = self._force * math.sin(math.radians(angle))

    def __add__(self,other):
        new_x = self._xforce + other._xforce
        new_y = self._yforce + other._yforce
        new_force = math.sqrt(new_x**2 + new_y**2)
        new_angle = math.degrees(math.atan(new_y/new_x))
        if new_angle < 0 and self._angle < 180 and other._angle < 180:
            new_angle = 180 + new_angle
        elif self._angle + other._angle < 360:
            new_angle = 360 + new_angle
        elif self._angle + other._angle > 360:
            new_angle = 180 + new_angle
        return ForceVector(new_force,new_angle)
    
    def __str__(self):
        return str(self._force) + ', ' + str(self._angle)




b = ForceVector(10,90)
a = ForceVector(10,270)
print(a)
print(b)
print(a + b)