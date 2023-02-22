def eulers_sum_of_powers():
    max_n = 145
    pow_5 = [n**5 for n in range(max_n)]
    pow5_to_n = {n**5: n for n in range(max_n)}
    for x0 in range(1, max_n):
        for x1 in range(1, x0):
            for x2 in range(1, x1):
                for x3 in range(1, x2):
                    pow_5_sum = sum(pow_5[i] for i in (x0, x1, x2, x3))
                    if pow_5_sum in pow5_to_n:
                        y = pow5_to_n[pow_5_sum]
                        return (x0, x1, x2, x3, y)

print(eulers_sum_of_powers())
#slow solution
#max_n = 145
#for a in range (1 , max_n):
#    for b in range (a, max_n):
#        for c in range (b, max_n):
#            for d in range (c, max_n):
#                for e in range (d+1,max_n):
#                    if a**5 + b**5 + c**5 + d**5 < e**5:
#                        break
#                    if a**5 + b**5 + c**5 + d**5 == e**5:
#                        print (a, b, c, d, e)
#                        break
                    
max_n = 145

for a in range (1 , max_n):
    a_5 = a**5
    for b in range (a, max_n):
        b_5 = b**5
        for c in range (b, max_n):
            c_5 = c**5
            for d in range (c, max_n):
                d_5 = d**5
                lhs_sum = a_5 + b_5 + c_5 + d_5
                for e in range (d+1,max_n):
                    e_5 = e**5
                    if lhs_sum < e_5:
                        break
                    if lhs_sum == e_5:
                        print (a, b, c, d, e)
                        break