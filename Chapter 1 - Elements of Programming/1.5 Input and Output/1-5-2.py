import stdio

a = []
while not stdio.isEmpty():
    n = stdio.readInt()
    if n < 0:
        stdio.writeln("number has to be bigger than 0 :)")
    else:
        a += [n]

print(a)
print(min(a), max(a))