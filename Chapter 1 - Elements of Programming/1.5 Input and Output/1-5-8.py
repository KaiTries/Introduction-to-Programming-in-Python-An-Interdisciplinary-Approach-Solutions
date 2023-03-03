import stdio
import math

a = []
b = []
t = 0
while not stdio.isEmpty():
    n = stdio.readInt()
    if n < 0:
        stdio.writeln("number has to be bigger than 0 :)")
    else:
        t += 1
        a += [n]
        b += [n]


for i in range(len(a)):
    a[i] = math.log(a[i]) / t

print(math.exp(math.fsum(a)))

total = 0
for i in range(len(b)):
    b[i] = 1 / b[i]
    total += b[i]

harmean = t / total
print(harmean)
