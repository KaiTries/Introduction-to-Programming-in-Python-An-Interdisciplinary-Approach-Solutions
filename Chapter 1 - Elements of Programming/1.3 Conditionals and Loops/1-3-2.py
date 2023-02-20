#Compose a more general and robust version of quadratic.py (from Section 1.2) that writes the roots of the polynomial ax2bx + c, 
#writes an appropriate error message if the discriminant is negative, and behaves appropriately (avoiding division by zero) if a is zero.

#code for quadratic.py
import stdio
import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

discriminant = b*b - 4*a 
c = math.sqrt(discriminant)
stdio.writeln((-b + c) / (2*a))
stdio.writeln((-b - c) / (2*a))

#if a is zero then the equation is linear and not quadratic so the code will not work and will give an error message.
#the code will also not work if the discriminant is negative because it will give an error message.

#code for quadratic.py
import stdio
import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = b*b - 4*a*c
if discriminant < 0:
    stdio.writeln("Error: discriminant is negative")
elif a == 0:
    stdio.writeln("Error: a is zero")
else:
    c = math.sqrt(discriminant)
    stdio.writeln((-b + c) / (2*a))
    stdio.writeln((-b - c) / (2*a))