import sys
from heapq import heappush, heappop

def main():
	heap = []
	n = int(sys.stdin.readline())
	for _ in range(n):
		curr = int(sys.stdin.readline())
		if (curr == 0):
			if not heap:
				print(0)
				continue
			else:
				el = heappop(heap)
				print(el[0]*el[1])
		else:
			heappush(heap, [abs(curr), curr//abs(curr)])


if __name__ == "__main__":
	main()
