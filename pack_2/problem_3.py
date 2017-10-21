n=int(input())
c=[]
a=[1]
for i in range(n+1):
	s=''
	for j in range(len(a)):
		s+=str(a[j])+' '
	c.append(s)
	a=[0]+a+[0]
	b=[]
	for i in range(len(a)-1):
		b.append(a[i]+a[i+1])
	a=b
	for j in range(i):
		c[j]=' '+c[j]
for x in c:
	print(x)
