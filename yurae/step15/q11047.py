import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
	arr.append(int(sys.stdin.readline()))

cnt = 0
while (k > 0):
	curr = arr.pop()
	cnt += k // curr
	k = k % curr

print(cnt)
