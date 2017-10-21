def arithmetic(a,b,s):
	if s=='+': return a+b
	elif s=='-': return a-b
	elif s=='*': return a*b
	elif (s=='/') and (b!=0): return a/b
	else: return 'Неизвестная операция'
	
a,b,s= input().split()
a=int(a)
b=int(b)
x=arithmetic(a,b,s)
print(x)
