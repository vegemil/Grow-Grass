import sys

def unify(arr, cnt, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_x] = find_y
		cnt[find_y] += cnt[find_x]


def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def main():
	for _ in range(int(sys.stdin.readline())):
		f = int(sys.stdin.readline())
		arr = [i for i in range(100000)]
		cnt = [1 for _ in range(100000)]

		dic = {}
		curr = 0
		for _ in range(f):
			line = sys.stdin.readline().split()
			x, y = line[0], line[1]
			if not x in dic:
				dic[x] = curr
				curr += 1
			if not y in dic:
				dic[y] = curr
				curr += 1
			unify(arr, cnt, dic[x], dic[y])
			print(cnt[find(arr, dic[x])])


if __name__ == "__main__":
	main()
