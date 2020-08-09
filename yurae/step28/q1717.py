import sys

def unify(x, y, arr):
	find_x = find(x, arr)
	find_y = find(y, arr)
	if find_x == find_y:
		return
	arr[find_x] = arr[find_y]


def find(x, arr):
	if arr[x] != x:
		arr[x] = find(arr[x], arr)
	return arr[x]		


def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = [i for i in range(n+1)]
	for _ in range(m):
		sel, x, y = map(int, sys.stdin.readline().split())
		if sel == 0:
			unify(x, y, arr)
		else:
			if find(x, arr) == find(y, arr):
				print("YES")
			else:
				print("NO")


if __name__ == "__main__":
	main()
