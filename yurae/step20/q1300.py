import sys


def chk(n, k, curr):
	res = 0
	for i in range(1, n+1):
			res += min(n, curr//i)
	return res >= k


def pick(n, k):
	bot = 1
	top = n**2
	res = 1

	while (bot <= top):
		curr = (bot+top)//2
		if chk(n, k, curr) == True:
			res = curr
			top = curr - 1
		else:
			bot = curr + 1
	return res


def main():
	n = int(sys.stdin.readline())
	k = int(sys.stdin.readline())

	print(pick(n, k))

if __name__ == "__main__":
	main()
