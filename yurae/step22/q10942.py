import sys

def main():
	n = int(sys.stdin.readline())
	arr = [0] + list(map(int, sys.stdin.readline().split()))
	m = int(sys.stdin.readline())
	q_arr = []
	for _ in range(m):
		q_arr.append(list(map(int, sys.stdin.readline().split())))

	chk = [[-1 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(n, 0, -1):
		for j in range(i, n+1):
			if (i == j):
				chk[i][j] = 1
				continue
			if (arr[i] != arr[j]):
				chk[i][j] = 0
				continue
			if (j - i == 1):
				chk[i][j] = 1
				continue
			chk[i][j] = chk[i+1][j-1]

	for el in q_arr:
		print(chk[el[0]][el[1]])


if __name__ == "__main__":
	main()
