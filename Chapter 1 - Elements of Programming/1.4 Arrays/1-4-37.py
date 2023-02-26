#Coupon collector. Run experiments to validate the classical mathematical result that the expected number of coupons needed to collect n values is about nHn. 
#For example, if you are observing the cards carefully at the blackjack table (and the dealer has enough decks randomly shuffled together), 
#you will wait until about 235 cards are dealt, on average, before seeing every card value.
import math
import random
y = 0.577215664901
n = int(input("how many different coupons: "))
#we test this with the blackjack table: a deck has 52 different cards and we want to add an additional card until we have seen all of them
#now we need to adjust to code so that it will run until b has seen all possible values and returns the length of a for our cards dealt.
#we know that b has seen all the possible valus if its length is the same as the possible values.
trials = int(input("number of trials: "))
length = 0
for i in range(trials):    
    a=[]
    b=[]
    while len(b) < n:
        r = random.randint(1,n)
        a +=[r]
        if r not in b:
            b += [r]
    length += len(a)
    

result = n * math.log(n) + n*y +(1/2)   #this is how many we should get through the mathematical formula
print(result)
print(length/trials)                    #this is our actual average we get through testing