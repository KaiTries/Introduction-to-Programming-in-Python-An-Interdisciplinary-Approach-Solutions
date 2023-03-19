#percolation in 3d :O
#we create 2 modules IO and percolation + this as the client
import percolation3d
import percolation3dio
import estimate
import percplot
import stddraw


isOpen = percolation3dio.random(2,0.5)

print(percolation3d.percolates3D(isOpen))
print(estimate.evaluate3D(2,0.5,100))


stddraw.setPenRadius(0.0)
percplot.curve3D(5,0,0,1,1)