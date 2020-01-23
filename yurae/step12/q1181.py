import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(sys.stdin.readline()[:-1])

	arr = sorted(arr, key=lambda x: (len(x), x))
	bef = ""
	for el in arr:
		if (el == bef):
			continue
		print(el)
		bef = el

if __name__ == "__main__":
	main()
