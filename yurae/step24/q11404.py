import sys

def main():
	INF = 2147483647
	n = int(sys.stdin.readline())
	m = int(sys.stdin.readline())

	dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
	edges = [[] for _ in range(n+1)]
	for _ in range(m):
		a, b, c = map(int, sys.stdin.readline().split())
		edges[a].append((b, c))
		if (dist[a][b] > c):
			dist[a][b] = c

	for i in range(n+1):
		dist[i][i] = 0

	for k in range(1, n+1):
		for i in range(1, n+1):
			for j in range(1, n+1):
				if (dist[i][k] < INF and dist[k][j] < INF):
					if (dist[i][k] + dist[k][j] < dist[i][j]):
						dist[i][j] = dist[i][k] + dist[k][j]

	for i in range(1, n+1):
		for j in range(1, n+1):
			if (dist[i][j] < INF):
				print(dist[i][j], end=" ")
			else:
				print(0, end=" ")
		print("")


if __name__ == "__main__":
	main()
