import stdio


a = []

while not stdio.isEmpty():
    x = stdio.readInt()
    a += [x]

for i in range(len(a)):
    if i == 0:
        stdio.write(a[i])
        stdio.write(" ")
    elif not a[i] == a[i-1]:
        stdio.write(a[i])
        stdio.write(" ")

