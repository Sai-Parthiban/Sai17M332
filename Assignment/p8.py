for t in range(int(input())):
    a=input().upper()
    b=input().upper()
s=""
for i in a:
    if i not in b:
        s+=i
print(s)
