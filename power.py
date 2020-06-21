from math import sqrt as s
from collections import Counter as c
n=int(input())
li=[]
while n%2 == 0:
    li.append(2)
    n//=2
for i in range(3,int(s(n))+1,2):
    while n%i == 0:
        li.append(i)
        n//=i
if n>2:
    li.append(n)
for i,j in dict(c(li)).items():
    print(i,j)
