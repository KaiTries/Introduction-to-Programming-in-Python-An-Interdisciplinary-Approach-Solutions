alphabet = "abcdefghijklmnopqrstuvwxyz"


n = 3
n = alphabet[:n]



def combinations(n):
    if len(n) == 0:
        return [[]]
    
    combos = []
    for combo in combinations(n[1:]):
        combos += [combo, combo + [n[0]]]
    return combos

print(combinations(n))
