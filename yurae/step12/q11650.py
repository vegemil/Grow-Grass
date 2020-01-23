import sys

def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))
	arr.sort()

	for el in arr:
		print(el[0], el[1])

if __name__ == "__main__":
	main()
