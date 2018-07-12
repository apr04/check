a=int(input())
b=input().split()
s=0
for i in range(a):
	if(b.count(b[i])>1):
		s=b[i]
		break
if(s==0):
	print("unique")
else:
	print(s)
