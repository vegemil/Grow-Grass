import sys, heapq

def main():
	m, n = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	chk = [[0 for _ in range(m)] for _ in range(n)]
	heap = []
	for i in range(n):
		for j in range(m):
			if (arr[i][j] == 1):
				heapq.heappush(heap, (0, i, j))

	while(heap):
		val, i, j = heapq.heappop(heap)
		if i>0 and arr[i-1][j] == 0:
			chk[i-1][j] = val+1
			arr[i-1][j] = val+1
			heapq.heappush(heap, (val+1, i-1, j))
		if i<n-1 and arr[i+1][j] == 0:
			chk[i+1][j] = val+1
			arr[i+1][j] = val+1
			heapq.heappush(heap, (val+1, i+1, j))
		if j>0 and arr[i][j-1] == 0:
			chk[i][j-1] = val+1
			arr[i][j-1] = val+1
			heapq.heappush(heap, (val+1, i, j-1))
		if j<m-1 and arr[i][j+1] == 0:
			chk[i][j+1] = val+1
			arr[i][j+1] = val+1
			heapq.heappush(heap, (val+1, i, j+1))

	mx = 0
	for i in range(n):
		for j in range(m):
			if (arr[i][j] == 0):
				print(-1)
				return
		mx = max([mx] + chk[i])
	print(mx)



if __name__ == "__main__":
	main()
