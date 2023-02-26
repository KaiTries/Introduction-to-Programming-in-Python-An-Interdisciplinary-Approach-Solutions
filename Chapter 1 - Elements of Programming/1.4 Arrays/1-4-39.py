#Binomial coefficients. Compose a program that builds and writes a two-dimensional ragged array a such that 
#a[n][k] contains the probability that you get exactly k heads when you toss a fair coin n times. Take a command-line argument to specify the maximum value of n. 
#These numbers are known as the binomial distribution: if you multiply each element in row k by 2n, 
#you get the binomial coefficients (the coefficients of xk in (x+1)n) arranged in Pascal's triangle. 
#To compute them, start with a[n][0] = 0.0 for all n and a[1][1] = 1.0, then compute values in successive rows, left to right, with a[n][k] = (a[n-1][k] + a[n-1][k-1])/2.0.
import stdarray
import math
import stdio

n = int(input("max val of n: "))
a = stdarray.create2D(n,n, 0)

a[1][1] = 1
for i in range(1,n):
    for j in range(1,i):
        a[i][j] = ((math.factorial(i)/math.factorial(i-j))/math.factorial(j))/(2**i)


for i in range(n):
    for j in range(n):
        stdio.write(a[i][j])
        stdio.write(" ")
    stdio.writeln()

#i dont know what they wanted to achieve with the extra information for the question. 