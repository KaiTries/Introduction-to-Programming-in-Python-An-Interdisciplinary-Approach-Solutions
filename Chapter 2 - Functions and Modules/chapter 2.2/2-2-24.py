#poker analysis
import stdrandom
import stdio

rans = [2,3,4,5,6,7,8,9,10,11,12,13,14]    #using numbers for faces just for simplicity in programming
sus = ["H","C","D","S"]


#create a deck

def deck(ranks,suits):
    deck = []
    for rank in ranks:
        for suit in suits:
            deck += [(rank,suit)]
    return deck

def hands(deck):
    stdrandom.shuffle(deck)
    hand = []
    for i in range(5):
        hand +=[deck[i]]
    return hand

def simulation(trials):
    pair = 0
    two_pair = 0
    three_kind = 0
    full_house = 0
    flush = 0
    straight = 0
    straight_flush = 0
    x = deck(rans,sus)
    for i in range(trials):
        hand = hands(x)
        ranks = []
        for i in range(len(hand)):
            ranks += [hand[i][0]]
        suits = []
        for i in range(len(hand)):
            suits += [hand[i][1]]        
        ranks_count = []
        for i in range(len(ranks)):
            count = 1
            for j in range(i+1,len(ranks)):
                if ranks[i] == ranks[j]:
                    count += 1
            ranks_count += [count]
        suits_count = []
        for i in range(len(suits)):
            count = 1
            for j in range(i+1,len(suits)):
                if suits[i] == suits[j]:
                    count += 1
            suits_count += [count]            

        if sum(ranks_count) == 6:
            pair += 1
        if sum(ranks_count) == 7:
            two_pair += 1
        if sum(ranks_count) == 8:
            three_kind += 1
        if sum(ranks_count) == 9:
            full_house += 1
        if sum(suits_count) == 15 and ((max(ranks) - min(ranks)) != 4):
            flush += 1
        if sum(suits_count) == 15 and ((max(ranks) - min(ranks)) == 4):
            straight_flush += 1
        if sum(suits_count) != 15 and ((max(ranks) - min(ranks)) == 4):
            straight += 1

    stdio.writef("The probability of getting a pair is: %1.5f \n",pair/trials)
    stdio.writef("The probability of getting a two pair is: %1.5f \n",two_pair/trials)
    stdio.writef("The probability of getting a three kind is: %1.5f \n",three_kind/trials)
    stdio.writef("The probability of getting a full house is: %1.5f \n",full_house/trials)
    stdio.writef("The probability of getting a flush is: %1.5f \n",flush/trials)
    stdio.writef("The probability of getting a straight is: %1.5f \n",straight/trials)
    stdio.writef("The probability of getting a straight flush is: %1.5f \n",straight_flush/trials)



trials = 100000
simulation(trials)
