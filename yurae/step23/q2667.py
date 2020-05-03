import sys

def dfs(arr, chk, i, j, cnt):
	chk[i][j] = len(cnt)
	cnt[-1] += 1

	if i > 0 and arr[i-1][j] != '0' and chk[i-1][j] == 0:
		dfs(arr, chk, i-1, j, cnt)
	if i < len(arr)-1 and arr[i+1][j] != '0' and chk[i+1][j] == 0:
		dfs(arr, chk, i+1, j, cnt)
	if j > 0 and arr[i][j-1] != '0' and chk[i][j-1] == 0:
		dfs(arr, chk, i, j-1, cnt)
	if j < len(arr)-1 and arr[i][j+1] != '0' and chk[i][j+1] == 0:
		dfs(arr, chk, i, j+1, cnt)

		
def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(sys.stdin.readline().split()[0])

	chk = [[0 for _ in range(n)] for _ in range(n)]
	cnt = []
	curr = 1
	for i in range(n):
		for j in range(n):
			if (chk[i][j] > 0 or arr[i][j] == '0'):
				continue
			cnt.append(0)
			dfs(arr, chk, i, j, cnt)

	cnt = sorted(cnt)
	print(len(cnt))
	for el in cnt:
		print(el)


if __name__ == "__main__":
	main()
