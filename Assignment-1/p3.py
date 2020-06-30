n=int(input())
li=list(map(int,input().split()))
m,c=li[0],li[0]
for i in range(1,n):
    c=max(li[i],c+li[i]) 
    m=max(m,c) 
print(m) 
