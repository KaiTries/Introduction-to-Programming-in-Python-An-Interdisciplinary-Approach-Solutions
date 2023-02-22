

a = [1, 2, 3, 4, 5, 5, 5, 8, 9, 10]

longestSequence = 0
location = 0

for i in range(len(a)):
    currentSequence = 0
    for j in range(i, len(a)):
        if a[j] == a[i]:
            currentSequence += 1
        else:
            break
    if currentSequence > longestSequence:
        longestSequence = currentSequence
        location = i

print("Longest sequence: " + str(longestSequence))
print("Location: " + str(location))