import sys, heapq

def main():
	INF = 2147483647
	n = int(sys.stdin.readline())
	m = int(sys.stdin.readline())
	edges = [[] for _ in range(n+1)]
	dist = [INF for _ in range(n+1)]
	for _ in range(m):
		x, y, z = map(int, sys.stdin.readline().split())
		edges[x].append((y, z))

	start, end = map(int, sys.stdin.readline().split())
	dist[start] = 0
	back_edges = [-1 for _ in range(n+1)]
	back_edges[start] = start
	
	heap = [(0, start)]
	while(heap):
		val, curr = heapq.heappop(heap)
		if curr == end:
			break
		for adj, w in edges[curr]:
			if (dist[adj] > val + w):
				dist[adj] = val + w
				heapq.heappush(heap, (dist[adj], adj))
				back_edges[adj] = curr

	res = []
	curr = end
	while(True):
		res.append(curr)
		if (curr == back_edges[curr]):
			break
		curr = back_edges[curr]

	print(dist[end])
	print(len(res))
	while(res):
		print(res.pop(), end=" ")
	print("")


if __name__ == "__main__":
	main()
