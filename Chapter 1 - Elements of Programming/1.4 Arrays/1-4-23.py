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
        r = random.randrange(0, m-1)
        temp = deck[j]
        deck[j] = deck[r]
        deck[r] = temp
    print(deck)
#    for k in range(m):
#        for j in range(m):
#            if deck[j] == k:
#                results[k][j] += 1


# Print the shuffled deck.
#print(deck)
#print("result matrix is")
#for i in range(m):
# for j in range(m):
#  print(results[i][j], " ", end='')
# print()

#how many times do you want to shuffle the deck? 5
#how big is the deck? 10
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[1, 4, 3, 7, 6, 9, 0, 2, 5, 8]
#[3, 1, 2, 1, 9, 8, 0, 7, 6, 5]
#[9, 1, 2, 6, 3, 5, 1, 8, 7, 0]
#[5, 3, 2, 1, 0, 1, 9, 8, 7, 3]
#[5, 9, 4, 3, 1, 2, 3, 1, 8, 7]

#if we choose a random number between 0 and m-1, we are not shuffling the deck. We are just swapping the first card with a random card. We need to choose a random number between j and m-1. This will shuffle the deck.