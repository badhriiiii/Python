def check(l):
    uni=[]
    for i in l:
        if i not in uni:
            uni.append(i)
    if len(uni)==1:
        return 1
    else:
        return -1
def seq(n,su):
    L=[1,2,3,4,5,6]
    l=[1 for i in range(n)]
    i=1
    while sum(l)!=su:
        del l[0]
        l.append(i)
        if check(l)==1:
            i+=1
    return l
n=int(input())
for i in range(n):
    n,s,r=map(int,input().split())
    a=s-r
    l=seq(n-1,r)
    for i in l:
        print(i,end=" ")
    print(a,end=" ")
