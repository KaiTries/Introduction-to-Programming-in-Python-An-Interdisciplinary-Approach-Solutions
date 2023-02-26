#Birthday problem. Suppose that people continue to enter an empty room until a pair of people share a birthday. On average, 
#how many people will have to enter before there is a match? 
#Run experiments to estimate the value of this quantity. Assume birthdays to be uniform random integers between 0 and 364.

import random
import stdarray

#below the basic logic that needs to be done

room = []                   #empty room
r = random.randint(1,365)   #random birthday
room += [r]                 #add birthday to room
print(room)                 #show result


#now we need to continously add a random birthday to the room until there is a match.
#for this we use a while loop that is True while there are no matches.
z = True
while z:
    r = random.randint(1,365)
    if r not in room:       #if the value is not yet in the array we add it.
        room += [r]
    else:                   #to test code you can also add a room += [r] here to check if it is in the array twice
        z = False 

print(room)                 #print the final array and its length to get how many people are in the room.
print("the number of people in the room is: ", len(room))



#to get the average we can automate this to run a for loop with range of trials.
trials = 20000
lengthrooms = 0 # we have to store the length of each iteration.
for i in range(trials):
    room = []
    z = True
    while z:
        r = random.randint(1,365)
        if r not in room:
            room += [r]
        else:
            z = False
    length = len(room)
    lengthrooms += length

print("the average number of people in the room is: ", lengthrooms / trials)

#through this we get the average number of people that can be in a room where everyone has a different birthday is around 23.6