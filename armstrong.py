num=int(input())
sum=0
temp=num
while temp>0:
	digital=temp%10
	sum=digital**3
	temp//=10
if num==sum:
            print("yes")
else:
             print("no")
