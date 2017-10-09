a=list(map(int, input().split()))
b=[a[len(a)-1]]+a[:len(a)-1:]
print(*b)

