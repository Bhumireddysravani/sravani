t1=list(map(int,input().split(" ")))
t2=list(map(int,input().split(" ")))
for i in range(0,2):
    if t1[i]>t2[i]:
        res=t1[i]-t2[i]
    else:
        res=t2[i]-t1[i]
    if i==1:
        print(res)
        break
    print(res,end=" ")
