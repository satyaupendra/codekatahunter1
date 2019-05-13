n1,n2=input().split(" ")
n1=int(n1)
n2=int(n2)
r=0
while(n1>=n2):
    n1=n1-n2
    r=r+1
print(r)
