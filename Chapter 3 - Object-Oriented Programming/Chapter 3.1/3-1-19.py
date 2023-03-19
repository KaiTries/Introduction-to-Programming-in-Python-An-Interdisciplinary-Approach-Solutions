#a start string and a stop string
#write substrings of a third given string that start with the first tring and end with the second and otherwise contain neiterh
#be careful of overlaps

#e.g. first string A second string T 
#third given string this is a Tree
#sub string would be "a T"
#similar solution to before with DNA
#find start with .find and same with end then repeat with shorter string
string = 'allisgoodbrother,allissuperbigman'


def subStringsinString(a,b,string):
    if len(string) < 2:
        return []
    result = []
    start = string.find(a)
    stop = string.find(b,start)
    if stop == -1:
        return []
    result += [string[start:stop+1]]
    return result + subStringsinString(a,b,string[stop+1:])

print(subStringsinString('a','b',string))
#['allisgoodb', 'allissuperb']