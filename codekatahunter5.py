n=int(input())
l=list(map(int,input().split()))
r=[]
t=0
for ele in l:
    if ele not in r:
        r.append(ele)
    else:
        print(ele)
        t=t+1
        break
if t==0:
    print("Unique")