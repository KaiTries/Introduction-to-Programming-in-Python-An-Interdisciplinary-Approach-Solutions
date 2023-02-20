#Redesign tenhellos.py to compose a program that accepts the number of lines to write as a command-line argument. 
#You may assume that the argument is less than 1000. Hint: consider using i % 10 and i % 100 to determine whether to use st, nd, rd, or th for writing the ith Hello.
#
#original code:
#Compose a program that writes the Hello, World message 10 times.
#import stdio
#
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')
#stdio.writeln('Hello, World')

#improved code:

import stdio
import time
import sys

n = int(sys.argv[1]) #number of lines to write / number of times to write Hello, World
 
i = 1
while i <= n :
    if i == 11:
        stdio.writeln("11th Hello")
    elif i == 12:
        stdio.writeln("12th Hello")
    elif i == 13:
        stdio.writeln("13th Hello")
    else:
        if i % 10 == 1:
            stdio.writeln(str(i) + "st Hello")
        elif i % 10 == 2:
            stdio.writeln(str(i) + "nd Hello")
        elif i % 10 == 3:
            stdio.writeln(str(i) + "rd Hello")
        else:
            stdio.writeln(str(i) + "th Hello")
    i = i + 1
