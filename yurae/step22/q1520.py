import sys

def main():
	m, n = map(int, sys.stdin.readline().split())
	arr = []
	vals = []
	for i in range(m):
		line = list(map(int, sys.stdin.readline().split()))
		vals.append(line)
		for j in range(n):
			arr.append([line[j], i, j])

	arr = sorted(arr, key=lambda k:k[0], reverse=True)

	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[0][0] = 1
	for el in arr:
		i, j = el[1], el[2]
		if (i>0 and vals[i-1][j] > vals[i][j]):
			dp[i][j] += dp[i-1][j]
		if (j>0 and vals[i][j-1] > vals[i][j]):
			dp[i][j] += dp[i][j-1]
		if (i<m-1 and vals[i+1][j] > vals[i][j]):
			dp[i][j] += dp[i+1][j]
		if (j<n-1 and vals[i][j+1] > vals[i][j]):
			dp[i][j] += dp[i][j+1]

	print(dp[m-1][n-1])


if __name__ == "__main__":
	main()
