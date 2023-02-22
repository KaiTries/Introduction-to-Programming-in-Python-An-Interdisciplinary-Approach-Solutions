import stdio

f = 0
g = 1 
for i in range(16):
    stdio.writeln(f)
    f = f + g
    g = f - g
    