n1=str(raw_input())
l=[]
b=['d','h','o','n','i']
b.sort()
for i in n1:
    l.append(i)
l.sort()
if(b==l):
    print("yes")
else:
    print("no")
