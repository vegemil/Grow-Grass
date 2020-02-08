import sys

def p(n, chk):
	if (chk[n] < 0):
		chk[n] = p(n-5, chk) + p(n-1, chk)
	return chk[n]

def main():
	t = int(sys.stdin.readline())
	chk = [-1 for _ in range(101)]
	chk[0], chk[1], chk[2], chk[3], chk[4] = 1, 1, 1, 2, 2
	for _ in range(t):
		n = int(sys.stdin.readline())
		print(p(n-1, chk))


if __name__ == "__main__":
	main()
