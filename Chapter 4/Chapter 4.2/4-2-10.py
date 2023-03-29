#dedup
#writes array of strings to output with duplicates removed and in order

a = ["it" ,"was", "the" ,"best", "of", "times", "it" ,"was"]

#just use mergesort for sorting again
from mergesort import sort
import stdio
def depop(a):
    sort(a)
    result = []
    for i in range(len(a)):
        if a[i] not in result:
            stdio.write(a[i])
            result += [a[i]]


depop(a)