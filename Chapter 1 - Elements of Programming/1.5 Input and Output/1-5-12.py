import stdio

a = []
while not stdio.isEmpty():
    x = stdio.readLine()
    x = x.split()
    a += [x]

for i in range(len(a)):
    for j in range(1,3):
        a[i][j] = int(a[i][j])

for i in range(len(a)):
    for j in range(1,2):
        x = a[i][j]/a[i][j+1]
    a[i] += [x]

for i in range(len(a)):
    for j in range(len(a[i])):
        if j == 0:
            stdio.writef('%-10s ',a[i][j])
        elif j == 3:
            stdio.writef('%-5.3f ',a[i][j])
        else:
            stdio.writef('%-5s ',a[i][j])
    stdio.writeln()