import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))

	chk = [[-1, -1, -1] for _ in range(n)]
	chk[0] = [arr[0], arr[0], -1]
	if (n > 1):
		chk[1] = [arr[0]+arr[1], arr[1], arr[0]]

	for i in range(2, n):
		chk[i][0] = arr[i] + max(chk[i-1][1:])
		chk[i][1] = arr[i] + max(chk[i-2])
		chk[i][2] = max(chk[i-1])

	print(max(chk[-1]))



if __name__ == "__main__":
	main()
