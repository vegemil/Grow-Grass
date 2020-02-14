import sys

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	# length, prev
	chk = [[-1, -1] for _ in range(n)]
	chk[0] = [1, arr[0]]

	for i in range(1, n):
		for j in range(i-1, -1, -1):
			if (arr[j] < arr[i] and chk[j][0] >= chk[i][0]):
				chk[i] = [chk[j][0]+1, arr[j]]
		if (chk[i][0] == -1):
			chk[i] = [1, arr[i]]
			
	print(max(chk)[0])


if __name__ == "__main__":
	main()
