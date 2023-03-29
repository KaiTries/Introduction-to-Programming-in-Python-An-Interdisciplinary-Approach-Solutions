#young tableau is ordered which means if x is bigger than a[0][0] and smaller then a[len(a)][len(a[len(a)])] it is in it


tableau = [[5, 23, 54, 67, 89],[6, 69, 73, 74, 90],[10, 71, 83, 84, 91,],[60, 73, 84, 86, 92,],[90, 91, 92, 93, 94]]

def invert(tableau):
    table = []
    for i in range(len(tableau)):
        row = []
        for j in range(len(tableau)):
            row += [tableau[j][i]]
        table += [row]
    return table

def youngTableau(tableau, x):
    minimum = tableau[0][0]
    maximumum = tableau[len(tableau)-1][len(tableau)-1]
    if x < minimum or x > maximumum: return False
    for i in range(len(tableau)):
        if x in tableau[i]:return True
    return False


print(youngTableau(tableau,73))