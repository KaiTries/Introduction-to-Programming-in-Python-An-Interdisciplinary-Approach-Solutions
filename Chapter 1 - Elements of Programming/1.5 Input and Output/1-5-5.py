import stdarray
import stdio

a = []

while not stdio.isEmpty():
    x = stdio.readInt()
    a += [x]


count = 0
max = 0
bigv = 0
for i in range(len(a)):
    count = 0
    for j in range(i,len(a)):
        if a[i] == a[j]:
            count += 1
        elif a[i] != a[j]:
            break
    if count > max:
        max = count
        bigv = a[i]


stdio.writeln("longest run: " + str(max) + " consecutive " + str(bigv) + "s")