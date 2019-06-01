s1,s2=list(map(str,input().split()))
t=len(s1)
for i in range(0,t-1):
  if s1[i:i+2] in s2:
    print("yes")
else:
    print("no")
