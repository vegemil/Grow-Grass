n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
cnt = 0
for i in range(n):
	cnt += arr[i]
	if (i < n-1):
		arr[i+1] += arr[i]
print(cnt)
