import sys, heapq

# works in pypy3
def main():
	INF = 2147483647
	for _ in range(int(sys.stdin.readline())):
		n, m, k = map(int, sys.stdin.readline().split())
		edges = [[] for _ in range(n+1)]
		for _ in range(k):
			u, b, c, d = map(int, sys.stdin.readline().split())
			edges[u].append((b, c, d))

		dist = [[INF for _ in range(m+1)] for _ in range(n+1)]
		dist[1] = [0 for _ in range(m+1)]
		for j in range(m+1):
			for i in range(1, n+1):
				if (dist[i][j] >= INF):
					continue
				for adj, c, d in edges[i]:
					if (m >= j+c):
						dist[adj][j+c] = min(dist[adj][j+c], d+dist[i][j])
		if (min(dist[n]) < INF):
			print(min(dist[n]))
		else:
			print("Poor KCM")


if __name__ == "__main__":
	main()
