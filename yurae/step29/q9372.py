import sys

def main():
	for _ in range(int(sys.stdin.readline())):
		n, m = map(int, sys.stdin.readline().split())
		for _ in range(m):
			a, b = map(int, sys.stdin.readline().split())

		print(n-1)

if __name__ == "__main__":
	main()
