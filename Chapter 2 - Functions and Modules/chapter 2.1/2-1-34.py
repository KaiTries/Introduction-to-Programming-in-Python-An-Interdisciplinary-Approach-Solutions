#postal barcodes
import math
import stdarray
import stdio
import stddraw
import sys

def _checkDigit(a=list):
    x = sum(a)
    x = x%10
    x = 10-x
    a += [x]
    return a

def _translate(a=list):
    if a == 0:
        return "11000"
    elif a == 1:
        return "00011"
    elif a == 2:
        return "00101"
    elif a == 3:
        return "00110"
    elif a == 4:
        return "01001"
    elif a == 5:
        return "01010"
    elif a == 6:
        return "01100"
    elif a == 7:
        return "10001"
    elif a == 8:
        return "10010"
    elif a == 9:
        return "10100"
    else:
        return "not a valid digit"

def _buffer(a):
    x = ["1"]
    x += a
    c = ["1"]
    x += c
    return x

def PostalCode(a):
    _checkDigit(a)
    for i in range(len(a)):
        a[i] = _translate(a[i])
    return _buffer(a)

def drawCode(a):
    stddraw.setYscale(0,2)
    stddraw.setXscale(0,((len(a)-2)*5)+2)
    t = 0.25
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "0":
                stddraw.filledRectangle(t,0,0.25,0.5)
            else:
                stddraw.filledRectangle(t,0,0.25,1)
            t += 1
    stddraw.show()

def intake(n):
    a = []
    while len(a) < n:
        x = stdio.readInt()
        a += [x]
    return a



n = int(sys.argv[1])


if n == 5:
    stdio.writeln("input the 5 digit Code")
    x = PostalCode(intake(n))
    stdio.writeln(x)
    drawCode(x)
elif n == 9:
    stdio.writeln("input the 9 digit Code")
    x = PostalCode(intake(n))
    stdio.writeln(x)
    drawCode(x)
else:
    stdio.writeln("not a valid code, try 5 or 9")
    

