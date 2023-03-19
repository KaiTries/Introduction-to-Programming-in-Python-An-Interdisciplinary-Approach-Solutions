#detecting circular shift
#e.g. ACTGACG is a circular shift of TGACGAC
#the characters are the same the starting point is just shifted

a = 'ACTGACG'
b = 'TGACGAC'

def isCircular(a,b):
    return a in b+a and b in b+a

print(isCircular(a,b))