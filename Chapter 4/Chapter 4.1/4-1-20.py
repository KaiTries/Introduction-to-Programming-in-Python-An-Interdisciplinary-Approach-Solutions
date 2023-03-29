import sys


n = int(sys.argv[1])
speed = 1
for i in range(0,120,n):
    speed *= 2

print(speed)