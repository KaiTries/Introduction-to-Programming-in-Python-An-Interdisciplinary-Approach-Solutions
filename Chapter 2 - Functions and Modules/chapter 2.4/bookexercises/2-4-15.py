#adaptive plotting again:

import percplot
import stddraw

n = 10          #reach max recursion fast around 40
trials = 10000  #takes a while but smooth curve
gap = 0.5       #can see more displacement on the x axis
err = 0.2       #longer stretches of points

stddraw.setPenRadius(0.0)

percplot.curve(n,0,0,1,1,trials,gap,err)
stddraw.show()