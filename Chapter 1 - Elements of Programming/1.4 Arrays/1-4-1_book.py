import random
import sys
import stdarray
import stdio
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck =[]
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck += [card]

m = 5 #choose this many elements
n = 52 #number of elements in the deck


#inizialize array perm with values 0, 1, 2, ..., n-1
perm = stdarray.create1D(n, 0)
for i in range(n):
    perm[i] = i

#create a random sample of m elements from perm
for i in range(m):
    r = random.randrange(i, n)
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

#write the sample to standard output
for i in range(m):
    stdio.write(deck[perm[i]])
    stdio.write(' ')
    stdio.writeln()

