#given string that represents website URl compase code fragment that determins its domain type
#domain type is .com .ch or .deu -> com, ch or edu



URL = 'https://introcs.cs.princeton.edu/python/31datatype/'

def domainType(string):
    x = string.rfind('.')           #gives last index of searched character
    domain = string[x:x+4]
    return domain

print(domainType(URL))