import stdarray
import stdio
import random



def multiply(a,b):         #multiply two n by n matrixes
    if len(a[0]) == len(b):     #checks if matrix multiplication is possible also gives extra credit allowing two different matrixes where number of columns in a equal to rows in b
        c = stdarray.create2D(len(a),len(b[0]),0)   #initialize the matrix
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    else:
        c = stdio.writeln("Cannot multiply these matrices")
        return c


a = [[1,1,2],[2,2,1]]
b = [[1,1,2],[2,2,1],[1,2,3]] 

print(multiply(a,b))