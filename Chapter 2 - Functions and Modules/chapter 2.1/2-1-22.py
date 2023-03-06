import random
import stdarray




def walk_in(x):                     #random birthday function that keeps adding to argument array until repeat number
    while True:
        r = random.randint(1,365) 
        if r not in x:
            x += [r]
        else:
            break
    return x              

def fill_room():                   #houses the walking in function holds the room, return the length of the room to make calculation easier
    room = []
    walk_in(room)
    return len(room)

def trials(n):                      #function that goes through the birthday problem as many times as given by argument n, returns the average of number of birthdays.
    lengthrooms = 0
    for i in range(n):
        lengthrooms += fill_room()
    return lengthrooms/n



print(trials(100000))

