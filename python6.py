PI="314159265358979323846264338327"
n=int(input())
for i in range(n):
    no=input()
    count=0
    for i in range(len(no)):
        if no[i]==PI[i]:
            count+=1
        else:
            break
    print(count)
