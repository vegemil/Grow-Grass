import sys

def main():
	n = int(sys.stdin.readline())
	stk = []
	for _ in range(n):
		line = sys.stdin.readline().split()
		if (line[0] == "push"):
			stk.append(line[1])
		elif (line[0] == "pop"):
			res = -1 if not stk else stk.pop()
			print(res)
		elif (line[0] == "size"):
			print(len(stk))
		elif (line[0] == "empty"):
			res = 1 if not stk else 0
			print(res)
		else:
			res = -1 if not stk else stk[-1]
			print(res)


main()
