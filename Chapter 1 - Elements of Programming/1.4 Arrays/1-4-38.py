#Riffle shuffle. Compose a program to rearrange a deck of n cards using the Gilbert-Shannon-Reeds model of a riffle shuffle. 
#First, generate a random integer r according to a binomial distribution: flip a fair coin n times and let r be the number of heads. 
#Now, divide the deck into two piles: the first r cards and the remaining n - r cards. 
#To complete the shuffle, repeatedly take the top card from one of the two piles and put it on the bottom of a new pile. 
#If there are n1 cards remaining in the first pile and n2 cards remaining in the second pile, 
#choose the next card from the first pile with probability n1 / (n1 + n2) and from the second pile with probability n2 / (n1 + n2). 
#Investigate how many riffle shuffles you need to apply to a deck of 52 cards to produce a (nearly) uniformly shuffled deck.
import random
import stdarray

n = int(input("deck of n cards, input n: "))

#random integer through binomial distribution
r = 0
for i in range(n):
    q = random.random()
    if q > 0.5:
        r += 1

#create the deck of n cards and numerize them, for better readability
deck = stdarray.create1D(n, 0)
for i in range(n):
    deck[i] = i

#split deck into two piles. 
d1 = stdarray.create1D(r, 0)
d2 = stdarray.create1D(n-r,0)
for i in range(r):
    d1[i] = deck[i]

for i in range(n-r):
    d2[i] = deck[i+r]

#riffle shuffle
shuffleddeck = []
i = 0
while len(shuffleddeck) < n:
    if i < len(d1):
        shuffleddeck += [d1[i]]
    if i < len(d2):
        shuffleddeck += [d2[i]]
    i += 1


#riffle shuffle with the probabilities of n1 / (n1 + n2) and from the second pile with probability n2 / (n1 + n2).
#the probabilites will be updated everytime a new card goes into the shuffleddeck, simulating the pile getting smaller.

shuffleddeck = []                       #empty array to house shuffleddeck
L = r                                   #Value for the initial length of the left stack
R = n - r                               #Value for the initial length of the right stack
i = 0                                   #Value deciding which value in the array we will take.
j = 0                                   #Value for the right stack
while len(shuffleddeck) < n:            #shuffling until we did the whole stack.
    x = L / (L + R)                     #gives us the probability of taking a card from the left stack
    u = random.random()                 #random number between 0-1
    if x > u:                           #if x is greater than u we will shuffle in a card of the left stack
        shuffleddeck += [d1[i]]         #i is increased so we move onto the next number in the left stack
        i += 1                          #L is decreased simulating that this pile is now smaller e.g. less probability
        L -= 1
    else:                               #if x is smaller than u we will shuffle in a card from the right stack
        shuffleddeck += [d2[j]]
        j += 1
        R -= 1

#now we will need to do this multiple times at once. 
#below is the stand-alone code for the final program.
#we print the shuffled deck after every iteration

import random
import stdarray


n = int(input("size of deck:"))

deck = stdarray.create1D(n, 0)
for i in range(n):
    deck[i] = i


print(deck)

shuffles = 10
for i in range(shuffles):
    shuffleddeck = []
    r = 0
    for t in range(n):
        q = random.random()
        if q > 0.5:
            r += 1
            
    d1 = stdarray.create1D(r, 0)
    d2 = stdarray.create1D(n-r,0)
    for p in range(r):
        d1[p] = deck[p]

    for p in range(n-r):
        d2[p] = deck[p+r]

    L = r                                   
    R = n - r                               
    k = 0                                   
    j = 0                   
    while len(shuffleddeck) < n:        
        x = L / (L + R)                     
        u = random.random() 
        if x > u:                           
            shuffleddeck += [d1[k]]         
            k += 1                          
            L -= 1
        else:                               
            shuffleddeck += [d2[j]]
            j += 1
            R -= 1
    print(shuffleddeck)
    deck = shuffleddeck