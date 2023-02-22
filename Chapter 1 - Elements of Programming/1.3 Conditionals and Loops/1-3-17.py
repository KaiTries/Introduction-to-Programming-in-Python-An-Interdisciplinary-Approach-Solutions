import sys
import stdio

EPSILON = 1e-15
stdio.writeln(EPSILON)

c = int(input('Enter a number: '))
t = c
while abs(t - c/t) > (EPSILON * t):
    print('t = ', t)
    t = (c/t + t) / 2.0
stdio.writeln(t)

