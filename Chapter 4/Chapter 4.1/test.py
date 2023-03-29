



def divisorSubstrings( num: int, k: int) -> int:
    count = 0
    string = str(num)
    for i in range(0,len(string)-k+1):
        sub = ''
        for j in range(i,i+k):
            sub += string[j]
            print(sub)
        test = int(sub)
        if test != 0:
            if num % test == 0:
                count += 1
    return count



print(divisorSubstrings(240,2))