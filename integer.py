s,z=input().split()
s,z=int(s),int(z)
a=""
for i in range(s+1,z):
        if(i%2==0):
            if i<z-2:
                a=""
            else:a=""
            print(i,end=a)
