t=int(input())
for _ in range(t):
    n=int(input())
    al,bl=[],[]
    for i in range(n):
        a,b=map(int,input().split())
        al.append(a)
        bl.append(b)
    ans=max(max(al)-min(al),max(bl)-min(bl))
    print(ans*ans)
