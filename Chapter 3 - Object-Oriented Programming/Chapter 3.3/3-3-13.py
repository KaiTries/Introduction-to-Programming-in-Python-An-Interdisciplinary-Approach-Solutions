#fibonacci



#recursive

def fibonacciR(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacciR(n - 1) + fibonacciR(n - 2)

print(fibonacciR(11))

#iterative

def fibonacciI(n):
    total = 0
    first = 0
    second = 1
    temp = 0
    for i in range(n):
        temp = second
        second = second + first
        first = temp
        total += first
    return first

print(fibonacciI(11))

#iterativeTuples

def fibonacciIT(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, b + a
    return a

print(fibonacciIT(11))