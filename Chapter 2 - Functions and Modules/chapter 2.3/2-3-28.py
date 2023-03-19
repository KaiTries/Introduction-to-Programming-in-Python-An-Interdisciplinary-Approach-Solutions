#binom with memo
import stdarray



def binomial(n, k,memo):
    if n in memo and k in memo:
        return memo[n][k]
    if (n == 0) or (k < 0):
        return 0
    if n == 0 or k == 1:
        return 1
    memo[n][k] = binomial(n-1, k,memo) + binomial(n-1, k-1,memo)
    return memo[n][k]



k = 100
n = 50
memo = stdarray.create2D(n+1,k+1,0)


print(binomial(n,k,memo))


print(memo)