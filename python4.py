def dig_sum(n):
    sum=0
    while n!=0:
        sum=sum+n%10
        n=n//10
    return sum
no=int(input())
for i in range(no):
    n,q=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(q):
        L=list(map(int,input().split()))
        if L[0]==2:
            print(l[L[1]-1])
        elif L[0]==1:
            for j in range(L[1]-1,L[2]):
                l[j]=dig_sum(l[j])
