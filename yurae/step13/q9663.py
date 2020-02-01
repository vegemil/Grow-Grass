import sys

# works in pypy3
def check_board(n, chk, x, y, cnt):
	chk[0][y] = chk[0][y] + cnt
	chk[1][n + x - y] = chk[1][n + x - y] + cnt
	chk[2][x + y] = chk[2][x + y] + cnt
				

def put_board(chk, curr, total):
	if (curr == total):
		return 1

	cnt = 0
	for j in range(0, total):
		i = curr
		if (chk[0][j] > 0 or chk[1][total+i-j] > 0 or chk[2][i+j] > 0):
			continue
		check_board(total, chk, curr, j, 1)
		cnt = cnt + put_board(chk, curr+1, total)
		check_board(total, chk, curr, j, -1)

	return cnt


def main():
	n = int(sys.stdin.readline())

	# row, left_cross, right_cross
	chk = []
	chk.append([0 for i in range(n)])
	chk.append([0 for i in range(n*2)])
	chk.append([0 for i in range(n*2)])

	cnt = 0
	for i in range(n//2):
		check_board(n, chk, 0, i, 1)
		cnt = cnt + put_board(chk, 1, n)
		check_board(n, chk, 0, i, -1)
	cnt = cnt*2

	if (n%2 != 0):
		i = n//2
		check_board(n, chk, 0, i, 1)
		cnt = cnt + put_board(chk, 1, n)
		check_board(n, chk, 0, i, -1)

	print(cnt)


if __name__ == "__main__":
	main()

