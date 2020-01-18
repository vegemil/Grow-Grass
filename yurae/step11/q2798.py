import sys

def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = list(map(int, sys.stdin.readline().split()))

	res = -1
	for i in range(n):
		for j in range(i+1, n):
			for k in range(j+1, n):
				curr = arr[i] + arr[j] + arr[k]
				if (curr == m):
					print(curr)
					return
				if ((curr < m) and (m - res > m - curr)):
					res = curr
	
	print(res)


main()
