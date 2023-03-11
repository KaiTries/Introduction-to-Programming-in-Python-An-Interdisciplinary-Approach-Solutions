#turkey plot
#input stream is one integer + one float per line
#so first we have to sort the data into readable arrays
import stdio
import stdarray
import stdstats
import stddraw
import gaussianinv

#function will read the input as described above and sort it into a matrix with i Integer rows, each with n float columns

def intake():
    X = []
    Y = []
    while not stdio.isEmpty():
        x = stdio.readInt()
        y = stdio.readFloat()
        X += [x]
        Y += [y]
    C = []
    for i in range(1,max(X)+1):
        row = []
        for j in range(len(X)):
            if X[j] == i:
                row += [Y[j]]
        C += [row]
    return C

def Tukey(C):                                               #need to calculate percentiles 10th and 90th, we use gaussian for this (inverse cdf to get percentile)
    stddraw.setYscale(-0.5,1.5)
    stddraw.setXscale(-1,len(C)+1)
    for i in range(len(C)):
        if len(C[i]) <= 1:
            break
        else:
            low = gaussianinv._PhiInverse(0.1,0.00001,min(C[i]),max(C[i]))
            hih = gaussianinv._PhiInverse(0.9,0.00001,min(C[i]),max(C[i]))
            x = stdstats.mean(C[i])
            stdv1 = stdstats.stddev(C[i])
            stddraw.line(i,low,i,hih)
            stddraw.filledRectangle(i-0.25,x-stdv1,0.5,2*stdv1)
    return stddraw.show()


#global code
Tukey(intake())
