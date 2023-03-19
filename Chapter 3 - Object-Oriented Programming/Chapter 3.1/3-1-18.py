#potential gene that finds all potential genes in a long dna string
#command line argument for minimum length of genes

#my command line argument will just be 6
import sys
import stdio
from instream import InStream



def isPotentialGene(dna):
    #number of bases is a multiple of 3
    if (len(dna) % 3) != 0: return False

    #starts with start codon
    if not dna.startswith('ATG'): return False

    #no intervening stop codons
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i:i+3] == 'TAA': return False
            if dna[i:i+3] == 'TAG': return False
            if dna[i:i+3] == 'TGA': return False
    
    #ends with a stop codon
    if dna.endswith('TAA'): return True
    if dna.endswith('TAG'): return True
    if dna.endswith('TGA'): return True

    return False

n = 6



#create your own txt file to test out the code
src = InStream('genes.txt')

DNA = src.readAllLines()
DNA = ''.join(DNA)
#string with find() find first index where we have a starter codon
#then we find first sequence were we have end codon
#if the length is > minimum length we add it to our result array, else we discard it
#then we loop through the entire thing again but wit hthe string[i:], starting point being after the ending codon
def findGenes(n,string=str):
    if len(string) < n:
        return []
    results = []
    start = string.find('ATG')
    stopTAA = string.find('TAA',start+3+n)
    stopTAG = string.find('TAG',start+3+n)
    stopTGA = string.find('TGA',start+3+n)
    stop = min(stopTAA,stopTAG,stopTGA)
    potentialDNA = string[start:stop+3]
    if isPotentialGene(potentialDNA):
        results += [potentialDNA]
    return results + findGenes(n,string[start+3:])

print(findGenes(5,DNA))



