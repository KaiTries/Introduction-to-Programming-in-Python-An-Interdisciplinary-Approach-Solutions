#music shuffle
import random
import stdarray

m = int(input("how many song do you have? "))

music = stdarray.create1D(m, 0)
for i in range(m):
    music[i] = i



for i in range(m):
    r = random.randrange(i, m)
    temp = music[i]
    music[i] = music[r]
    music[r] = temp

print(music)

#chance songs are not consecutive in the shuffled list


consecutive = 0
for i in range(m-1):
    if music[i] == music[i+1] - 1:
        consecutive += 1


print("Chance songs are consecutive in the shuffled list is ",(100 * consecutive / m),  "%")
