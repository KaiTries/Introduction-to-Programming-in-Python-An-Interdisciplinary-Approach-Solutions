#location data tyep
import random
import math
import stdio



class Location:
    """
    create location object -> can call random on itself to create random location
    """

    def __init__(self, lat: float=0, long: float=0):
        self._lat = lat
        self._long = long

    
    def random(self):
        """
        this changes the object itself
        """
        self._lat = round(random.uniform(-90,90),5)
        self._long = round(random.uniform(-180,180),5)

    def parse(self):
        """
        prettier str variant
        """
        if self._lat < 0:
            lat = str(abs(self._lat)) + ' S,'
        else:
            lat = str(abs(self._lat)) + ' N,'
        if self._long < 0:
            lot = str(abs(self._long)) + ' W'
        else:
            lot = str(abs(self._long)) + ' E'

        print(lat,lot)
    
    def distanceTo(self,other):
        x1 = math.radians(self._lat)
        y1 = math.radians(self._long)
        x2 = math.radians(other._lat)
        y2 = math.radians(other._long)

        # Compute using the law of cosines.

        # Great circle distance in radians
        angle1 = math.acos(math.sin(x1) * math.sin(x2) \
                 + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

        # Convert back to degrees.
        angle1 = math.degrees(angle1)

        # Each degree on a great circle of Earth is 60 nautical miles.
        distance1 = 60.0 * angle1

        stdio.writeln(str(distance1) + ' nautical miles')

    def __str__(self) -> str:
        return str(self._lat) + ', ' + str(self._long)
    




loc = Location()
loc.random()
loc.parse()
loc1 = Location()
loc1.random()
loc1.parse()

loc.distanceTo(loc1)