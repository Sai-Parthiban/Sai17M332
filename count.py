from math import gcd as g
from itertools import permutations as p
n=int(input())
li=[i for i in range(1,n+1)]
c=n
for i in list(p(li,2)):
    if g(i[0],i[1])==i[1]:
        c+=1
print(c)
