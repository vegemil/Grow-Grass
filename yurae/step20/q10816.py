import sys

cnt = [0 for _ in range(-10000000, 10000001)]
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for el in arr:
	cnt[el] += 1
m = int(sys.stdin.readline())
chk = list(map(int, sys.stdin.readline().split()))
for el in chk:
	print(cnt[el], end=" ")
print("")
