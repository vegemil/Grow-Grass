import sys

def mulArr(A, B):
	N, M, K = len(A), len(B), len(B[0])
	res = [[0 for _ in range(N)] for _ in range(K)]
	for i in range(N):
		for j in range(M):
			for k in range(K):
				res[i][k] += (A[i][j] * B[j][k]) % 1000
	return res


def main():
	n, b = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	res = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
	while (b > 0):
		if (b%2 != 0):
			res = mulArr(arr, res)
		arr = mulArr(arr, arr)
		b //= 2

	for row in res:
		for el in row:
			print(el%1000, end=" ")
		print("")


main()
