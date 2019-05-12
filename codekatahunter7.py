n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
m=[]
for i in range(n):
    if(l[i]%2==0 and i%2!=0):
        print(l[i],end=" ")
    elif(l[i]%2!=0 and i%2==0):
        print(l[i],end=" ")
