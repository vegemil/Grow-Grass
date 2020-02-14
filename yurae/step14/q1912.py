def main():
	n = int(input())
	arr = list(map(int, input().split()))

	chk = [0 for _ in range(n)]
	chk[0] = arr[0]
	mx = arr[0]
	for i in range(1, n):
		chk[i] = max([arr[i], chk[i-1] + arr[i]])
		mx = max(chk[i], mx)

	print(mx)

if __name__ == "__main__":
	main()
