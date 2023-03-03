import stdio
import sys
import stdarray
import random





#n is the input from a file whos output is 1 per line
n = []
while not stdio.isEmpty():
    x = stdio.readInt()
    n += [x]
#m is random sample size
m = random.randint(1,len(n))

# Initialize perm.
perm = stdarray.create1D(len(n), 0)
for i in range(len(n)):
    perm[i] = i

# Create random sample in perm[0], perm[1], ..., perm[m-1]
for i in range(m):

    # Choose a random integer r between i and n-1.
    r = random.randrange(i, len(n))

    # Swap perm[i] and perm[r].
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

# Write the results.
for i in range(m):
    stdio.write(str(perm[i]) + ' ')
stdio.writeln()