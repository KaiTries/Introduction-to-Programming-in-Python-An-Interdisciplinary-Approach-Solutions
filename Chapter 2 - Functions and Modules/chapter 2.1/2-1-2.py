
def odd(a,b,c):
    if False not in (a,b,c):
        return True
    elif a + b + c == 1:
        return True
    else:
        return False

a = False
b = False
c = True

print(odd(a,b,c))