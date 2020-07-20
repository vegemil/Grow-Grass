import sys
from collections import deque

sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
edges = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
parent[1] = 1

for _ in range(n-1):
	x, y = map(int, sys.stdin.readline().split())
	edges[x].append(y)
	edges[y].append(x)

deq = deque([1])
while(deq):
	curr = deq.popleft()
	for adj in edges[curr]:
		if (parent[adj] < 0):
			parent[adj] = curr
			deq.append(adj)

for i in range(2, n+1):
	print(parent[i])
