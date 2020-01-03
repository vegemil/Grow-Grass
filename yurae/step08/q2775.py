import sys

t = int(sys.stdin.readline())
arr = [[-1 for _ in range(15)] for _ in range(15)]
arr[0] = [i for i in range(15)]
for i in range(1, 15):
	for j in range(15):
		arr[i][j] = sum(arr[i-1][:(j+1)])

for _ in range(t):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	print(arr[k][n])
