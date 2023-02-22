#probability to roll a 1 in 6 rolls



not1 = 1
for i in range(6):
    not1 *= 5/6

print("Probability to roll a 1 in ", 6, " rolls: ", 1 - not1)

#probability to roll at least two 1 in 12 rolls

not1 = 1
for i in range(12):
    not1 *= 5/6

print("Probability to roll at least two 1 in ", 12, " rolls: ", 1 - (not1)-12*(1/6)*(5/6)**11)