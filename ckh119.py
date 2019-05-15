n=int(input())
k=list(map(int,input().split()))
t=0
for i in range(n):
    for j in range(i+1,n):
            if(k[i]<k[j]):
                t=t+1
print(t)
