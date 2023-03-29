
#-----------------------------------------------------------------------
# Randombody.py
#-----------------------------------------------------------------------
from vector import Vector
import stddraw
import random
class RandomBody:

    # Construct a new Body object whose position is specified by
    # Vector object r, whose velocity is specified by Vector object
    # v, and whose mass is specified by float mass.

    def __init__(self):
        rx   = random.randint(1e7,1e11)
        ry   = -random.randint(1e8,1e11)
        velo = random.randint(1e2,2e2)
        r = random.random()
        if r < 0.5:
            velo = velo
        else:
            velo = -velo
        r = random.random()
        if r < 0.5:
            vx = velo
            vy = 0
        else:
            vy = velo
            vx = 0
        
        mass = random.randint(1e25,1e26)
        r = Vector([rx, ry])
        v = Vector([vx, vy])
        self._r = r        # Position
        self._v = v        # Velocity
        self._mass = mass  # Mass

    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt.

    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r += self._v.scale(dt)

    # Return the force between Body objects self and other.

    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draw self to standard draw.

    def draw(self,x):
        stddraw.setPenRadius(0.01)
        stddraw.point(self._r[0] + x, self._r[1])