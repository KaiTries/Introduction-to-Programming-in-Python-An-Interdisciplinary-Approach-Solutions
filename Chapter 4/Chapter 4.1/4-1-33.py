#anysum
import stdarray
import stdio

#input

n = 10

numbers = stdio.readAllInts()


def subsets(numbers):
    subset =  []
    for i in range(n):
        for j in range(i,n):
            if sum(numbers[i:j+1]) == 0:
                subset += [numbers[i:j+1]]
    return subset
