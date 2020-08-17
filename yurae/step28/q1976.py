import sys

def unify(arr, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_x] = find_y


def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def main():
	n = int(sys.stdin.readline())
	m = int(sys.stdin.readline())
	arr = [i for i in range(n+1)]
	for i in range(n):
		line = list(map(int, sys.stdin.readline().split()))
		for j in range(n):
			if line[j] == 1:
				unify(arr, i+1, j+1)
	
	q = list(map(int, sys.stdin.readline().split()))
	curr = q[0]
	for el in q[1:]:
		if find(arr, curr) != find(arr, el):
			print("NO")
			return
	print("YES")


if __name__ == "__main__":
	main()
