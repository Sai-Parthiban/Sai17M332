n=int(input())
li=[]
for i in range(n):
    x,y=map(int,input().split())
    l=[]
    l.extend([x,y,i+1])
    li.append(t)
d=sorted(li,key=lambda x:(x[1],-x[0],-x[2]))
for i in d:
    print(i[2],end=" ")
