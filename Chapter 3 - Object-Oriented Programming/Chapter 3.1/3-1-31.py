#entropy
import stdarray
import math
#n characters in a string
#fc frequency of occurence of character c
#quantity pc = fc / n is an estimate of the probability that c would be in the tring it it were a random string
#enttropy is the quantity pc log2(pc) over all characters that appear in the string
#if each character appears the same number of times entropy is at its minimum


string = 'abc'
string = string.replace(' ','')
n = len(string)
#collect all unique characters
characters = []
for char in string:
    if char not in characters:
       characters += [char]
#give frequency of all unique characters
characters_freq = stdarray.create1D(len(characters),0)
for i in range(len(string)):
    for j in range(len(characters)):
        if characters[j] == string[i]:
            characters_freq[j] += 1

#give pc = fc / n
characters_P = []
characters_P = [freq/n for freq in characters_freq]
#calculate the entropy
characters_entropy = []
characters_entropy = [-(prob*math.log(prob,2)) for prob in characters_P]
string_entropy = sum(characters_entropy)

print(string_entropy)

def entropy_ideal(length):
    "Calculates the ideal Shannon entropy of a string with given length"

    prob = 1.0 / length

    return -1.0 * length * prob * math.log(prob) / math.log(2.0)

print(entropy_ideal(n))