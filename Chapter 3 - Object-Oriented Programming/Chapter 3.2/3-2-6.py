#data type location
import math
import sys

class Location:


    def __init__(self, lat, log):
        self._lat = lat
        self._log = log

    
    def distanceTo(self,other):
        #great circle
        #input
        a1 = self._lat #latitude1
        b1 = self._log #longitude1
        a2 = other._lat #latitude2
        b2 = other._log #longitude2
        #process
        a1d = math.degrees(a1)
        b1d = math.degrees(b1)
        a2d = math.degrees(a2)
        b2d = math.degrees(b2)
        return (60 * math.acos((math.sin(a1d)) * math.sin(a2d) + math.cos(a1d) * math.cos(a2d) * math.cos(b1d - b2d)))
    



def main():
    lat1 = sys.argv[1]
    log1 = sys.argv[2]
    lat2 = sys.argv[3]
    log2 = sys.argv[4]

    location1 = Location(lat1,log1)
    Location2 = Location(lat2,log2)

    print(location1.distanceTo(Location2))