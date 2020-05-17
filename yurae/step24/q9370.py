import sys, heapq

def dijkstra(edges, start):	
	INF = 2147483647
	dist = [INF for _ in range(len(edges))]
	dist[start] = 0
	heap = [[0, start]]
	while(heap):
		val, curr = heapq.heappop(heap)
		for adj, weight in edges[curr]:
			if (dist[curr] + weight < dist[adj]):
				dist[adj] = dist[curr] + weight
				heapq.heappush(heap, [dist[adj], adj])
	return dist


def main():
	INF = 2147483647
	for _ in range(int(sys.stdin.readline())):
		n, m, t = map(int, sys.stdin.readline().split())
		s, g, h = map(int, sys.stdin.readline().split())
		edges = [[] for _ in range(n+1)]
		edge_gh = INF
		for _ in range(m):
			x, y, w = map(int, sys.stdin.readline().split())
			edges[x].append([y, w])
			edges[y].append([x, w])
			if ((g==x and h==y) or (h==x and g==y)):
				edge_gh = w
		dests = []
		for _ in range(t):
			dests.append(int(sys.stdin.readline()))

		d_s = dijkstra(edges, s) 
		d_h = dijkstra(edges, h) 
		d_g = dijkstra(edges, g)

		res = []
		for dest in dests:
			dist1 = d_s[g] + edge_gh + d_h[dest]
			dist2 = d_s[h] + edge_gh + d_g[dest]
			if (min([dist1, dist2]) <= d_s[dest]):
				res.append(dest)

		res.sort()
		for el in res:
			print(el, end=" ")
		print("")


if __name__ == "__main__":
	main()
