from collections import Counter as co
t,n=map(int,input().split())
l=[]
for i in range(t):
    l.append(list(input()))
l1=list(zip(*l))
#print(l1)
s=""
for i in l1:
    c=co(sorted(i))
    s+=c.most_common(1)[0][0]
print(s)
