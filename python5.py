n,m=map(int,input().split())
l = list(map(int,input().strip().split()))[:m]
L=[x for x in range(1,n+1)]
cost=0
ind=1
for i in l:
    if ind<i:
        cost=cost + (i-ind)
        ind=i
    elif ind>i:
        cost=cost+ (n-ind) + (i)
        ind=i
print(cost)
