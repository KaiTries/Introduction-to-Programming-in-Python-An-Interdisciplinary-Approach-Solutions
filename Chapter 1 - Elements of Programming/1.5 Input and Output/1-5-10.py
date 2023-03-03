import stdio

a = []
while not stdio.isEmpty():
    x = stdio.readInt()
    if x > 0 and x < 99:
        a += [x]


for i in range(len(a)):
    if i%10 == 0 and i != 0:
        stdio.writeln()
    stdio.writef('%-3s',a[i])