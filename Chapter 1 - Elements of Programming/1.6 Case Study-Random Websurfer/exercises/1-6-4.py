import random
moves = 0
n = 0
p = 0


for i in range(moves):                      #how many times do we switch a page
    r = random.random()                     #gives randomness
    total = 0.0                             #counter 
    for j in range(0,n):                    #iterates through all the possibible paths from the current page
        total += p[page][j]                 #adds the value of the probability per path together
        if r < total:                       #if the values have exceeded the value given by randomnesss 
            page = j                        #we move to that page
            break
    if r > total:
        r = random.uniform(0,total)
        total = 0.0
        for j in range(0,n):
            total += p[page][j]
            if r > total:
                page= j
                break



# if the probabilities do not add up to 1 then r could be bigger than the total after j has iterated through all page links.
#we can fix this by adding an if statement to repeat the process. -> else: create a new r that is random.uniform(0,total) -> same for statement. 