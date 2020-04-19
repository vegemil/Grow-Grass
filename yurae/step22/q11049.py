import sys

# works in pypy3
def main():
	INF = 2147483647
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	dp = [[INF for _ in range(n)] for _ in range(n)]

	dp[0][0] = 0
	for i in range(1, n):
		dp[i][i] = 0
		dp[i-1][i] = arr[i-1][0]*arr[i-1][1]*arr[i][1]
		dp[i][i-1] = arr[i-1][0]*arr[i-1][1]*arr[i][1]

	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			for k in range(i, j):
				curr = dp[i][k] + dp[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1]
				dp[i][j] = min(dp[i][j], curr)

	print(dp[0][n-1])


if __name__ == "__main__":
	main()
