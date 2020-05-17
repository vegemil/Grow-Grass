import sys, heapq


def dijkstra(edges, start, end):	
	INF = 2147483647
	dist = [INF for _ in range(len(edges))]
	dist[start] = 0
	heap = [[0, start]]
	while(heap):
		val, curr = heapq.heappop(heap)
		if (curr == end):
			return val
		for adj, weight in edges[curr]:
			if (dist[curr] + weight < dist[adj]):
				dist[adj] = dist[curr] + weight
				heapq.heappush(heap, [dist[adj], adj])
	return dist[end]


def main():
	INF = 2147483647
	n, e = map(int, sys.stdin.readline().split())
	edges = [[] for _ in range(n+1)]
	for _ in range(e):
		x, y, w = map(int, sys.stdin.readline().split())
		edges[x].append([y, w])
		edges[y].append([x, w])
	v1, v2 = map(int, sys.stdin.readline().split())

	dist = [INF for _ in range(n+1)]
	dist[1] = 0
	heap = [[0, 1]]
	while(heap):
		val, curr = heapq.heappop(heap)
		for adj, weight in edges[curr]:
			if (dist[curr] + weight < dist[adj]):
				dist[adj] = dist[curr] + weight
				heapq.heappush(heap, [dist[adj], adj])

	dist1, dist2 = dist[v1], dist[v2]
	dist1 += (dijkstra(edges, v1, v2) + dijkstra(edges, v2, n))
	dist2 += (dijkstra(edges, v2, v1) + dijkstra(edges, v1, n))

	res = min([dist1, dist2])
	if (res < INF):
		print(res)
	else:
		print(-1)


if __name__ == "__main__":
	main()
