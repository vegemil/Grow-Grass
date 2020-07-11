from collections import deque

def main():
	n, k = map(int, input().split())
	# cnt, curr
	dp = [[-1, -1] for _ in range(100001)]
	dp[n] = [0, n]
	visit = deque([(n, 0)])
	cnt = 1

	while(visit):
		curr, cnt = visit.popleft()
		if curr == k:
			break
		if curr > 0 and dp[curr-1][0] < 0:
			dp[curr-1] = [cnt+1, curr]
			visit.append((curr-1, cnt+1))
		if curr < 100000 and dp[curr+1][0] < 0:
			dp[curr+1] = [cnt+1, curr]
			visit.append((curr+1, cnt+1))
		if curr <= 50000 and dp[curr*2][0] < 0:
			dp[curr*2] = [cnt+1, curr]
			visit.append((curr*2, cnt+1))

	print(dp[k][0])

	res = deque([])
	curr = k
	while(curr != dp[curr][1]):
		res.append(curr)
		curr = dp[curr][1]
	res.append(n)

	while(res):
		print(res.pop(), end=" ")
	print("")


if __name__ == "__main__":
	main()
