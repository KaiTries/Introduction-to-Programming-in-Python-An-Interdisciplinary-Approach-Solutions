#create function watson crick complement of dna


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


string = "ATCG"
print(complementWC(string))

