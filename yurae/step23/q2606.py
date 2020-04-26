import sys
from collections import deque

cnt = 0

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = [[[], False] for _ in range(n+1)]
for _ in range(m):
	v, w = map(int, sys.stdin.readline().split())
	edges[v][0].append(w)
	edges[w][0].append(v)

edges[1][1] = True
deque = deque([1])
while deque:
	curr = deque.popleft()
	for adj in edges[curr][0]:
		if edges[adj][1] == True:
			continue
		deque.append(adj)
		edges[adj][1] = True
		cnt += 1


print(cnt)
