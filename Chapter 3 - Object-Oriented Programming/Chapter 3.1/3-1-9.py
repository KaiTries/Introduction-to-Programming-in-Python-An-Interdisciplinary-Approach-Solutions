#define a function that only returns true if a given string only consists of ACT and G
#we can check for number of unique characters
#and the just checking if ACT and G are in the string
#if they all are in the string and the number of unique characters is 4 then it will return true


string = "AATTACTG"

#we can create a set class to get the unique characters
string_set = set(string)
print(string)
print(string_set)
#would make it to easy 

#this is a function that achieves the same
#it checks the count of the wanted characters if they are the same as the entire length of the string,
#the string only consists of those characters.

def isValidDNA(string):
    #string = string.upper()     add this so the function is not case sensitive
    x = len(string)
    A = string.count('A')
    C = string.count('C')
    T = string.count('T')
    G = string.count('G')
    if (A+C+T+G) == x:
        return True
    return False

print(isValidDNA(string))