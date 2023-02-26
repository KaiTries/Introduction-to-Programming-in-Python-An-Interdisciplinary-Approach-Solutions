#Bridge hands. In the game of bridge, four players are dealt hands of 13 cards each. 
#An important statistic is the distribution of the number of cards in each suit in a hand. Which is the most likely, 5-3-3-2, 4-4-3-2, or 4-3-3-3? 
#Compose a program to help you answer this question.

#bridge uses standard 52-card deck.

import random
import stdarray

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] #ranks are irrelevant in this scenario -> use it just for the amount of cards

p1 = stdarray.create1D(13, 0)   #initialize an array for one of the players

deck =[]                        #creates the deck array with only suits.  -> 13times each suit.         
for rank in RANKS:
    for suit in SUITS:
        card = suit
        deck += [card]

deck2 = deck                    #storing the unshuffled deck in a seperate object.

n = len(deck)                 

trials = 2000                   #how many times we iterate over the shuffling -> 2000 should give enough for result
order1 = 0                      #order of: 5-3-3-2
order2 = 0                      #order of: 4-4-3-2
order3 = 0                      #order of: 4-3-3-2

for i in range(trials):         #each iteration we initialize the unshuffled deck and set the counts of the suits to 0
    deck = deck2
    countC = 0
    countH = 0
    countS = 0
    countD = 0
    for j in range(n):          #then we shuffle the whole deck
        r = random.randrange(j,n)
        temp = deck[r]
        deck[r] = deck[j]
        deck[j] = temp
    for t in range(13):         #we hand out 13 cards to the player
        p1[t] = deck[t]
    for l in range(13):         #we count the number of each suit
        if p1[l] == 'Clubs':
            countC += 1
        elif p1[l] == 'Hearts':
            countH += 1
        elif p1[l] == 'Spades':
            countS += 1
        elif p1[l] == 'Diamonds':
            countD += 1
    if countC == 5 and countH == 3 and countS == 3:         #if one of the wanted orders is handed out we increase its count by 1
        order1 += 1
    elif countC == 4 and countH == 4 and countS == 3:
        order2 += 1
    elif countC == 4 and countH == 3 and countS == 3:
        order3 += 1

averagecount1 = order1 / trials     #the average of the respective order.
averagecount2 = order2 / trials
averagecount3 = order3 / trials
print("number of runs: ", trials)
print("Average Number of 5-3-3-2; ",averagecount1)
print("Average Number of 4-4-3-2; ", averagecount2)
print("Average Number of 4-3-3-3; ", averagecount3)

#number of runs:  2000
#Average Number of 5-3-3-2;  0.012
#Average Number of 4-4-3-2;  0.015
#Average Number of 4-3-3-3;  0.025
#the order 4-3-3-3 its the most common one.
