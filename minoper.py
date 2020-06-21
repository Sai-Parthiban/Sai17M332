li=list(map(int,input().split()))
k=int(input())
n=len(li)
c=0
for i in range(n):
    if li[i]!=1 and li[i]>k:
        c+=min(li[i]%k,k-li[i]%k)
    else:
        c+=k-li[i]
print(c)
