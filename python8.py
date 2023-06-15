n=input()
new=''
n=n.lower()
for i in n:
    if ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85 or  ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117:
        new=new
    elif (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        new=new+'.'+i
    else:
        new=new+i
print(new)
