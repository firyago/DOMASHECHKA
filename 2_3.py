n=int(input())
a=[1]
print(*a)
for i in range(n):
	a=[0]+a+[0]
	b=[]
	for i in range(len(a)-1):
		b.append(a[i]+a[i+1])
	a=b
	print(*a)
