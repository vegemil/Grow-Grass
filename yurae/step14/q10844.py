def main():
	n = int(input())
	arr = [[-1 for _ in range(10)] for _ in range(n)]
	arr[0] = [1 for _ in range(10)]
	arr[0][0] = 0

	for i in range(1, n):
		for j in range(0, 10):
			if (j == 0):
				arr[i][j] = arr[i-1][j+1]
			elif (j == 9):
				arr[i][j] = arr[i-1][j-1]
			else:
				arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

	print(sum(arr[-1])%1000000000)


if __name__ == "__main__":
	main()
