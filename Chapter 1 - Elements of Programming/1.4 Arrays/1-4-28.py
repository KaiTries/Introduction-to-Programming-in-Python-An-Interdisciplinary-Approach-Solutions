#Rumors. Alice is throwing a party with n other guests, including Bob. Bob starts a rumor about Alice by telling it to one of the other guests. 
#A person hearing this rumor for the first time will immediately tell it to one other guest, chosen at random from all the people at the party except Alice and the person from whom they heard it. 
#If a person (including Bob) hears the rumor for a second time, he or she will not propagate it further. 
#Compose a program to estimate the probability that everyone at the party (except Alice) will hear the rumor before it stops propagating. 
#Also calculate an estimate of the expected number of people to hear the rumor.


import stdio
import stdarray
import sys
import random


n = int(input("Number of guests: ")) #number of guests
m = int(input("Number of iterations: ")) #number of iterations
GR = stdarray.create2D(m, n, False) #guests who have heard the rumor at each iteration

for i in range(m):
    G = stdarray.create1D(n, False) #guests who have heard the rumor at each iteration
    G[0] = True #Bob starts a rumor about Alice by telling it to one of the other guests
    z = True #z is True if the rumor is still propagating                                                                        
    while z:
        a = G[0]                                                                    
        r = random.randint(0, n-1)                                                  
        if G[r] == a: #if person tells the rumor to himself, nothing happens                                                                
            a = a
        if G[r] == True: #if person hears the rumor for a second time, he or she will not propagate it further                                                            
            z = False
        else: #if person hears the rumor for the first time, he or she will immediately tell it to one other guest, chosen at random from all the people at the party except Alice and the person from whom they heard it
            G[r] = True                                                            
            a = G[r]      
    GR[i] = G #guests who have heard the rumor at each iteration  


#probability that everyone at the party (except Alice) will hear the rumor before it stops propagating
p = 0
for i in range(m):
    if sum(GR[i]) == n: #True counts as a 1, False counts as a 0 
        p += 1
    print(GR[i])

print("probability that everyone at the party (except Alice) will hear the rumor before it stops propagating:", p/m)

#expected number of people to hear the rumor
e = 0
for i in range(m):
    e += sum(GR[i])
print("expected number of people to hear the rumor:", e/m)