#instead of max guessses give range of possible ns


n = 10


def questions(low,high):
    if (high - low )== 1: return print(low)


    mid = (low + high) // 2
    print(mid)
    x = int(input("is it bigger and or equal? "))
    if x == 1:
        questions(mid,high)

    else:
        questions(low,mid)





questions(0,n+1)