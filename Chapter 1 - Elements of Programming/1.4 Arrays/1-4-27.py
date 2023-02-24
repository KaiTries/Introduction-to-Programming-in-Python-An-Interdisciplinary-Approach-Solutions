#Hadamard matrix. The n-by-n Hadamard matrix Hn matrix is a boolean matrix with the remarkable property that any two rows differ in exactly n/2 elements. 
#(This property makes it useful for designing error-correcting codes.) H1 is a 1-by-1 matrix with the single element True, and for n > 1, 
#H2n is obtained by aligning four copies of Hn in a large square, and then inverting all of the elements in the lower right n-by-n copy, 
#as shown in the following examples (with T representing True and F representing False, as usual).

#H(1)  H(2)    H(4)
#-------------------
# T    T T   T T T T
#      T F   T F T F 
#            T T F F       as seen here H(4) is obtained by aligning four copies of H(2) in a large square,
#            T F F T       and then inverting all of the elements in the lower right 2-by-2 copy

#Compose a program that takes one command-line argument n and writes Hn. Assume that n is a power of 2.


import stdio
import stdarray
import sys
def print_matrix(H):
    for i in range(n):
        for j in range(n):
            if H[i][j]:
                stdio.write('T ')
            else:
                stdio.write('F ')
        stdio.writeln()


n = int(input("enter the order of matrix: "))

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
        
            print(i2, i3, i1)
            print_matrix(H)
            print()
    i1 += i1

# Write the matrix.

