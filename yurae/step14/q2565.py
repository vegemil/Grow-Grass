import sys

def main():
	n = int(sys.stdin.readline())
	# adj
	arr = []
	for _ in range(n):
		a, b = map(int, sys.stdin.readline().split())
		arr.append([a, b])
	arr = sorted(arr)

	# max-left, prev-left, max-right, prev-right
	chk = [[-1, -1] for _ in range(len(arr))]
	for i in range(n):
		chk[i][0] = 1
		chk[i][1] = arr[i][1]
		for j in range(i-1, -1, -1):
			if (arr[j][1] < arr[i][1] and chk[j][0] >= chk[i][0]):
				chk[i][0] = chk[j][0]+1
				chk[i][1] = arr[j][1]

	mx = max(chk)[0]
	print(n - mx)


if __name__ == "__main__":
	main()
