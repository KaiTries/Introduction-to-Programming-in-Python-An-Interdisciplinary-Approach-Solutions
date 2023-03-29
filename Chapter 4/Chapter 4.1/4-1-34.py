#array notation


#given array reverse it at point k


def reverse(a,k):
    reversed_part = a[:k]
    reversed_part = reversed_part[::-1]
    return reversed_part + a[k+1:]


def reversedO(a,k):
    reversed_part = a[k:]
    reversed_part = reversed_part[::-1]
    return reversed_part + a[:k]