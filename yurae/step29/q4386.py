import sys, heapq, math

def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def unify(arr, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_y] = find_x


def get_dist(a, b):
	return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def main():
	n = int(sys.stdin.readline())
	arr = [i for i in range(n)]
	pos = []
	for _ in range(n):
		x, y = map(float, sys.stdin.readline().split())
		pos.append((x, y))

	heap = []
	for i in range(n):
		for j in range(n):
			if i != j:
				heapq.heappush(heap, (get_dist(pos[i], pos[j]), i, j))

	res = 0
	while heap:
		dist, curr, adj = heapq.heappop(heap)
		if find(arr, curr) != find(arr, adj):
			unify(arr, curr, adj)
			res += dist

	print(res)


if __name__ == "__main__":
	main()
