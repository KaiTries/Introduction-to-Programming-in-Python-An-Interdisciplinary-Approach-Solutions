#-----------------------------------------------------------------------
# percolation.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import stddraw
import percolationio
#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    m = len(isFull[1])
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flow(isOpen, isFull, i+1, j  )  # Down.
    _flow(isOpen, isFull, i  , j+1)  # Right.
    _flow(isOpen, isFull, i  , j-1)  # Left.
    _flow(isOpen, isFull, i-1, j  )  # Up.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flow(isOpen):
    n = len(isOpen)
    m = len(isOpen[1])
    isFull = stdarray.create2D(n, m, False)
    for j in range(m):
        _flow(isOpen, isFull, 0, j)
    return isFull

#-----------------------------------------------------------------------

# isOpen is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    m = len(isFull[1])
    for j in range(m):
        if isFull[n-1][j]:
            return True
    return False

#-----------------------------------------------------------------------
def _flowD(isOpen, isFull, i, j):
    n = len(isFull)
    m = len(isFull[1])
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flowD(isOpen, isFull, i+1, j  )  # Down.
    _flowD(isOpen, isFull, i  , j+1)  # Right.
    _flowD(isOpen, isFull, i  , j-1)  # Left.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flowD(isOpen):
    n = len(isOpen)
    m = len(isOpen[1])
    isFull = stdarray.create2D(n, m, False)
    for j in range(n):
        _flowD(isOpen, isFull, 0, j)
    return isFull

#-----------------------------------------------------------------------
def _flowAnimated(isOpen, isFull, i, j):
    n = len(isFull)
    m = len(isFull[1])
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    percolationio.draw(isOpen, False)
    stddraw.setPenColor(stddraw.BLUE)
    percolationio.draw(isFull, True)
    stddraw.show(1000.0)
    _flowAnimated(isOpen, isFull, i+1, j  )  # Down.
    _flowAnimated(isOpen, isFull, i  , j+1)  # Right.
    _flowAnimated(isOpen, isFull, i  , j-1)  # Left.
    _flowAnimated(isOpen, isFull, i-1, j  )  # Up.

#-----------------------------------------------------------------------
def flowAnimated(isOpen):
    n = len(isOpen)
    m = len(isOpen[1])
    isFull = stdarray.create2D(n, m, False)
    for j in range(n):
        _flowAnimated(isOpen, isFull, 0, j)
    return isFull
# isOpen is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolatesD(isOpen):
    
    # Compute the full sites of the system.
    isFull = flowD(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    m = len(isFull[1])
    for j in range(m):
        if isFull[n-1][j]:
            return True
    return False

# Read from standard input a boolean matrix that represents the
# open sites of a system. Write to standard output a boolean
# matrix representing the full sites of the system. Then write
# True if the system percolates and False otherwise.
#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

def _flowFast(isOpen, isFull, i, j):
    n = len(isFull)
    m = len(isFull[1])
    if True in isFull[n-1]:
        return
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flowFast(isOpen, isFull, i+1, j  )  # Down.
    _flowFast(isOpen, isFull, i  , j+1)  # Right.
    _flowFast(isOpen, isFull, i  , j-1)  # Left.
    _flowFast(isOpen, isFull, i-1, j  )  # Up.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flowFast(isOpen):
    n = len(isOpen)
    m = len(isOpen[1])
    isFull = stdarray.create2D(n, m, False)
    for j in range(m):
        _flowFast(isOpen, isFull, 0, j)
    return isFull

#-----------------------------------------------------------------------
def percolatesFast(isOpen):
    
    # Compute the full sites of the system.
    isFull = flowFast(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    m = len(isFull[1])
    for j in range(m):
        if isFull[n-1][j]:
            return True
    return False

#-----------------------------------------------------------------------
def _flowTriangle(isOpen, isFull, i, j):
    n = len(isFull)
    m = len(isFull[1])
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= m):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flowTriangle(isOpen, isFull, i+1, j  )  # Down.
    _flowTriangle(isOpen, isFull, i  , j+1)  # Right.
    _flowTriangle(isOpen, isFull, i  , j-1)  # Left.
    _flowTriangle(isOpen, isFull, i-1, j  )  # Up.
    _flowTriangle(isOpen, isFull, i+1, j+1)  # Diagonal down Right

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flowTriangle(isOpen):
    n = len(isOpen)
    m = len(isOpen[1])
    isFull = stdarray.create2D(n, m, False)
    for j in range(m):
        _flowTriangle(isOpen, isFull, 0, j)
    return isFull
#-----------------------------------------------------------------------
def percolatesTriangle(isOpen):
    
    # Compute the full sites of the system.
    isFull = flowTriangle(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    m = len(isFull[1])
    for j in range(m):
        if isFull[n-1][j]:
            return True
    return False
#-----------------------------------------------------------------------