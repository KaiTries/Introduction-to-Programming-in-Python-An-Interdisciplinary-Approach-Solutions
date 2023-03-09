#benfords law
import stdio
import stdarray
import math
import sys
import stddraw
import random

#-------------------------------
#reads the input and puts it into an array

def reader():
    a = []
    while not stdio.isEmpty():
        x = stdio.readInt()
        a += [x]
    return a

#-------------------------------
#modifies the array so that only the first digit remains

def filter(a):
    for i in range(len(a)):
        a[i] = int(str(a[i])[0])
    return a

#-------------------------------
#count how many times each digit is represented

def count(a):
    list = stdarray.create1D(9,0)
    for i in range(len(list)):
        for j in range(len(a)):
            if a[j] == i + 1:
                list[i] += 1
    return list

#-------------------------------
#plot the representation 

def drawcount(a):
    stddraw.setXscale(0,9)
    stddraw.setYscale(0,max(a)+0.25)
    for i in range(len(a)):
        stddraw.filledRectangle(i + 0.25, 0, 0.5, a[i])
    stddraw.show(5000)
#-------------------------------
#give us the probability for each digit

def probs(a):
    x = sum(a)
    for i in range(len(a)):
        a[i] = a[i] / x
    return a

#-------------------------------
#use the functions
x = probs(count(filter(reader())))
for i in range(0, len(x)):
    stdio.writef("%d: %6.1f%%\n", i+1, 100.0 * float(x[i]))

#-------------------------------
#trick the IRS

#generate set of starting digits according to the distribution 
def IRS(a,o):
    x = a #probability array
    result = []
    for i in range(1,len(x)):
        x[i] += x[i-1]
    print(x)
    z = True
    l = 0
    while z:
        l += 1
        r = random.random()
        total = 0
        for i in range(len(x)):
            if x[i] >= r:
                print(r)
                result +=[i+1]
                break
        if l > o:
            z = False
    for i in range(len(result)):
        result[i] = str(result[i])        
    return result

#add the starting digits to random integers

def Cash(a):
    x = a
    n = len(x)
    b = stdarray.create1D(n,0)
    end = stdarray.create1D(n,0)
    for i in range(n):
        r = random.randint(0,99)
        b[i] = str(r)
    for i in range(n):
        end[i] = int(x[i]+b[i])
    return end


print(IRS(x,100))
print(Cash(IRS(x,100)))