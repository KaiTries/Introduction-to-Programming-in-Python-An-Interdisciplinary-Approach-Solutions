

def closestTo(array):
    solution = ()
    diff = 100
    n = len(array)
    for i in range(n):
        for j in range(n):
            if i != j:
                if abs(i-j) < diff:
                    diff = abs(i-j)
                    solution = (i,j)
    return solution



a = [1,2,3,4,5,6,7]

print(closestTo(a))