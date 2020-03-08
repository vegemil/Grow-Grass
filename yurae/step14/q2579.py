import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))

	if (n < 2):
		print(arr[0])
		return

	chk = [[-1, -1, -1] for _ in range(n)]
	chk[0] = [0, arr[0], arr[0]]
	chk[1] = [arr[0], arr[1], arr[0] + arr[1]]
	i = 2
	for i in range(2, n):
		chk[i][0] = max([chk[i-2][0], chk[i-2][2]]) + arr[i]
		chk[i][1] = max(chk[i-1])
		chk[i][2] = max(chk[i-1][:-1]) + arr[i]

	print(max([chk[-1][0], chk[-1][2]]))

if __name__ == "__main__":
	main()
