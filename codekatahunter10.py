n,m=list(map(int,input().split()))
nl=list(map(str,input().split()))
ml=list(map(str,input().split()))
if(all(i in nl for i in ml )):
    print("Yes")
else:
    print("No")