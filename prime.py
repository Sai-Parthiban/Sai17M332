from math import sqrt as s
n,k=map(int,input().split())
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
if k>len(li):
    print(-1)
else:
    print(li[k-1])
