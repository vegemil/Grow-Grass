import sys

def main():
	INF = 2147483647
	n, m = map(int, sys.stdin.readline().split())
	edges = []
	for _ in range(m):
		a, b, c = map(int, sys.stdin.readline().split())
		edges.append((a, b, c))

	dist = [INF for _ in range(n+1)]
	dist[1] = 0
	valid = True
	for i in range(n):
		for j in range(m):
			x, y, w = edges[j]
			if (dist[x] != INF and dist[y] > dist[x] + w):
				dist[y] = dist[x] + w
				if (i == n-1):
					print(-1)
					return

	for i in range(n):
		for j in range(m):
			x, y, w = edges[j]
			if (dist[x] != INF and dist[y] > dist[x] + w):
				print(-1)
				return


	for i in range(2, n+1):
		res = dist[i] if dist[i] < INF else -1
		print(res)
	

if __name__ == "__main__":
	main()
