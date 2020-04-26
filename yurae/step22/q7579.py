import sys

def main():
	n, m = map(int, sys.stdin.readline().split())
	vals = list(map(int, sys.stdin.readline().split()))
	cost = list(map(int, sys.stdin.readline().split()))

	if (m == 0):
		print(0)
		return

	cost_sum = sum(cost)
	res = cost_sum
	dp = [[0 for _ in range(cost_sum+1)] for _ in range(n)]

	for i in range(0, n):
		for j in range(0, cost_sum+1):
			if j < cost[i]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(vals[i] + dp[i-1][j-cost[i]], dp[i-1][j])

			if (dp[i][j] >= m):
				res = min(res, j)

	print(res)
			

if __name__ == "__main__":
	main()
