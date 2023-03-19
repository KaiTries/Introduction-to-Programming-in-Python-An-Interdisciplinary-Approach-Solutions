#check if a given DNA string is watson crick complemented palindrome
#e.g. if the DNA string is the same as the watson-crick backwards
#first create the watsoncrick
#then flip it with s[::-1]
#then simple for loop to check if theyre the same

DNA = 'ACTG' #this should return False
DNA = 'ACGT' #this should return True

def complementWC(string):
    n = len(string)
    for i in range(n):
        if string[i] == 'A':
            string = string[:i] + 'T' + string[i+1:]
        elif string[i] == 'T':
            string = string[:i] + 'A' + string[i+1:]
        elif string[i] == 'C':
            string = string[:i] + 'G' + string[i+1:]
        elif string[i] == 'G':
            string = string[:i] + 'C' + string[i+1:]
        else:
            return "string is not DNA"
    return string

def palindromeWC(DNA):
    WC = complementWC(DNA)
    flippedWC = WC[::-1]
    for i in range(len(DNA)):
        if flippedWC[i] != DNA[i]:
            return False
    return True

print(palindromeWC(DNA))
