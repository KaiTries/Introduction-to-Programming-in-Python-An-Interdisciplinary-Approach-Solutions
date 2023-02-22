import random
import math
import stdio
import sys

stake = int(input("stake:"))
goal = int(input("goal:"))
trials = int(input("trials:"))
maxbets = int(input("maxbets:"))

countbets = 0
wins = 0
for t in range(trials):
    bets = 0
    cash = stake
    while (cash > 0) and (cash < goal) and (bets < maxbets):
            bets += 1
            countbets += 1
            if random.randrange(0,2) == 0:
                cash += 1
            else:
                cash -= 1
    if cash == goal:
        wins += 1

print(wins)
print(bets)
print(trials)
print(maxbets)
stdio.writeln(str(100*wins//trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(countbets//trials))
stdio.writeln("expected cash: " + str(((100*wins//trials)/100) *(goal)))