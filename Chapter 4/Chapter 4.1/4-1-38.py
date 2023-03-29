#pattern matching
#find the biggest square of 1s
import stdarray

a = [[1, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 1, 0],
     [0, 0, 1, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 1, 1, 1, 1, 0]]

n = len(a)
solution = stdarray.create2D(n,n,0)


for i in range(n):
    for j in range(n):
        if i == 0:
            solution[i][j] = a[i][j]
        elif a[i][j] == 1:
            solution[i][j] = min(solution[i-1][j],solution[i][j-1],solution[i-1][j-1])+1
        else:
            solution[i][j] = 0

maxi = 0
for i in range(n):
    if max(solution[i]) > maxi:
        maxi = max(solution[i])

print(maxi)