r,b=map(int,input().split())
def score(l):
    con=alt=0
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            con+=1
        else:
            alt+=1
    return con,alt
def one(r,b):
    l=[]
    for i in range(r+b):
        if i%2==0:
            if r==0:
                l.append(1)
                b=b-1
            elif b==0:
                l.append(0)
                r=r-1
            elif len(l)>=1:
                if l[-1]==1:
                    l.append(1)
                    b=b-1
                elif l[-1]==0:
                    l.append(0)
                    r=r-1
            elif len(l)==0:
                    l.append(1)
                    b=b-1

        else:
            if r==0:
                l.append(1)
                b=b-1
            elif b==0:
                l.append(0)
                r=r-1
            elif l[-1]==1:
                l.append(0)
                r=r-1
            elif l[-1]==0:
                l.append(1)
                b=b-1
        #print(r,b,l)
    return score(l)
def zero(r,b):
    l=[]
    for i in range(r+b):
        if i%2==0:
            if r==0:
                l.append(1)
                b=b-1
            elif b==0:
                l.append(0)
                r=r-1
            elif len(l)>=1:
                if l[-1]==1:
                    l.append(1)
                    b=b-1
                elif l[-1]==0:
                    l.append(0)
                    r=r-1
            elif len(l)==0:
                    l.append(0)
                    r=r-1

        else:
            if r==0:
                l.append(1)
                b=b-1
            elif b==0:
                l.append(0)
                r=r-1
            elif l[-1]==1:
                l.append(0)
                r=r-1
            elif l[-1]==0:
                l.append(1)
                b=b-1
        #print(r,b,l)
    return score(l)
r1,b1=one(r,b)
r2,b2=zero(r,b)
if r2>r1:
    print(r2,b2)
else:
    print(r1,b1)
