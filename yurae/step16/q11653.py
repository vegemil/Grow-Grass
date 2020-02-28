n = int(input())
arr = []
div = 2
while(n > 1):
	if (n % div == 0):
		arr.append(div)
		n /= div
	else:
		div += 1

arr.sort()
for el in arr:
	print(el)
