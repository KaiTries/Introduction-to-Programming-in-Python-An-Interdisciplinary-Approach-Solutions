#largest empty interval



#sort the timeframes find the biggest disparity
#go through it once and keep the longest timedisparity stored


def disparity(a):
    a.sort()
    n = len(a)
    diff = 0
    for i in range(n-1):
        if a[i]-a[i+1] < diff:
            diff = a[i] - a[i+1]
    return diff