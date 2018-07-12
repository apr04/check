a=int(input())
b=input().split()
s=[]
for i in range(a):
	b[i]=int(b[i])
for i in range(a):
	if(i%2==0 and b[i]%2!=0):
		s.append(b[i])
	elif(i%2!=0 and b[i]%2==0):
		s.append(b[i])
for i in range(0,len(s)):
	if(i<len(s)-1):
		print(s[i],end=" ")
	else:
		print(s[i])
