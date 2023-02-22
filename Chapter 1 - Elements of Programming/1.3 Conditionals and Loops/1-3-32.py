import math


n = int(input("Enter the number: "))

for a in range(n):
    a3 = a**3
    if a3 > n:
        break

    for b in range(a, n):
        b3 = b**3
        if a3 + b3 > n:
            break

        for c in range(a + 1, n):
            c3 = c**3
            if (a3 + b3) < c3:
                break

            for d in range(c, n):
                d3 = d**3
                if (a3 + b3) < (c3 + d3):
                    break
                if (a3 + b3) == (c3 + d3):
                    print("for: ",(a**3+b**3), "Cube numbers are: ", a, b, c, d)
                    break



