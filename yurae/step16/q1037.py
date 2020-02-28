n = int(input())
arr = sorted(list(map(int, input().split())))
if (n == 0):
	print(1)
else:
	print(arr[0]*arr[-1])
