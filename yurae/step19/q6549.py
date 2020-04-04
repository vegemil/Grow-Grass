import sys


def main():
	while(True):
		line = list(map(int, sys.stdin.readline().split()))
		n = line[0]
		if (n == 0):
			return

		arr = line[1:]
		arr.append(0)
		res = arr[0]

		# [idx, height]
		stk = []
		stk.append([-1, 0])
		stk.append([0, arr[0]])
		for i in range(1, len(arr)):
			while(stk and stk[-1][1] > arr[i]):
				top = stk.pop()
				res = max((i - stk[-1][0] - 1) * top[1], res)
			stk.append([i, arr[i]])
		print(res)
	

if __name__ == "__main__":
	sys.setrecursionlimit(10000000)
	main()
