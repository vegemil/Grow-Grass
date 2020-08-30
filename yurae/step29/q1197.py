import sys, heapq

def main():
	v, e = map(int, sys.stdin.readline().split())
	edges = [[] for _ in range(v+1)]
	for _ in range(e):
		a, b, c = map(int, sys.stdin.readline().split())
		edges[a].append((c, b))
		edges[b].append((c, a))

	visited = [False for _ in range(v+1)]
	visited[1] = True
	curr = 1
	res = 0
	heap = []
	for el in edges[1]:
		heapq.heappush(heap, el)
	
	while(heap):
		dist, adj = heapq.heappop(heap)
		if visited[adj] == True:
			continue
		visited[adj] = True	
		res += dist
		for c, b in edges[adj]:
			if visited[b] == True:
				continue
			heapq.heappush(heap, (c, b))

	print(res)


if __name__ == "__main__":
	main()
