import sys

t = int(sys.stdin.readline())
for _ in range(t):
	arr = list(map(int, sys.stdin.readline().split()))
	n = arr[0]
	ave = sum(arr[1:])/n
	arr = sorted(arr[1:], reverse=True)
	for i in range(0, len(arr)):
		if(arr[i] <= ave):
			ans = round((i*100.0)/n, 3)
			print("{:.3f}%".format(ans))
			break

