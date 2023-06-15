n=int(input())
for i in range(n):
    no=int(input())
    L=[]
    for i in range(no):
        l=list(map(int,input().split()))
        L.append(l)
    i=0
    l_new=[]
    for i in range(no):
        l_new.append(L[i][0])
    first=max(l_new,key=l_new.count)
    actual=[]
    actual.append(first)
    for i in range(no):
        if l_new[i]!=first:
            actual=actual+L[i]
    for i in actual:
        print(i,end=" ")
