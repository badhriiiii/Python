n=int(input())
for i in range(n):
    l=int(input())
    dire=input()
    cond=0
    x=y=0
    for i in dire:
        if i=="U":
            y+=1
        elif i=="D":
            y-=1
        elif i=="L":
            x-=1
        elif i=="R":
            x+=1
        if x==y==1:
            print("YES")
            cond=1
            break
    if cond==0:
        print("NO")
