import sys


# 결국 실패해서 C++로 다시 짜서 냈습니다
# python3으로 시간초과가 나지 않으려면 knuth optimization을 사용해야 할 것 같습니다
def main():
	t = int(sys.stdin.readline())
	for _ in range(t):
		cnt = int(sys.stdin.readline())
		arr = list(map(int, sys.stdin.readline().split()))
		dp = [[100000000 for _ in range(cnt)] for _ in range(cnt)]

		dp[0][0] = arr[0]
		for i in range(1, cnt):
			dp[i][i] = 0
			dp[i-1][i] = arr[i-1] + arr[i]
			dp[i][i-1] = arr[i-1] + arr[i]

		for i in range(cnt-1, -1, -1):
			for j in range(i+1, cnt):
				for k in range(i, j):
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum(arr[i:j+1]))
		print(dp[0][cnt-1])	


if __name__ == "__main__":
	main()
