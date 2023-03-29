#binary search that accounts for x not in index returns either val thats next biggest.



#-----------------------------------------------------------------------
# binarysearch.py
#-----------------------------------------------------------------------

import sys
import stdio
import instream

#-----------------------------------------------------------------------

# Return the index of key in array a[lo:hi], or -1 if key is not
# present.

def _search(key, a, lo, hi):
    if hi <= lo and key < a[0]:
        return -1
    elif hi <= lo:
        return lo -1 
    mid = (lo + hi) // 2

    # Python 2.6 implements a cmp() function which calls a __cmp__()
    # method.  But Python 3.x does not.  So must use < instead.

    if key < a[mid]:
        return _search(key, a, lo, mid)
    elif a[mid] < key:
        return _search(key, a, mid+1, hi)
    else:
        return mid

#-----------------------------------------------------------------------

# Return the index of key in array a, or -1 if key is not present.

def search(key, a):
    return _search(key, a, 0, len(a))

#-----------------------------------------------------------------------

# Accept as a command-line argument a string which is the name of a
# whitelist file. Write to standard output the keys in standard input
# that are not in the whitelist file.

def main():
    a = [1,3,4,5,6,8,9,10,11]
    print(search(12,a))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------
