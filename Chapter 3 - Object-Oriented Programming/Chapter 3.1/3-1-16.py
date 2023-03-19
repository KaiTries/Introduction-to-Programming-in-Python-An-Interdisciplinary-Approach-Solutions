#given domain name return the reverse domain

URL = 'https://introcs.cs.princeton.edu/python/31datatype/'

def _fullDomain(string):
    x = string.rfind('.')           #gives last index of searched character
    t = string.find('//')
    domain = string[t+2:x+4]
    return domain


def reverseDomain(string):
    string = _fullDomain(string)
    string_list = string.split('.')
    string_list = string_list[::-1]
    return '.'.join(string_list)

print(reverseDomain(URL))