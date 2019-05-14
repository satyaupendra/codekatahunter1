n=input()
for i in range(len(n)):
    t=0
    if(n[i]==" "):
        if(n[i+1]==n[i+1].upper()):
            t=1
if(t==1):
    print('yes')
else:
    print('no')
        
