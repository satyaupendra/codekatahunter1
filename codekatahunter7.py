n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
m=[]
for i in range(n):
    if(l[i]%2==0 and i%2!=0):
        even.append(l[i])
    elif(l[i]%2!=0 and i%2==0):
        odd.append(l[i])
m=even+odd
print(*m,sep=" ")