n=raw_input()
l=list(n)
s=0
for i in range(0,len(l)):
     s=s+(int(l[i])**i)
print(s)
