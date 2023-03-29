#mode of an array



def mode(a):
    a.sort()
    current_count = 1
    max_count = 0
    mod = 0
    for i in range(1,len(a)):
        if a[i-1] == a[i]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mod = a[i-1]
            current_count = 0
    return mod


