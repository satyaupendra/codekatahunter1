n=int(input())
r=[]
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if((l[i]==l[j]) and l[i] not in r):
            r.append(l[i])
r.sort()
print(" ".join(map(str,r)))