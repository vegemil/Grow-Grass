import sys

(n, x) = map(int, sys.stdin.readline().split())
arr = list(filter(lambda k:k < x, map(int, sys.stdin.readline().split())))
print(arr[0], end="")
for el in arr[1:]:
	print("", el, end="")
print("")
