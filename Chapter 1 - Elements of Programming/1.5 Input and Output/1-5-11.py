import stdio

a = []
while not stdio.isEmpty():
    n = stdio.readString()
    a += [n]

print(a)
print(len(a))