import sys, heapq

def main():
	INF = 2147483647
	v, e = map(int, sys.stdin.readline().split())
	k = int(sys.stdin.readline())
	edges = [[] for _ in range(v+1)]
	dist = [INF for _ in range(v+1)]
	dist[k] = 0
	for _ in range(e):
		x, y, w = map(int, sys.stdin.readline().split())
		edges[x].append([y, w])

	heap = [[0, k]]
	while(heap):
		val, curr = heapq.heappop(heap)
		for adj, weight in edges[curr]:
			if (dist[curr] + weight < dist[adj]):
				dist[adj] = dist[curr] + weight
				heapq.heappush(heap, [dist[adj], adj])

	for el in dist[1:]:
		if el == INF:
			print("INF")
		else:
			print(el)

if __name__ == "__main__":
	main()
