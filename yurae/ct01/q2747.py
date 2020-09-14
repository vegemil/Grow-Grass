n = int(input())

a = 0
b = 1
res = 0

for i in range(n):
	a, b = b, a+b
	res = a

print(res)
