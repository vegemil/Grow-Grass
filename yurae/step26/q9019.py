import sys
from collections import deque

# works with pypy3
def main():
	for _ in range(int(sys.stdin.readline())):
		a, b = map(int, sys.stdin.readline().split())
		# D=1, S=2, L=3, R=4
		dslr = ["", "D", "S", "L", "R"]

		# dslr, before
		dp = [[-1, -1] for _ in range(10000)]
		dp[a] = [0, a]
		visit = deque([])
		visit.append(a)
		while(visit):
			curr = visit.popleft()
			if (curr == b):
				break

			nxt = (curr*2)%10000
			if (dp[nxt][0] < 0):
				dp[nxt] = [1, curr]
				visit.append(nxt)
			nxt = (curr+9999)%10000
			if (dp[nxt][0] < 0):
				dp[nxt] = [2, curr]
				visit.append(nxt)
			nxt = (curr%1000)*10+curr//1000
			if (dp[nxt][0] < 0):
				dp[nxt] = [3, curr]
				visit.append(nxt)
			nxt = (curr%10)*1000+curr//10
			if (dp[nxt][0] < 0):
				dp[nxt] = [4, curr]
				visit.append(nxt)

		curr = b
		res = ""
		while(dp[curr][1] != curr):
			res = dslr[dp[curr][0]] + res
			curr = dp[curr][1]

		print(res)


if __name__ == "__main__":
	main()
