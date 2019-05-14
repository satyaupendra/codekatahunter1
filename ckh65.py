n,k=list(map(int,input().split(" ")))
l=[int(n) for n in input().split()]
while k in l:
	l.remove(k)
if l==[]:
	print("empty")
else:
	print(*l)
