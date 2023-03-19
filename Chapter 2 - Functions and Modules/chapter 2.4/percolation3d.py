import stdio
import stdarray
import stddraw
import percolationio
import percolation3dio
#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

def _flow3D(isOpen, isFull, z,i, j):
    n = len(isFull)
    m = len(isFull[1])
    if (z < 0) or (z >= n):
        return
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[z][i][j]:
        return
    if isFull[z][i][j]:
        return
    isFull[z][i][j] = True
    _flow3D(isOpen, isFull, z,i+1, j  )  # Down.
    _flow3D(isOpen, isFull, z,i  , j+1)  # Right.
    _flow3D(isOpen, isFull, z,i  , j-1)  # Left.
    _flow3D(isOpen, isFull, z,i-1, j  )  # Up.
    _flow3D(isOpen, isFull, z-1,i, j  )  # backwards.
    _flow3D(isOpen, isFull, z+1,i, j  )  # forward.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flow3D(isOpen):
    z = len(isOpen)
    n = len(isOpen[1])
    m = len(isOpen[1][1])
    isFull = percolation3dio.random(z,0)
    for z in range(z):
        for j in range(m):
            _flow3D(isOpen, isFull, z,0, j)
    return isFull

#-----------------------------------------------------------------------

# isOpen is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates3D(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow3D(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    z = len(isFull)
    n = len(isFull[1])
    m = len(isFull[1][1])
    for i in range(z):
        for j in range(m):
            if isFull[i][n-1][j]:
                return True
    return False