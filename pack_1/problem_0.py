a=list(input().split())
b=[]
if a!=[]:
    b=[a[len(a)-1]]+a[:len(a)-1:]
print(*b)

