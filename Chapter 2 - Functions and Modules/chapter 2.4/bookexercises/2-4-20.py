#now with a trangular grid
#it is exactly the same as before but we will add additional possible connectivity
#now we also add the diagonal lines
#we can keep our square matrix for now just imagine it being of rhombus shape



import percolationio
import stddraw
import percolation
import estimate
illustrate = __import__('2-4-1')
#we can use the same generator to make our arrays
n = 5
p = 0.5

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
                    if a[i+1][j+1] and a[i][j]:
                        stddraw.line(j,n-i-1,j+1,n-i-2)                
            else:
                if a[i][j]:
                    stddraw.filledCircle(j, n-i-1, .05)
                if j < (m-1):
                    if a[i][j+1] and a[i][j]:
                        stddraw.line(j,n-i-1,j+1,n-i-1)                   


#create random boolean array
array = percolationio.random(n,n,p)
#prints True False statement if it percolates
print(percolation.percolatesTriangle(array))
#returns the nodes in command window
illustrate.draw(array)
#draw the illustration
draw(array)

stddraw.show()