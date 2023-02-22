#solution
import math
n = int(input("Enter a number: "))
total = 0.0

for i in range (1, n+1):
    total += 1.0 / (i*i)

print(total)
print(math.sqrt(6*total))