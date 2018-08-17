n=int(input())
s=list(map(int,input().split(" ")))
s.sort()
for i in range(len(s)):
    if i==len(s)-1:
        print(s[i])
        break 
    print(s[i],end=" ")

