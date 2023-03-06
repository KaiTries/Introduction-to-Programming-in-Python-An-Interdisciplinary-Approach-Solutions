import random
import sys
import stdarray
import stdio
import math


def deck():     #creates deck
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck =[]
    for rank in RANKS:
        for suit in SUITS:
            card = rank + ' of ' + suit
            deck += [card]
    return deck

def shuffle(x):     #shuffles an array
    for i in range(len(x)):
        r = random.randrange(i,len(x))
        temp = x[r]
        x[r] = x[i]
        x[i] = temp
    return x

def hands(n,deck):
    x = str('All hands have been dealt have fun playing')
    for i in range(n):
        stdio.writeln("-----------------")
        stdio.writeln("this is the " + str(i + 1) + "th hand")
        stdio.writeln("-----------------")
        for j in range(5):
            stdio.writeln(deck[j])
    stdio.writeln("-----------------")
    return x


n = int(sys.argv[1]) #how many hands 


print(hands(n,shuffle(deck())))