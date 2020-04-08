import sys
from heapq import heappush, heappop

def main():
	heap = []
	n = int(sys.stdin.readline())
	for _ in range(n):
		curr = int(sys.stdin.readline())
		if (curr == 0):
			res = 0 if not heap else -heappop(heap)
			print(res)
		else:
			heappush(heap, -curr)


if __name__ == "__main__":
	main()
