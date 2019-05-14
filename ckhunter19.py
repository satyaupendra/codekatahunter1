n,l=map(int,input().split())
k=[]
for i in range(n):
	s=set(map(int,input().split()))
	k.append(s)
t=s.intersection(*k)
print(*t)
