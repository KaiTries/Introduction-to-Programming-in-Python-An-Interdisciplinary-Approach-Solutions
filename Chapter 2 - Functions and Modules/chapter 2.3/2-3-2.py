#recursive function for ln(n!)
import math

def factorialln(n):
    if n == 1: return 0
    return factorialln(n-1) + math.log(n)       #we dont change the conversion step of n-1 only the output of every conversion to math.log(n) given at that conversion level

print(factorialln(6))
print(math.log(math.factorial(6)))