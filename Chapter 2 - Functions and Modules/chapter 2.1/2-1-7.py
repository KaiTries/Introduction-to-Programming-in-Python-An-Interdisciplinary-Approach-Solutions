def lg(n):
    base = 2
    count = 1
    while base**count < n:
        count += 1
    if base**count > n: return count-1
    else: return count



print(lg(1025))

