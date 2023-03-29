
#-----------------------------------------------------------------------
# merge.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray

#-----------------------------------------------------------------------

# Merge a[lo:mid] with a[mid:hi] using aux as auxiliary memory.

def _merge(a, lo, mid, hi):
    aux = a[:]
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1
    a[lo:hi] = aux[0:n]

#-----------------------------------------------------------------------

# Sort a[lo:hi] into increasing order, using array aux as auxiliary
# memory.

def _sort(a, lo, hi):
    n = hi - lo
    if n <= 1:
        return
    mid = (lo + hi) // 2
    _sort(a, lo, mid)

    _sort(a, mid, hi)

    _merge(a, lo, mid, hi)


#-----------------------------------------------------------------------

# Sort array a into increasing order.

def sort(a):
    n = len(a)
    _sort(a, 0, n)

#-----------------------------------------------------------------------


def main():
    a = ["the" ,"and" ,"was" ,"his", "you" ,"tom" ,"but" ,"for" ,"had" ,"him "]
    sort(a)
    for s in a:
        stdio.write(s + ' ')
    stdio.writeln()

if __name__ == '__main__':
    main()
