n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if((l[i]<l[j]) and (l[j]<l[k]) and (l[i]<l[k]) and (i<j)and(j<k)and(i<k)):
                c=c+1
print(c)
