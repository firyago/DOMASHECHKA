def fact(x):
	p=1
	for i in range(2,x+1):
		p*=i
	return p

x=int(input())
print(fact(x))

