def main():
	n = int(input())
	n = n%1500000

	arr = []
	a1 = 0
	a2 = 1
	arr.append(a1)
	arr.append(a2)
	for i in range(1500000):
		a1, a2 = a2, (a1+a2)%1000000
		arr.append(a2)

	print(arr[n])

if __name__ == "__main__":
	main()

