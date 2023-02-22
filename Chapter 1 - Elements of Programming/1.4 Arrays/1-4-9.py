#create a copy of a two dimensional array

import stdarray


# the array is square

#a = stdarray.create2D(5, 5, 0)
#print(a)
#b = a[:]
#print(b)
# the array is rectangular

#c = stdarray.create2D(5, 10, 0)
#print(c)
#d = c[:]
#print(d)
# the array is ragged
e = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
f = e[:]
print(f)

# the array is ragged
z = []
for i in range(len(e)):
    t = []
    for j in range(len(e[i])):
        t += [e[i][j]]
    z += [t]
print(z)