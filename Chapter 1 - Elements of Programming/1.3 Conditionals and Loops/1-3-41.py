#game simulation monte hall problem

import random

n = int(input("How many times do you want to play? "))

winswitch = 0
lose = 0

for i in range(0,n):
    prize = random.randrange(0,3)
    choice = random.randrange(0,3)
    reveal = random.randrange(0,3)
    while reveal == prize or reveal == choice:
        reveal = random.randrange(0,3)
    other = 0 + 1 + 2 - reveal - choice

    if other == prize:
        winswitch += 1
    else:
        lose += 1

fractionWon = winswitch/n

print("You won", winswitch, "times out of", n, "for a fraction of", fractionWon)