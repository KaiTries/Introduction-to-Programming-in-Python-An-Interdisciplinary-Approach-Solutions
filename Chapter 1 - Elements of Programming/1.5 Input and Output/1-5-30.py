import stdio
import math
import stddraw





R = 0.45        
x = 0.5
y = 0.5
t = 0
while True:
    seconds = t % 60
    minutes = (t / 60.0) % 60
    hours   = (t / 3600.0) % 12
    stddraw.circle(x,y,R)  
    #seconds
    angle1 = math.radians(6 * seconds)
    x1 = x + R *math.sin(angle1)
    y1 = y + R *math.cos(angle1)
    stddraw.line(x,y,x1,y1)
    #minutes
    angle2 = math.radians(6 * minutes)
    x1 = x + R *math.sin(angle2)
    y1 = y + R *math.cos(angle2)
    stddraw.line(x,y,x1,y1)
    #hours
    angle3 = math.radians(6 * hours)
    x1 = x + R *math.sin(angle3)
    y1 = y + R *math.cos(angle3)
    stddraw.line(x,y,x1,y1)

    stddraw.show(1000)
    stddraw.clear()
    t += 1