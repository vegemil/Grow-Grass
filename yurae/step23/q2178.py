import sys
from collections import deque

def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(sys.stdin.readline().split()[0])

	chk = [[0 for _ in range(m)] for _ in range(n)]
	chk[0][0] = 1
	deq = deque([(0, 0)])
	while(deq):
		i, j = deq.popleft()
		if (i == n-1 and j == m-1):
			break
		if i>0 and arr[i-1][j] == '1' and chk[i-1][j] == 0:
			chk[i-1][j] = chk[i][j] + 1
			deq.append((i-1, j))
		if i<n-1 and arr[i+1][j] == '1' and chk[i+1][j] == 0:
			chk[i+1][j] = chk[i][j] + 1
			deq.append((i+1, j))
		if j>0 and arr[i][j-1] == '1' and chk[i][j-1] == 0:
			chk[i][j-1] = chk[i][j] + 1
			deq.append((i, j-1))
		if j<m-1 and arr[i][j+1] == '1' and chk[i][j+1] == 0:
			chk[i][j+1] = chk[i][j] + 1
			deq.append((i, j+1))
	print(chk[n-1][m-1])


if __name__ == "__main__":
	main()
