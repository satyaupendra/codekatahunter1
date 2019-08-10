n=int(input())
l=[]
for i in range(n):
    l=l+list(map(int,input().split()))
l.sort()
print(*l)
