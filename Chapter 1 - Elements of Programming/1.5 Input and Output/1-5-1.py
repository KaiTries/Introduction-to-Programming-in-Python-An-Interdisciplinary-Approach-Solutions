import stdio

a = []
while not stdio.isEmpty():
    n = stdio.readInt()
    a += [n]

print(a)
print(min(a), max(a))