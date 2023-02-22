import math
import stdarray
import random


#Determine the size of the matrix
n = int(input("Enter size of matrix: "))

#Create the first matrix with random values
A = []
for i in range(n):
    row = []
    for j in range(n):
        row += [bool(random.randint(0,1))]
    A += [row]

#Create the second matrix with random values
B = []
for i in range(n):
    row = []
    for j in range(n):
        row += [bool(random.randint(0,1))]
    B += [row]


#show the first matrix        
print("first matrix is")

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], " ", end='')
    print()

#show the second matrix
print("second matrix is")
for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j], " ", end='')
    print()

#Create the third matrix by multiplying the first and second matrix
# and show the third matrix


C = []
for i in range(n):
    row = []
    for j in range(n):
        row += [bool(0)]
    C += [row]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print("third matrix is")
for i in range(len(C)):
    for j in range(len(C[i])):
        print(bool(C[i][j]), " ", end='')
    print()
