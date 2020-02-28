a, b = map(int, input().split())
x, y = a, b
if (x < y):
	x, y = y, x
while(x%y != 0):
	x, y = y, x%y

print(y)
print((a*b)//y)

