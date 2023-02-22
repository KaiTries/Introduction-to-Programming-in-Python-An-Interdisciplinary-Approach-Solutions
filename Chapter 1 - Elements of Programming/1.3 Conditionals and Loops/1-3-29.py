#relatively prime
# 1-3-29.py
import stdio
import math

n = int(input("n:"))

#check in a n times n grid which numbers are coprime

for i in range (1 ,n+1):
    stdio.write(str(i) + " ")
    for j in range (1 ,n+1):
        if (math.gcd(i,j) == 1):
            stdio.write("*" + " ")
        else:
            stdio.write(" " + " ")

    stdio.writeln()

stdio.writeln()

#write the same grid but without the math.gcd function

for i in range (1 ,n+1):
    stdio.write(str(i) + " ")
    for j in range (1 ,n+1):
        if (i == 1) or (j == 1):
            stdio.write("*" + " ")
        elif (i == j):
            stdio.write(" " + " ")
        elif (i % j == 0) or (j % i == 0):
            stdio.write(" " + " ")
        elif (i % 2 == 0) and (j % 2 == 0):
            stdio.write(" " + " ")
        elif (i % 3 == 0) and (j % 3 == 0):
            stdio.write(" " + " ")
        else:
            stdio.write("*" + " ")

    stdio.writeln()