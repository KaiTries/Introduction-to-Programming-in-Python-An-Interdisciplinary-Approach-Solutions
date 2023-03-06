import math
import stdio
import stdarray
import sys


def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a


def euler(n):
    count = 0
    number = []
    for i in range(2,n):
        if gcd(n,i) == 1:
            count += 1
            number += [i]
    return count,number


n = int(sys.argv[1])
result = euler(n)
stdio.writef('%s',result)