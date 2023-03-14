#recursive rules
import stdio
import stddraw


def ruler(n):
    if n == 1: return 1
    return ruler(n-1),(n),ruler(n-1) 

print(ruler(4))
#output 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

#now plotting subdivisions
