import sys, math

# works in pypy3
def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))
	k = int(sys.stdin.readline())

	dp = [[0]*k for _ in range(1<<n)]
	dp[0][0] = 1
	mods = [[(j*10**len(str(arr[i]))+arr[i])%k for j in range(k)] for i in range(n)]

	for i in range(1<<n):
		for j in range(n):
			if (i&(1<<j)):
				continue
			for l in range(k):
				dp[i|(1<<j)][mods[j][l]] += dp[i][l]
	
	num = dp[-1][0]
	den = sum(dp[-1])
	res_gcd = math.gcd(den, num)
	print(num//res_gcd, end="")
	print("/", end="")
	print(den//res_gcd)


if __name__ == "__main__":
	main()
