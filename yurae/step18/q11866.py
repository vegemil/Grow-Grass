from collections import deque

n, k = map(int, input().split())
arr = deque([i+1 for i in range(n)])
res = []

while (arr):
	for _ in range(k-1):
		arr.append(arr.popleft())
	res.append(arr.popleft())

print("<", end="")
for el in res[:-1]:
	print(el, end=", ")
print(res[-1], end=">\n")
