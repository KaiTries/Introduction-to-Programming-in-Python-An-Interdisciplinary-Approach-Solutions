#modify so that we can see the flow -> each box being filled
import percolationio
import percolation
import stddraw

n = 10
p = 0.5

array = percolationio.random(n,p)
percolation.flowAnimated(array)
stddraw.show()