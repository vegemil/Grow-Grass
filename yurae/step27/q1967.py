import sys
from collections import deque

def main():
	v = int(sys.stdin.readline())
	edges = [[] for _ in range(v+1)]
	for _ in range(v-1):
		x, y, z = map(int, sys.stdin.readline().split())
		edges[x].append((y, z))
		edges[y].append((x, z))

	visit = [[-1, i] for i in range(v+1)]
	visit[1] = [0, 1]
	deq = deque([(0, 1)])
	while(deq):
		dist, curr = deq.popleft()
		for adj, e in edges[curr]:
			if visit[adj][0] >= 0:
				continue
			visit[adj][0] = dist + e
			deq.append((dist+e, adj))

	start = max(visit)[1]

	visit = [[-1, i] for i in range(v+1)]
	visit[start] = [0, start]
	deq = deque([(0, start)])
	while(deq):
		dist, curr = deq.popleft()
		for adj, e in edges[curr]:
			if visit[adj][0] >= 0:
				continue
			visit[adj][0] = dist + e
			deq.append((dist+e, adj))

	print(max(visit)[0])



if __name__ == "__main__":
	main()
