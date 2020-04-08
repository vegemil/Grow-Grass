import sys

def chk(arr, c, curr):
	res = 1
	prev_idx = 0
	for i in range(1, len(arr)):
		if (arr[i] - arr[prev_idx] >= curr):
			res += 1
			prev_idx = i
	return res >= c


def pick(arr, c):
	maxval = max(arr)//c
	top = maxval
	bot = 1
	res = 0
	while (bot <= top):
		curr = (top+bot)//2
		if chk(arr, c, curr):
			res = curr
			bot = curr+1
		else:
			top = curr-1
	return res


def main():
	n, c = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))
	arr.sort()
	print(pick(arr, c))


if __name__ == "__main__":
	main()
