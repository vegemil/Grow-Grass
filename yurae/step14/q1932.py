import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	chk = [[-1 for _ in range(i+1)] for i in range(n)]
	chk[0] = arr[0]
	for i in range(1, n):
		for j in range(i+1):
			if (j == 0):
				chk[i][j] = chk[i-1][j] + arr[i][j]
			elif (j >= i):
				chk[i][j] = chk[i-1][j-1] + arr[i][j]
			else:
				chk[i][j] = max(chk[i-1][j-1], chk[i-1][j]) + arr[i][j]
	
	print(max(chk[-1]))

if __name__ == "__main__":
	main()
