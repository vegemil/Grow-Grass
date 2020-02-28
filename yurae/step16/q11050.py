n, k = map(int, input().split())
ans = 1
for i in range(k):
	ans *= (n-i)
for i in range(k):
	ans //= (i+1)

print(int(ans))
