n=int(input())
r1=[]
t=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if((l[i]==l[j]) and l[i] not in r1):
            r1.append(l[i])
            t=1
r1.sort()
print(" ".join(map(str,r1)))
if(t==0):
    print('unique')
