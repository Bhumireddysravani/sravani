s,r=map(int,raw_input().split())
for i in range(s+1,r):
    if(i>1):
            for k in range(2,i):
                   if(i%k==0):
                           break
            else:
                     print i,
