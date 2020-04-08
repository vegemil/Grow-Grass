# works in pypy3
import sys

def chk(arr, n, m, h):
	res = 0
	for el in arr:
		res += max(0, el - h)
	return (res >= m)


def pick(arr, n, m):
	bot = 0
	top = 1000000000
	curr = (top+bot)//2
	res = 0

	while(bot <= top):
		chk_len = chk(arr, n, m, curr)
		if chk_len == True:
			res = curr
			bot = curr+1
		else:
			top = curr-1
		curr = (top+bot)//2
	return res


def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = list(map(int, sys.stdin.readline().split()))
	print(pick(arr, n, m))



if __name__ == "__main__":
	main()
