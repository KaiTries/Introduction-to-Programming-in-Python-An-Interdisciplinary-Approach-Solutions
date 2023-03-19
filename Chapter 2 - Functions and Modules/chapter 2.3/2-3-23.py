#pancake flips


n = [1,2,3,4,4,2,7]

def setup(n):
    for i in range(len(n)):
        if n[i] == max(n):
            return i

def flip(n):
    x = setup(n)
    s = n[:x]
    t = n[x:]
    t = t[::-1]
    new = s + t
    flipped = new[::-1]
    return flipped
        

def pancake(n):
    if len(n) == 1:
        return n
    
    result = []
    x = flip(n)
    result += [x[0]]
    return result + pancake(x[1:])
    
print(pancake(n))

