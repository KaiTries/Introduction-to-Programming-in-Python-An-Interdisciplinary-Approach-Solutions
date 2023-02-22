import sys
import stdio

EPSILON = 1e-15
stdio.writeln(EPSILON)

c = int(input('Enter a number: '))
x= c
n = int(input('Enter the root: '))


i = x - (x**n - c) / (n * x**(n-1))
while abs(i - x) > EPSILON:
    x = i
    i = x - (x**n - c) / (n * x**(n-1))
stdio.writeln(i)
