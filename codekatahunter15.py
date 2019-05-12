n=int(input())
l=list(map(int,input().split( )))
superstar=max(l)
s=[]
for i in range(0,n-1):
	temp=0
	for j in range(i+1,n):
		
		if l[i]>l[j]:
			temp=temp+1
	if temp==(n-1-i):
		s.append(l[i])
s.append(l[n-1])		
print(*s)
print(superstar)


