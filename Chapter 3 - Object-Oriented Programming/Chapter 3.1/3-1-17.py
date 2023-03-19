#mystery function

def mystery(s):
    n = len(s)
    if n <= 1: return s
    a = s[0: n//2]
    b = s[n//2: n]
    return mystery(b) + mystery(a)


s = 'hello'

print(mystery(s))


#it flips it in the middle