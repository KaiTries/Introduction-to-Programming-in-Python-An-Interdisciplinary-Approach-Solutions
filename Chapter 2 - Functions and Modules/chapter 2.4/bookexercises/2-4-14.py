#already modified the functions to allow rectangular systems beforehand

import estimate


n = 10
m = 20
p = 0.5
print(estimate.evaluate(n,m,p,1000))        #0.348

print(estimate.evaluate(m,n,p,1000))        #0.014

#wide bois are better!