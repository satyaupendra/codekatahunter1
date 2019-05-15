n=input()
l=list(n)
s=0
for i in range(0,len(l)):
  k=pow(int(l[i]),i)
  s=s+k
print(s)
