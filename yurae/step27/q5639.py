import sys


def find_next(tree, start, end, bound):
	while(end-start > 1):
		mid = (start+end)//2
		if tree[mid] > bound:
			end = mid
		else:
			start = mid
	return start
			

def pre2post(tree, start, end):
	if start > end:
		return
	curr = tree[start]
	if start == end:
		print(curr)
		return

	if curr > tree[end]:
		pre2post(tree, start+1, end)
		print(curr)
		return

	nxt = find_next(tree, start, end, curr)
	pre2post(tree, start+1, nxt)
	pre2post(tree, nxt+1, end)
	print(curr)


def main():
	tree = []
	while True:
		try:
			el = int(sys.stdin.readline())
			tree.append(el)
		except:
			break

	pre2post(tree, 0, len(tree)-1)
		

if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
