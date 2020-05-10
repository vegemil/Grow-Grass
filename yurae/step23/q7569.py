import sys, heapq

def main():
	m, n, h = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(h):
		arr.append([])
		for _ in range(n):
			arr[-1].append(list(map(int, sys.stdin.readline().split())))

	chk = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
	heap = []
	for i in range(h):
		for j in range(n):
			for k in range(m):
				if (arr[i][j][k] == 1):
					heapq.heappush(heap, (0, i, j, k))

	while(heap):
		val, i, j, k = heapq.heappop(heap)
		if i>0 and arr[i-1][j][k] == 0:
			chk[i-1][j][k] = val+1
			arr[i-1][j][k] = val+1
			heapq.heappush(heap, (val+1, i-1, j, k))
		if i<h-1 and arr[i+1][j][k] == 0:
			chk[i+1][j][k] = val+1
			arr[i+1][j][k] = val+1
			heapq.heappush(heap, (val+1, i+1, j, k))
		if j>0 and arr[i][j-1][k] == 0:
			chk[i][j-1][k] = val+1
			arr[i][j-1][k] = val+1
			heapq.heappush(heap, (val+1, i, j-1, k))
		if j<n-1 and arr[i][j+1][k] == 0:
			chk[i][j+1][k] = val+1
			arr[i][j+1][k] = val+1
			heapq.heappush(heap, (val+1, i, j+1, k))
		if k>0 and arr[i][j][k-1] == 0:
			chk[i][j][k-1] = val+1
			arr[i][j][k-1] = val+1
			heapq.heappush(heap, (val+1, i, j, k-1))
		if k<m-1 and arr[i][j][k+1] == 0:
			chk[i][j][k+1] = val+1
			arr[i][j][k+1] = val+1
			heapq.heappush(heap, (val+1, i, j, k+1))

	mx = 0
	for i in range(h):
		for j in range(n):
			for k in range(m):
				if (arr[i][j][k] == 0):
					print(-1)
					return
			mx = max([mx] + chk[i][j])
	print(mx)



if __name__ == "__main__":
	main()
