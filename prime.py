num = int(input())
for s in range(2, int(num/2)):
	if num % s == 0:
		print("no")
		break
else:
	     print("yes")
