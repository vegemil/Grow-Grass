import sys

def mark_nth(n, arr):
	if (arr[n][0] > -1):
		return

	if (n >= 1 and arr[n-1][0] == -1):
		mark_nth(n-1, arr)
	if (n >= 2 and arr[n-2][0] == -1):
		mark_nth(n-2, arr)
	arr[n][0] = arr[n-1][0] + arr[n-2][0]
	arr[n][1] = arr[n-1][1] + arr[n-2][1]

t = int(sys.stdin.readline())
# zeros, ones
arr = [[-1, -1] for _ in range(41)]
arr[0] = [1, 0]
arr[1] = [0, 1]
for _ in range(t):
	n = int(sys.stdin.readline())
	mark_nth(n, arr)
	print(arr[n][0], arr[n][1])
