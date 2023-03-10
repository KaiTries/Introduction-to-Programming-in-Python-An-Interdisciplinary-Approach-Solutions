import stdarray
import stdio

n = int(input("Enter a number: "))

isPrime = stdarray.create1D(n+1, True)

for i in range (2, n):
    if (isPrime[i]):
        for j in range (2, n//i+1):
            isPrime[i*j] = False

count = 0
for i in range (2, n+1):
    if (isPrime[i]):
        count += 1

stdio.writeln(count)