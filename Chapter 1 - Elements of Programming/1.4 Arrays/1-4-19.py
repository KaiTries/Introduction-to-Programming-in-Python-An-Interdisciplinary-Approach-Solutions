import stdarray

n = int(input("Size of the three dimensional square: "))

a = stdarray.create2D(n, n, False)
print(a)

b = []
for i in range(n):
    zval = []
    for j in range(n):
        zval += [a]
    b += [zval]

print(b)