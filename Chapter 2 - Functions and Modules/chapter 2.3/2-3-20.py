alphabet = "abcdefghijklmnopqrstuvwxyz"
a = 0
n = 5
n = alphabet[a:n]
k = 3


def perm(n,k):
    res = []

    def backtrack(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return
        
        for i in range(start,len(n)):
            comb.append(n[i])
            backtrack(i + 1, comb)
            comb.pop()
    backtrack(0,[])
    return res


print(perm(n,k))