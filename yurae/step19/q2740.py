import sys

def main():
	n, m = map(int, sys.stdin.readline().split())
	arr_a, arr_b = [], []
	for _ in range(n):
		arr_a.append(list(map(int, sys.stdin.readline().split())))

	m, k = map(int, sys.stdin.readline().split())
	for _ in range(m):
		arr_b.append(list(map(int, sys.stdin.readline().split())))

	res = [[0 for _ in range(k)] for _ in range(n)]

	for i in range(n):
		for j in range(m):
			for h in range(k):
				res[i][h] += arr_a[i][j] * arr_b[j][h]

	for row in res:
		for el in row:
			print(el, end=" ")
		print("")


main()
