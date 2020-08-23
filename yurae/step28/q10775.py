import sys

def unify(arr, x, y):
	find_x = find(arr, x)
	find_y = find(arr, y)
	if find_x != find_y:
		arr[find_x] = find_y


def find(arr, x):
	if arr[x] != x:
		arr[x] = find(arr, arr[x])
	return arr[x]


def main():
	g = int(sys.stdin.readline())
	p = int(sys.stdin.readline())
	arr = [i for i in range(g+1)]
	occupied = [False for _ in range(g+1)]
	cnt = 0
	for _ in range(p):
		curr = int(sys.stdin.readline())
		while curr > 0:
			if occupied[curr] == False:
				occupied[curr] = True
				cnt += 1
				break
			nxt = find(arr, curr) - 1
			unify(arr, curr, nxt)
			curr = nxt
		if curr == 0:
			break

	print(cnt)
	

if __name__ == "__main__":
	main()	
