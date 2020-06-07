import sys


def tsp(dp, arr, idx, visit):
	INF = 2147483647
	if visit >= ((1<<len(arr))-1):
		return arr[idx][0] if arr[idx][0] > 0 else INF
	if dp[idx][visit] > 0:
		return dp[idx][visit]

	curr = INF
	for i in range(1, len(arr)):
		if (visit>>i)%2 == 1 or arr[idx][i] == 0:
			continue
		curr = min(curr, arr[idx][i] + tsp(dp, arr, i, visit | (1<<i)))
	dp[idx][visit] = curr
	return curr


def main():
	INF = 2147483647
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	dp = [[0 for _ in range(1<<n)] for _ in range(n)]
	print(tsp(dp, arr, 0, 1))


if __name__ == "__main__":
	main()
