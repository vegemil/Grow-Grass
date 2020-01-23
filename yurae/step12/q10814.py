import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
	line = sys.stdin.readline().split()
	arr.append([int(line[0]), line[1]])
arr = sorted(arr, key=lambda x: x[0])
for el in arr:
	print(el[0], el[1])
