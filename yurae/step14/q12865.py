import sys

def getVal(i, w, vals, items):
	if (vals[i][w] > -1):
		return vals[i][w]
	if w == 0:
		return 0

	curr_w = items[i][0]
	curr_v = items[i][1]

	if i == 0:
		if (w < curr_w):
			vals[i][w] = 0
			return 0
		else:
			vals[i][w] = curr_v
			return curr_v

	if (w < items[i][0]):
		return getVal(i-1, w, vals, items)
	else:
		val = max([getVal(i-1, w, vals, items), (getVal(i-1, w-items[i][0], vals, items)+items[i][1])])
		vals[i][w] = val
		return val
		

def main():
	(n, k) = map(int, sys.stdin.readline().split())
	items = []
	for _ in range(0, n):
		(w, v) = map(int, sys.stdin.readline().split())
		items.append((w, v))

	vals = [[-1 for _ in range(0, k+1)] for _ in range(0, n)]
	val = getVal(n-1, k, vals, items)
	
	print(val)

if __name__ == "__main__":
	main()
