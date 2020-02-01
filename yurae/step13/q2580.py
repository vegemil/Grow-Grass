import sys

# works in pypy3
def get_cands(arr, i, j):
	res = [i for i in range(1, 10)]
	for k in range(9):
		if arr[i][k] in res:
			res.remove(arr[i][k])
		if arr[k][j] in res:
			res.remove(arr[k][j])

	start_row = i - i%3
	start_col = j - j%3
	for row in range(start_row, start_row+3):
		for col in range(start_col, start_col+3):
			if arr[row][col] in res:
				res.remove(arr[row][col])

	return res


def pick(arr, blanks, curr):
	if curr >= len(blanks):
		print_arr(arr)
		sys.exit(0)

	(row, col) = blanks[curr]
	cands = get_cands(arr, row, col)
	for cand in cands:
		arr[row][col] = cand
		pick(arr, blanks, curr+1)
		arr[row][col] = 0


def print_arr(arr):
	for row in arr:
		for el in row[:-1]:
			print(el, end=" ")
		print(row[-1])



def main():
	arr = []
	for _ in range(9):
		arr.append(list(map(int, sys.stdin.readline().split())))

	blanks = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
	pick(arr, blanks, 0)


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
