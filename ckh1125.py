n=input()
l=[]
for i in n:
    t=n.count(i)
    if t==1:
        l.append(i)
s=""
for i in l:
    s=s+i
print(s)
