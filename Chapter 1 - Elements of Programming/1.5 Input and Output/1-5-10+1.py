import sys
import stdio
import random


m = int(sys.argv[1])
n = int(sys.argv[2])


for i in range(n):
    print(random.randint(0,m-1))