import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))
	arr = sorted(arr, key=lambda x: (x[1], x[0]))

	for el in arr:
		print(el[0], el[1])

if __name__ == "__main__":
	main()
