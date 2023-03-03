import math
import stdarray
import stdio
import sys
import stddraw





n = int(sys.argv[1])
lo = float(sys.argv[2])
hi = float(sys.argv[3])



x = stdio.readAllFloats()                               #readall has while not isempty() included
a = []                                                  #Holds all floats between lo and hi
for i in x:
    if i >= lo and i <= hi:
        a += [i]

amnt = hi - lo                                          #size of histogram
steps = amnt/n                                          #size of step


stddraw.setXscale(lo,hi)                                #set x so that histogram has space
stddraw.setYscale(lo,100)                               #set y value high so graph has space

current_lvl = 0                                         #current histogram
nxt_lvl = current_lvl + steps                           #next histo
for i in range(n):                                      #iterating through all steps

    x0 = current_lvl                                    #starting points of the current lvl
    x1 = current_lvl
    y0 = 0                                              #initial end points of current lvl
    y1 = 0
    for j in range(len(a)):                             #test if any numbers in the array fall into that lvl
        if a[j] >= current_lvl and a[j] < nxt_lvl:
            y1 += 1                                     #increase lvl by 1 everytime number falls into it       
    stddraw.line(x0,y0,x1,y1)                           #draw the line 
    current_lvl += steps
    nxt_lvl += steps


stddraw.show()