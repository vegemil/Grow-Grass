import sys


def dfs(it, ib, pt, pb, ins, inidx, posts):
	if it > ib or pt > pb:
		return

	root = posts[pb]
	print(root, end=" ")

	dfs(it, inidx[root]-1, pt, pt+(inidx[root]-it)-1, ins, inidx, posts)
	dfs(inidx[root]+1,ib, pt+(inidx[root]-it), pb-1, ins, inidx, posts)


sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
inidx = [-1 for _ in range(n+1)]
for i in range(n):
	inidx[inorder[i]] = i

dfs(0, n-1, 0, n-1, inorder, inidx, postorder)
print("")


