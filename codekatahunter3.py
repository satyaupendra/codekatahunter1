n=int(input())
r=[]
l=list(map(int,input().split()))
for i in range(n):
    if(i==l[i]):
        r.append(l[i])
r.sort()
if(len(r)==0):
    print("-1")
else:
    print(" ".join(map(str,r)))