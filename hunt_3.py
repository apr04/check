a=int(input())
b=input().split()
s=[]
for i in range(a):
	if(int(b[i])==i):
		s.append(b[i])
s.sort()
if(len(s)==0):
	print("-1")
else:
	for i in range(0,len(s)):
		if(i<len(s)-1):
			print(s[i],end=" ")
		else:
			print(s[i])
