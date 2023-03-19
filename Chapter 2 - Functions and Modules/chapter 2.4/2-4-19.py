#bond percolation
#same approach but instead of using squares we will use dots for each matrix value
#if two neighbourings values are true we connect them with a line
import percolationio
import stddraw
import percolation
import estimate
illustrate = __import__('2-4-1')
#we can use the same generator to make our arrays
n = 5
p = 0.5
array = percolationio.random(n,n,p)

illustrate.draw(array)

def draw(a):
    n = len(a)
    m = len(a[1])
    stddraw.setXscale(-1.5, n+1)
    stddraw.setYscale(-1.5, n+1)
    for i in range(n):
        for j in range(m):
            if i < (n-1):
                if a[i][j]:
                    stddraw.filledCircle(j, n-i-1, .05)        
                if a[i+1][j] and a[i][j]:
                    stddraw.line(j,n-i-1,j,n-i-2)
                if j < (m-1):
                    if a[i][j+1] and a[i][j]:
                        stddraw.line(j,n-i-1,j+1,n-i-1)                
            else:
                if a[i][j]:
                    stddraw.filledCircle(j, n-i-1, .05)
                if j < (m-1):
                    if a[i][j+1] and a[i][j]:
                        stddraw.line(j,n-i-1,j+1,n-i-1)                   


draw(array)
stddraw.show()

#if we run this programm we will get a visual representation of the grid, in the command line you see the True nodes with "*" in the draw window you see the edges
#as far as i understand it we can just use our normal percolates function to get the true false:
#its basically the same problem but illustrated differently?


