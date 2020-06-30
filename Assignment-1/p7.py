n,l1,l2,d,m=int(input()),[],[],[],0
for i in range(n):
    x,y=map(int,input().split())
    l1.append(x)
    l2.append(y)
for i in range(n):
    a,b=sum(l1[:i+1]),sum(l2[:i+1])
    if a-b>0:
        if a-b>m:
            m=a-b
            w=1
    else:
        if a-b>m:
            m=a-b
            w=2        
print(w,m)
