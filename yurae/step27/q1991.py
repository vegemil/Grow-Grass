import sys

def insert(tree, curr, target, left, right):
	if tree[curr] == target:
		if curr*2+1 < len(tree):
			tree[curr*2+1] = left
		if curr*2+2 < len(tree):
			tree[curr*2+2] = right
		return True
	else:
		if curr*2+1 < len(tree):
			insert(tree, curr*2+1, target, left, right)
		if curr*2+2 < len(tree):
			insert(tree, curr*2+2, target, left, right)
		return False
	

def dfs(tree, curr, res):
	res[0] += tree[curr]
	if curr*2+1 < len(tree) and tree[curr*2+1] != ".":
		dfs(tree, curr*2+1, res)
	res[1] += tree[curr]
	if curr*2+2 < len(tree) and tree[curr*2+2] != ".":
		dfs(tree, curr*2+2, res)
	res[2] += tree[curr]


def main():
	n = int(sys.stdin.readline())
	tree = ["." for _ in range(n**2)]
	tree[0] = "A"
	for _ in range(n):
		p, l, r = sys.stdin.readline().split()
		insert(tree, 0, p, l, r)

	# pre, mid, post
	res = ["", "", ""]
	dfs(tree, 0, res)
	for el in res:
		print(el)	


if __name__ == "__main__":
	main()
