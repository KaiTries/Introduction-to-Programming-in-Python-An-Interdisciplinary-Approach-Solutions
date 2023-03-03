import stdio
import sys


x = float(sys.argv[1])
y = float(sys.argv[1])
z = float(sys.argv[2])

closest = float('inf')
winner = []
while not stdio.isEmpty():
    x1 = stdio.readFloat()
    if stdio.isEmpty(): print("incomplete coordin")
    else: y1 = stdio.readFloat()
    if stdio.isEmpty(): print("incomplete coordin")
    else: z1 = stdio.readFloat()

    if (((x - x1)*(x - x1)) + ((y-y1)*(y-y1)) + ((z-z1)*(z-z1))) < closest:
        winner = [x1, y1, z1]

stdio.writef('Closest point = (%f, %f, %f)\n', winner[0], winner[1], winner[2])