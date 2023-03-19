import stdarray
import stdio
import math
from scipy import special

def coPrime(i,j):
    if j == 0: return i == 1
    return coPrime(j,i%j)

def binomCOEF(n,k):
    return int(math.exp(special.gammaln(n+1) - special.gammaln(k+1) - special.gammaln(n-k+1)))




def MatrixCoPrime(n):
    N = stdarray.create2D(n,n,False)
    for i in range(len(N)):
        for j in range(len(N)):
            if coPrime(i,j):
                N[i][j] = True
    return N

def hadamard(n):
    n = 2**n
    # Create the matrix.
    H = stdarray.create2D(n, n, True)
    # Initialize Hadamard matrix of order n.
    i1 = 1
    while i1 < n:
        for i2 in range(i1):
            for i3 in range(i1):
                H[i2+i1][i3]    = H[i2][i3]
                H[i2][i3+i1]    = H[i2][i3]
                H[i2+i1][i3+i1] = not H[i2][i3]
        i1 += i1
    return H

def coefMatrix(n):
    C = stdarray.create2D(n,n,False)

    for i in range(len(C)):
        for j in range(len(C[i])):
            print(binomCOEF(i,j))
            if binomCOEF(i,j)%2 == 1:
                C[i][j] = True
    return C





def draw(N):
    yes = "*"
    no = " "
    for i in range(len(N)+1):
        if i == 0:
            stdio.writef('%-4s',no)
        else:
            stdio.writef('%-4s',str(i))
        for j in range(len(N)):
            if i == 0:
                stdio.writef('%-4s',str(j+1))
            else:
                if N[i-1][j] == True:
                    stdio.writef('%-4s',yes)
                else:
                    stdio.writef('%-4s',no)
        stdio.writeln()


