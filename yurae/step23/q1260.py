import sys
from collections import deque

def dfs_(curr, edges, dfs):
	dfs.append(curr)
	edges[curr][1] = True
	for adj in edges[curr][0]:
		if edges[adj][1] == True:
			continue
		dfs_(adj, edges, dfs)


def bfs_(start, edges, bfs):
	deq = deque([start])
	edges[start][1] = True
	bfs.append(start)
	while(deq):
		curr = deq.popleft()
		for adj in edges[curr][0]:
			if edges[adj][1] == True:
				continue
			edges[adj][1] = True
			deq.append(adj)
			bfs.append(adj)


n, m, v = map(int, sys.stdin.readline().split())
edges = [[[], False] for _ in range(n+1)]
for _ in range(m):
	x, y = map(int, sys.stdin.readline().split())
	edges[x][0].append(y)
	edges[y][0].append(x)

for el in edges:
	el[0] = sorted(el[0])

# dfs
dfs = []
dfs_(v, edges, dfs)

for el in edges:
	el[1] = False

#bfs
bfs = []
bfs_(v, edges, bfs)

for el in dfs:
	print(el, end=" ")
print("")

for el in bfs:
	print(el, end=" ")
print("")


