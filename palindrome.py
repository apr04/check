a=raw_input()
n=len(a)/2
m=len(a)
c=0
for i in range(0,n):
	if(a[i]!=a[m-1]):
		c=c+1
	m=m-1
if(c==0):
	print("yes")
else:
	print("no")
