n=int(input())
li=[]
for _ in range(n):
    k=""
    s=input()
    for i in s:
        if i.isalpha() or i==" ":
            k+=i
    li.append(k.split())
for i in l[::-1]:
    for j in i[::-1]:
        print(j,end=" ")
    print()
