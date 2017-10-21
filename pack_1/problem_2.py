def del(x):
	a=[]
	for i in range(2, x + 1):
		if x % i == 0: a.append(i)
	return a

x=int(input())
print(*del(x))
	
