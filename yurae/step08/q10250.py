import sys

def main():
	n = int(sys.stdin.readline())
	for _ in range(n):
		h, w, n = map(int, sys.stdin.readline().split())
		if n % h == 0:
			res = h*100 + (n//h)
		else:
			res = (n - h*(n//h))*100 + (n//h) + 1
		print(res)

if __name__ == "__main__":
	main()
