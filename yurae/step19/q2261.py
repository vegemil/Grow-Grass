import sys, math
from collections import deque


def dist(a, b):
	return (a[0] - b[0])**2 + (a[1] - b[1])**2


def sweep(arr, start, end):
	if (end-start < 2):
		return 1000000000
	elif (end-start == 2):
		return (dist(arr[start], arr[end-1]))
	curr = (start+end)//2
	min_dist = min(sweep(arr, start, curr), sweep(arr, curr, end))
	
	cands = [*filter(lambda d: (d[0]-arr[curr][0])**2<min_dist, arr[start:end])]
	cands.sort(key=lambda x: x[1])
	for i in range(len(cands)):
		for j in range(i+1, len(cands)):
			if ((cands[i][1] - cands[j][1])**2 >= min_dist):
				break
			min_dist = min(min_dist, dist(cands[i], cands[j]))
	return min_dist


def main():
	n = int(sys.stdin.readline())
	arr = []
	for i in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())) + [i])
	arr.sort()

	print(sweep(arr, 0, n))



if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
