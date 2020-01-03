import sys

def main():
	(a, b, c) = map(int, sys.stdin.readline().split())
	if b >= c:
		print(-1)
		return

	res = a // (c-b)
	print(res + 1)


if __name__ == "__main__":
	main()
