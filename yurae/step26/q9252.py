import sys

def main():
	in1 = sys.stdin.readline().split()[0]
	in2 = sys.stdin.readline().split()[0]

	dp = [["" for _ in range(1001)] for _ in range(1001)]

	for i in range(len(in1)):
		for j in range(len(in2)):
			if in1[i]==in2[j]:
				dp[i][j] = in1[i] if i==0 or j==0 else dp[i-1][j-1]+in1[i]
			else:
				if i==0:
					dp[i][j] = "" if j==0 else dp[i][j-1]
				elif j==0:
					dp[i][j] = dp[i-1][j]
				else:
					if (len(dp[i-1][j]) > len(dp[i][j-1])):
						dp[i][j] = dp[i-1][j]
					else:
						dp[i][j] = dp[i][j-1]

	print(len(dp[i][j]))
	print(dp[i][j])
				

if __name__ == "__main__":
	main()
