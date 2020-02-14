import sys

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	# max-left, prev-left, max-right, prev-right
	chk = [[-1, -1, -1, -1] for _ in range(n)]

	for i in range(0, n):
		chk[i][0] = 1
		chk[i][1] = arr[i]
		for j in range(i-1, -1, -1):
			if (arr[j] < arr[i] and chk[j][0] >= chk[i][0]):
				chk[i][0] = chk[j][0]+1
				chk[i][1] = arr[j]

	for i in range(n-1, -1, -1):
		chk[i][2] = 1
		chk[i][3] = arr[i]
		for j in range(i+1, n):
			if (arr[j] < arr[i] and chk[j][2] >= chk[i][2]):
				chk[i][2] = chk[j][2]+1
				chk[i][3] = arr[j]

	mx = -1
	for el in chk:
		if (el[0] + el[2] - 1> mx):
			mx = el[0] + el[2] - 1
	print(mx)

if __name__ == "__main__":
	main()
