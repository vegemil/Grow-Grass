from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
	p = sys.stdin.readline().split()[0]
	n = int(sys.stdin.readline())
	line = sys.stdin.readline().split()[0]
	arr = deque(line[1:-1].split(','))

	if (arr[0] == ''):
		arr = []

	front = True
	is_valid = True
	for cmd in p:
		if cmd == "R":
			front = not front
			continue
		if not arr:
			is_valid = False
			break
		else:
			if front:
				arr.popleft()
			else:
				arr.pop()

	if not is_valid:
		print("error")
		continue

	arr = list(arr)
	if not front:
		arr.reverse()

	if len(arr) > 0 :
		print("[", end="")
		for el in arr[:-1]:
			print(el, end=",")
		print(arr[-1], end="]\n")
	else:
		print("[]")
