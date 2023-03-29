




def furthestFrom(array):
    solution = ()
    diff = 0
    n = len(array)
    for i in array:
        for j in array:
            if i != j:
                if i+j > diff:
                    diff = i+j
                    solution = (i,j)
    return solution

def furthestfast(array):
    top = max(array)
    x = array.index(top)
    second = max(array[:x]+array[x+1:])
    return (top,second)


a = [1,2,3,4,5,6,7]

print(furthestfast(a))
print(furthestFrom(a))