a, b, c = map(int, input().split())

def func(a, b, c):
	if (b < 100):
		return (a**b)%c
	else:
		div = func(a, b//2, c)
		if (b%2 == 0):
			return (div*div)%c
		else:
			return (div*div*a)%c

print(func(a, b, c))
