r,c=map(int,input().split())
li=[]
for i in range(r):
    st=""
    s=str(list(map(int,input().split())))
    for i in s:
        if i=="0" or i=="1":
            st+=i
    li.append(st)
l=set(li)
for i in li:
    if i in l:
        print(" ".join(i))
        l.remove(i)
