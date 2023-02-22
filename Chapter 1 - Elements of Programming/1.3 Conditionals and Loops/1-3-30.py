#generate point that is randomly generated on unit circle

import random
import math
import stdio

x = random.uniform(-1,1)
y = random.uniform(-1,1)

while (x*x + y*y) > 1:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

stdio.writeln(str(x) + " " + str(y))

#generate point that is randomly generated on unit circle
