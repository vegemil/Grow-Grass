import sys


def get_cnt(arr, n, x, y):
	res = [0, 0, 0]
	if n <= 1:
		res[arr[y][x]+1] += 1
		return res
	k = n//3
	for i in range(3):
		for j in range(3):
			div = get_cnt(arr, k, x+i*k, y+j*k)
			for idx in range(3):
				res[idx] += div[idx]
	for i in range(3):
		if res[i] == 9 and sum(res) == 9:
			res[i] = 1
	return res


def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	res = get_cnt(arr, n, 0, 0)
	for el in res:
		print(el)


if __name__ == "__main__":
	main()
