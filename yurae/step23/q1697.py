import sys
from collections import deque

def main():
	n, k = map(int, sys.stdin.readline().split())
	deq = deque([n])
	visit = [-1 for _ in range(100001)]
	visit[n] = 0
	while(deq):
		curr = deq.popleft()
		if curr == k:
			print(visit[curr])
			return
		cnt = visit[curr]
		if curr > 0 and visit[curr-1] < 0:
			visit[curr-1] = cnt+1
			deq.append(curr-1)
		if curr < 100000 and visit[curr+1] < 0:
			visit[curr+1] = cnt+1
			deq.append(curr+1)
		if curr < 50001 and visit[curr*2] < 0:
			visit[curr*2] = cnt+1
			deq.append(curr*2)


if __name__ == "__main__":
	main()
