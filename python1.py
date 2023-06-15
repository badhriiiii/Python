l=[]
for i in range(5):
    a,b,c,d,e=map(int,input().split())
    l.append([a,b,c,d,e])
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            if i>2:
                if j>2:
                    print(i-2+j-2)
                    break
                else:
                    print(i-2+2-j)
                    break
            else:
                if j>2:
                    print(2-i+j-2)
                    break
                else:
                    print(2-i+2-j)
                    break
