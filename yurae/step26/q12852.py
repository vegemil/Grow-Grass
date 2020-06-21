import sys

sys.setrecursionlimit(1000000)
res = [2147483647, []]

def dfs(curr, dp, arr):
	cnt = dp[curr]
	global res
	if (curr == 1 and res[0] > cnt):
		res = [cnt, arr+[]]
	if (curr%3 == 0 and dp[curr//3] > cnt+1):
		dp[curr//3] = cnt+1
		arr.append(curr//3)
		dfs(curr//3, dp, arr)
	if (curr%2 == 0 and dp[curr//2] > cnt+1):
		dp[curr//2] = cnt+1
		arr.append(curr//2)
		dfs(curr//2, dp, arr)
	if (curr-1 > 0 and dp[curr-1] > cnt+1):
		dp[curr-1] = cnt+1
		arr.append(curr-1)
		dfs(curr-1, dp, arr)
	arr.pop()
		

n = int(sys.stdin.readline())
dp = [2147483647 for _ in range(1000001)]
arr = [n]
dp[n] = 0
dfs(n, dp, arr)
print(dp[1])
for el in res[1]:
	print(el, end=" ")
print("")
