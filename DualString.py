t=int(input())
for _ in range(t):
    string=input()
    if len(set(string)) != len(string):
        print("Yes")
    else:
        print("No")
