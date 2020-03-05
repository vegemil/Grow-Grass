import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
	arr.append(int(sys.stdin.readline()))

stk = []
res = []
curr, idx = 1, 0
valid = True
while (True):
	if idx >= len(arr):
		break
	if curr < arr[idx]:
		res.append("+")
		stk.append(curr)
		curr += 1
	elif curr == arr[idx]:
		res.append("+")
		res.append("-")
		idx += 1
		curr += 1
	else:
		if stk.pop() == arr[idx]:
			res.append("-")
			idx += 1
		else:
			valid = False
			break

if not valid or idx < len(arr)-1:
	print("NO")
else:
	for el in res:
		print(el)
