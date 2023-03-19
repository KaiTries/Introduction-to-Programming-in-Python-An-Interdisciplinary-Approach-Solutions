#created flowfast in percolation

import percolation
import percolationio
import percplot
import stddraw


n = 5
p = 0.6
array = percolationio.random(n,n,p)

percolation.flowFast(array)
stddraw.setPenRadius(0.0)
percplot.curveFast(5,0,0,1,1)

#its a bit faster

percplot.curve(5,0,0,1,1)
