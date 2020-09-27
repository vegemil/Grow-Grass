import sys

def ref_count(curr, nodes, res):
	for adj in nodes[curr][0]:
		nodes[adj][1] -= 1
		if (nodes[adj][1] <= 0):
			res.append(adj)
			ref_count(adj, nodes, res)


def main():
	n, m = map(int, sys.stdin.readline().split())
	# adj, count
	nodes = [[[], 0] for _ in range(n+1)]
	
	for _ in range(m):
		a, b = map(int, sys.stdin.readline().split())
		nodes[a][0].append(b)
		nodes[b][1] += 1

	start_nodes = []
	for i in range(1, n+1):
		if (nodes[i][1] == 0):
			start_nodes.append(i)

	res = []
	for node in start_nodes:
		res.append(node)
		ref_count(node, nodes, res)

	for r in res[:-1]:
		print(r, end=" ")
	print(res[-1])


sys.setrecursionlimit(100000)
main()

