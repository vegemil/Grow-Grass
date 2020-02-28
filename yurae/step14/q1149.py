import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	chk = [[-1, -1, -1] for _ in range(n)]
	chk[0] = arr[0]
	for i in range(1, n):
		chk[i][0] = arr[i][0] + min(chk[i-1][1], chk[i-1][2])
		chk[i][1] = arr[i][1] + min(chk[i-1][0], chk[i-1][2])
		chk[i][2] = arr[i][2] + min(chk[i-1][0], chk[i-1][1])

	print(min(chk[-1]))


if __name__ == "__main__":
	main()
