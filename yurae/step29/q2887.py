import sys, heapq

def dist(a, b):
	return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def unify(arr, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_y] = find_x
		return True
	else:
		return False


def main():
	n = int(sys.stdin.readline())
	points = []
	for i in range(n):
		points.append([i, list(map(int, sys.stdin.readline().split()))])

	heap = []
	points = sorted(points, key=lambda x:x[1][0])
	for i in range(n-1):
		heapq.heappush(heap, [dist(points[i][1], points[i+1][1]), points[i][0], points[i+1][0]])

	points = sorted(points, key=lambda x:x[1][1])
	for i in range(n-1):
		heapq.heappush(heap, [dist(points[i][1], points[i+1][1]), points[i][0], points[i+1][0]])

	points = sorted(points, key=lambda x:x[1][2])
	for i in range(n-1):
		heapq.heappush(heap, [dist(points[i][1], points[i+1][1]), points[i][0], points[i+1][0]])

	arr = [i for i in range(n)]

	res = 0
	while heap:
		edge, a, b = heapq.heappop(heap)
		if unify(arr, a, b):
			res += edge

	print(res)


if __name__ == "__main__":
	main()
