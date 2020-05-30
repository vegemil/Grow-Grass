import sys

# works in pypy3
def main():
	INF = 2147483647
	v, e = map(int, sys.stdin.readline().split())

	dist = [[INF for _ in range(v+1)] for _ in range(v+1)]
	for i in range(1, v+1):
		dist[i][i] = 0

	for _ in range(e):
		a, b, c = map(int, sys.stdin.readline().split())
		if (dist[a][b] > c):
			dist[a][b] = c

	for k in range(1, v+1):
		for i in range(1, v+1):
			for j in range(1, v+1):
				if (dist[i][k] + dist[k][j] < dist[i][j]):
					dist[i][j] = dist[i][k] + dist[k][j]

	min_cycle = INF
	for i in range(1, v+1):
		for j in range(1, v+1):
			if (i == j):
				continue
			if(dist[i][j] + dist[j][i] < min_cycle):
				min_cycle = dist[i][j] + dist[j][i]

	if min_cycle < INF:
		print(min_cycle)
	else:
		print(-1)



if __name__ == "__main__":
	main()
