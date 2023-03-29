#no2slash





def no2slash(string):
    solution = ''
    for i in range(len(string)):
        if not(string[i] == '/' and string[i-1] == '/'): solution += string[i]
    return solution


string = '/d1///d2////d3/test.htm'

print(no2slash(string))