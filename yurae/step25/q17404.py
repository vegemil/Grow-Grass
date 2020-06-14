import sys

def main():
	INF = 2147483647
	n = int(sys.stdin.readline())
	arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

	dp = [[INF for _ in range(3)] for _ in range(n)]
	res = INF

	for i in range(3):
		for j in range(3):
			if (i == j):
				dp[0][j] = arr[0][j]
			else:
				dp[0][j] = INF
		
		for j in range(1, n):
			dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
			dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
			dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]

		for j in range(3):
			if (i == j):
				continue
			res = min(res, dp[-1][j])

	print(res)

if __name__ == "__main__":
	main()
