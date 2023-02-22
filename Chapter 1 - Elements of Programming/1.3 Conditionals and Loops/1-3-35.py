import math
import random

n = int(input("boundary to walk to: "))

steps = 0
starthorizontal = 0
startvertical = 0
end = n

while abs(starthorizontal) < end or abs(startvertical) < end:
    x = random.randint(0,3)
    if x == 0:
        starthorizontal += 1
        steps += 1
    elif x == 1:
        starthorizontal -= 1
        steps += 1
    elif x == 2:
        startvertical += 1
        steps += 1
    elif x == 3:
        startvertical -= 1
        steps += 1
    if abs(starthorizontal) == end or abs(startvertical) == end:
        if abs(starthorizontal) == end:
            print("horizontal: ", starthorizontal)
            print("steps: ", steps)
        else:
            print("vertical: ", startvertical)
            print("steps: ", steps)
        break

