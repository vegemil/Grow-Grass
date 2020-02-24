n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))
cnt = 0
mx = 0
for el in arr:
	if (el[0] < mx):
		continue
	else:
		cnt += 1
		mx = el[1]

print(cnt)
