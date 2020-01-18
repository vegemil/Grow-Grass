def main():
	mx = 100
	arr = [-1 for _ in range(mx)]
	arr[0] = 0
	arr[1] = 1

	n = int(input())
	if (n < 2):
		print(arr[n])
		return

	for i in range(2, n+1):
		arr[i] = arr[i-1] + arr[i-2]
	
	print(arr[n])


if __name__ == "__main__":
	main()
