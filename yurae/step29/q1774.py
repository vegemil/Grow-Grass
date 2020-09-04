import sys, heapq, math

def dist(a, b):
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def unify(arr, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_y] = find_x


def main():
	n, m = map(int, sys.stdin.readline().split())
	points = []
	for _ in range(n):
		points.append(list(map(int, sys.stdin.readline().split())))

	heap = []
	for i in range(n):
		for j in range(n):
			if i != j:
				heapq.heappush(heap, (dist(points[i], points[j]), i, j))

	res = 0
	arr = [i for i in range(n)]
	for _ in range(m):
		a_, b_ = map(int, sys.stdin.readline().split())
		a, b = a_-1, b_-1
		unify(arr, a, b)

	while(heap):
		edge, a, b = heapq.heappop(heap)
		if find(arr, a) != find(arr, b):
			unify(arr, a, b)
			res += edge
	
	print("{:.2f}".format(res))


if __name__ == "__main__":
	main()
