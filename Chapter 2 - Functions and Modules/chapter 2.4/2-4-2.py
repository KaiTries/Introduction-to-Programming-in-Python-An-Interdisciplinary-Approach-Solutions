#compose a write() function for percolationIO.py that write 1 for blocked 0 for open and * for filled sites
import sys
import stdarray
import stddraw
import stdrandom
import stdio

#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-.5, n)
    stddraw.setYscale(-.5, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, .5)


def drawB(isOpen,isFull):
    full = "*"
    open = "0"
    blocked = "1"
    n = len(isOpen)
    for i in range(n):
        for j in range(n):
            if isOpen[i][j]:
                if isFull[i][j]:
                    stdio.writef('%-3s',full)
                else:
                    stdio.writef('%-3s',open)
            else:
                stdio.writef('%-3s',blocked)
        stdio.writeln()

#-----------------------------------------------------------------------

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
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
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull

#-----------------------------------------------------------------------

isOpen = random(5,0.5)
isFull = flow(isOpen)

drawB(isOpen,isFull)