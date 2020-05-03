import sys


def dfs(arr, x, y):
	arr[x][y][1] = True
	if (x > 0 and arr[x-1][y][0] == 1 and arr[x-1][y][1] == False):
		dfs(arr, x-1, y)
	if (x < len(arr)-1 and arr[x+1][y][0] == 1 and arr[x+1][y][1] == False):
		dfs(arr, x+1, y)
	if (y > 0 and arr[x][y-1][0] == 1 and arr[x][y-1][1] == False):
		dfs(arr, x, y-1)
	if (y < len(arr[0])-1 and arr[x][y+1][0] == 1 and arr[x][y+1][1] == False):
		dfs(arr, x, y+1)
	


def main():
	t = int(sys.stdin.readline())
	for _ in range(t):
		m, n, k = map(int, sys.stdin.readline().split())
		arr = [[[0, False] for _ in range(n)] for _ in range(m)]
		for _ in range(k):
			x, y = map(int, sys.stdin.readline().split())
			arr[x][y][0] = 1

		cnt = 0
		for i in range(m):
			for j in range(n):
				if (arr[i][j][1] == True or arr[i][j][0] == 0):
					continue
				cnt += 1
				dfs(arr, i, j)
		print(cnt)


if __name__ == "__main__":
	sys.setrecursionlimit(100000000)
	main()
