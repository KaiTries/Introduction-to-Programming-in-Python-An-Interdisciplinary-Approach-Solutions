import stdarray
import random

probabilities = stdarray.create1D(13, 0.0)

for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1.0

for k in range(2, 13):
    probabilities[k] /= 36.0

print(probabilities)

n = int(input("Dice throws: "))
results = stdarray.create1D(13, 0)
for i in range(n):
    result = (random.randrange(1, 7) + random.randrange(1, 7))
    results[result] += 1

for k in range(2, 13):
    results[k] /= n

print(results)
