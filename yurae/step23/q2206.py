import sys
from collections import deque

def main():
	n, m = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(sys.stdin.readline().split()[0])

	chk = [[[-1, -1] for _ in range(m)] for _ in range(n)]
	chk[0][0] = [1, -1]

	deq = deque([(1, 0, 0, 0)])

	while(deq):
		val, x, y, stat = deq.popleft()
		if x == n-1 and y == m-1:
			print(val)
			return
		if x > 0:
			if arr[x-1][y] == '1' and chk[x-1][y][1] < 0 and stat==0:
				chk[x-1][y][1] = val+1
				deq.append((val+1, x-1, y, 1))
			if arr[x-1][y] == '0' and chk[x-1][y][stat] < 0:
				chk[x-1][y][stat] = val+1
				deq.append((val+1, x-1, y, stat))
		if x < n-1:
			if arr[x+1][y] == '1' and chk[x+1][y][1] < 0 and stat==0:
				chk[x+1][y][1] = val+1
				deq.append((val+1, x+1, y, 1))
			if arr[x+1][y] == '0' and chk[x+1][y][stat] < 0:
				chk[x+1][y][stat] = val+1
				deq.append((val+1, x+1, y, stat))
		if y > 0:
			if arr[x][y-1] == '1' and chk[x][y-1][1] < 0 and stat==0:
				chk[x][y-1][1] = val+1
				deq.append((val+1, x, y-1, 1))
			if arr[x][y-1] == '0' and chk[x][y-1][stat] < 0:
				chk[x][y-1][stat] = val+1
				deq.append((val+1, x, y-1, stat))
		if y < m-1:
			if arr[x][y+1] == '1' and chk[x][y+1][1] < 0 and stat==0:
				chk[x][y+1][1] = val+1
				deq.append((val+1, x, y+1, 1))
			if arr[x][y+1] == '0' and chk[x][y+1][stat] < 0:
				chk[x][y+1][stat] = val+1
				deq.append((val+1, x, y+1, stat))


	print(-1)


if __name__ == "__main__":
	main()
