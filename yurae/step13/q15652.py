import sys


def pick(lower, upper, total, curr, res):
	for i in range(lower, upper+1):
		nxt = curr[:]
		nxt.append(i)
		if (len(nxt) >= total):
			res.append(nxt)
			continue
		pick(i, upper, total, nxt, res)



def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = []
	pick(1, n, m, [], arr)

	arr.sort()
	for el in arr:
		for num in el[:-1]:
			print(num, end=" ")
		print(el[-1])


if __name__ == "__main__":
	main()
