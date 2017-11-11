class TExchange:
	def __init__(self):
		self.time=0.0
		self.size=0
		self.name=''

with open('TRD2.csv') as f:	
	d=f.readlines()
	d=d[1::]
	a=[]
	b=[]
	for x in d:
		x1,x2,x3,x4=x.split(',')
		p=list(x1.split(':'))
		rec=TExchange()
		rec.time=float(p[-1])
		rec.size=int(x3)
		rec.name=x4
		a.append(rec)
		if x4 not in b: b.append(x4)

	for x in b:
		s=0.0
		k=0
		c=[]
		st=''
		d=[]
		for i in range(len(a)):
			if a[i].name==x:
				if st=='': st=a[i].time
				if s+a[i].time<1: 
					s+=a[i].time
					k+=1
				if s>=1:
					c.append(k)
					d.append(st)
					s=0
					k=0
					st=''
		if c!=[]:
			print(x,max(c),d[c.index(max(c))])
		else:
			print(x,k,st)

						
