import sys

def ref_count(curr, nodes, res):
	for adj in nodes[curr][0]:
		nodes[adj][1] -= 1
		if (nodes[adj][1] <= 0):
			res.append(adj)
			ref_count(adj, nodes, res)


def main():
	for _ in range(int(sys.stdin.readline())):
		fl = 0

		n = int(sys.stdin.readline())
		nodes = [[[], 0] for _ in range(n+1)]
		arr = list(map(int, sys.stdin.readline().split()))
		for i in range(1, n):
			for j in range(0, i):
				nodes[arr[j]][0].append(arr[i])
				nodes[arr[i]][1] += 1

		m = int(sys.stdin.readline())
		for _ in range(m):
			a, b = map(int, sys.stdin.readline().split())
			if (b in nodes[a][0]):
				nodes[a][0].remove(b)
				nodes[b][0].append(a)
				nodes[a][1] += 1
				nodes[b][1] -= 1
			elif (a in nodes[b][0]):
				nodes[b][0].remove(a)
				nodes[a][0].append(b)
				nodes[b][1] += 1
				nodes[a][1] -= 1
			else:
				fl = 2
				break

		start_nodes = []
		for i in range(1, n+1):
			if (nodes[i][1] == 0):
				start_nodes.append(i)	

		res = []
		for node in start_nodes:
			res.append(node)
			ref_count(node, nodes, res)

		for node in nodes:
			if (node[1] != 0):
				fl = 2
				break

		if fl == 1:
			print("?")
			continue
		elif fl == 2:
			print("IMPOSSIBLE")
			continue

		for r in res[:-1]:
			print(r, end=" ")
		print(res[-1])



sys.setrecursionlimit(1000000)
main()
