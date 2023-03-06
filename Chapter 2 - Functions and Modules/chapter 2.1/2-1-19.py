import math
import stdio
import stdarray


def any(a):
    if True in a:
        return True
    else:
        return False
    


a = [True,True, True]

print(any(a))

def all(a):
    if False not in a:
        return True
    else:
        return False
    
print(all(a))

