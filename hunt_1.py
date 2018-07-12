a=int(input())
b=input().split()
for i in range(a):
	b[i]=int(b[i])
s=[]
for i in range(0,len(b)):
	if(b.count(b[i])>1):
		s.append(b[i])
if(len(s)==0):
	print("unique")
else:
	a=set(s)
	a=list(a)
	for i in range(0,len(a)):
		if(i<len(a)-1):
			print(a[i],end=" ")
		else:
			print(a[i])
