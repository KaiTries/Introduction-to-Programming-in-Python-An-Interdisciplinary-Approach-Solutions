#we compute the weighted average of a row of a matrix.
#example is of a class with 10 students who took 3 exams.
#the first row is the first student's scores, the second row is the second student's scores, etc.
#the first column is the first exam's scores, the second column is the second exam's scores, etc.
#the last column is the weighted average of the student's scores.
#the last row is the weighted average of the exam's scores.


import random
import stdarray
import stdio


#Determine the size of the matrix
m = 10
n = 3

a = [[99, 85, 98, 0],[98, 57, 78, 0],[92, 77, 76, 0],[94, 32, 11, 0],[99, 34, 22, 0],[90, 46, 54, 0],[76, 59, 88, 0],[92, 66, 89, 0],[97, 71, 24, 0],[89, 29, 38, 0],[0, 0, 0, 0]] #matrix of the scores of the students
w = [0.25,0.25,0.5] #create a list of weights for the exams

print("original matrix is")
for i in range(m):
 for j in range(n):
  print(a[i][j], " ", end='')
 print()

#last column is the weighted average of the student's scores
for i in range(m):
    total = 0
    for j in range(n):
        total += a[i][j]*w[j]
    a[i][n] = total

#last row is the weighted average of the exam's scores
for j in range(n):
    total = 0
    for i in range(m):
        total += a[i][j]
    a[m][j] = total/m


print("modified matrix is")
for i in range(m+1):
 for j in range(n+1):
  print(a[i][j], " ", end='')
 print()
