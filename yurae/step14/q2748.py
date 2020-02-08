import sys

def main():
	n = int(sys.stdin.readline())

	a0 = 0
	a1 = 1
	for i in range(n):
		a0, a1 = a1, a0 + a1
	print(a0)
	

if __name__ == "__main__":
	main()
