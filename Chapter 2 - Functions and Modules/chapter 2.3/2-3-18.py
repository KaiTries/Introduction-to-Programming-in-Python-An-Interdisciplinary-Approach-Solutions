#perm of alphabet

alphabet = "abcdefghijklmnopqrstuvwxyz"

k = 3
n = alphabet[:k]


def permutation(array):
    if len(array) == 1:
        return [array]

    perms = permutation(array[1:])
    char = array[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print(permutation(n))
