import sys

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())
arr = []
dp = [[[-1, -1] for _ in range(w+1)] for _ in range(w+1)]

def dist(a, b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])


def process(a, b):
	global w
	curr = max(a, b)
	if (curr >= w+1):
		return 0
	if (dp[a][b][0] > 0):
		return dp[a][b][0]
	d1 = process(curr+1, b) + dist(arr[a], arr[curr+1])
	d2 = process(a, curr+1) + dist(arr[b], arr[curr+1])
	dp[a][b][0] = min(d1, d2)
	dp[a][b][1] = 1 if d1 <= d2 else 2
	return dp[a][b][0]


def pick(a, b):
	global w
	curr = max(a, b)
	if (curr >= w+1):
		return
	d1 = process(curr+1, b) + dist(arr[a], arr[curr+1])
	d2 = process(a, curr+1) + dist(arr[b], arr[curr+1])
	if (d1<d2):
		print(1)
		pick(curr+1, b)
	else:
		print(2)
		pick(a, curr+1)


def main():
	global n
	arr.append([1, 1])
	arr.append([n, n])
	for _ in range(w):
		arr.append(list(map(int, sys.stdin.readline().split())))

	dp[0][0] = [0, -1]
	res = process(0, 1)
	print(res)
	pick(0, 1)


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
