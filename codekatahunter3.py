n=int(input())
s=[]
l=list(map(int,input().split()))
for i in range(n):
    if(i==l[i]):
        s.append(l[i])
s.sort()
if(len(s)==0):
    print("-1")
else:
    print(" ".join(map(str,s)))
