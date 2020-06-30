n=int(input())
s=input()
li=[]
for i in range(n):
    for j in range(i+1,n+1):
        t=s[i:j]
        if t==t[::-1]:
            li.append(t)
a=max(li,key=len)
print(len(a))
print(a)
