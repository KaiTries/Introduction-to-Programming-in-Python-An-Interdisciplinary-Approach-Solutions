import random
import sys
import stdarray
import stdio

n = int(input("how many times do you want to shuffle the deck? "))
m = int(input("how big is the deck? "))

# Create a deck of cards.
deck = stdarray.create1D(m, 0)
for i in range(m):
    deck[i] = i

print (deck)
backup = deck
#shuffle the deck n times
results = stdarray.create2D(m,m, 0)

for i in range(n):
    deck[i] = i
    for j in range(m):
        r = random.randrange(j, m)
        temp = deck[j]
        deck[j] = deck[r]
        deck[r] = temp

    for k in range(m):
        for j in range(m):
            if deck[j] == k:
                results[k][j] += 1


# Print the shuffled deck.
print(deck)
print("result matrix is")
for i in range(m):
 for j in range(m):
  print(results[i][j], " ", end='')
 print()

