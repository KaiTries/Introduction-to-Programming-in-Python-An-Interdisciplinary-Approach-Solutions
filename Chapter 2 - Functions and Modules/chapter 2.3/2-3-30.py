#collatz
import stdio
import stdarray

def collatz(n):
    stdio.write(str(n) + ' ')
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3*n + 1)



def collatz(n,memo):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    elif n % 2 == 0:
        memo += [n]
        collatz(n // 2,memo)    
    else:
        memo += [n]
        collatz(3*n + 1,memo)

n = 10
memo = []
print(collatz(n,memo))
print(memo)