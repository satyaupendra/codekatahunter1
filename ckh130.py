n=int(input())
s=0
k=[]
l=[]
for i in range(2,n+1):
    for j in range(2,n):
        if(i%j==0):
            k.append(i)
        elif(i%10==3):
            s=s+i
            break
print(s)
        
