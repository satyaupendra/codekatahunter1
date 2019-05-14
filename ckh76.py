n = int(input())
l,sum = [],0
for i in range(0,n):
  l.append(list(map(int,input().split())))
for i in range(0,n):
  for j in range(0,n):
    sum = sum+l[i][j]
r = sum / n**2
print('%.6f' %r)
