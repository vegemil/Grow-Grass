import sys

arr = []
for _ in range(10):
	arr.append(int(sys.stdin.readline())%42)
arr = sorted(arr)

cnt = 1
for i in range(1, len(arr)):
	if(arr[i] != arr[i-1]):
		cnt = cnt + 1

print(cnt)
