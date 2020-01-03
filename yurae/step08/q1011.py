import sys, math

def main():
	n = int(sys.stdin.readline())
	for _ in range(n):
		x, y = map(int, sys.stdin.readline().split())
		dist = y - x

		cnt = 0
		for i in range(int(math.sqrt(dist)), dist+1):
			if (i*i + i >= dist):
				if(i*i >= dist):
					cnt = 2*i-1
				else:
					cnt = 2*i
				break

		print(cnt)

if __name__ == "__main__":
	main()
