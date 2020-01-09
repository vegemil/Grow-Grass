import sys

def main():
	chk = [[], []]
	for _ in range(3):
		x, y = map(int, sys.stdin.readline().split())
		if (x in chk[0]):
			chk[0] = list(filter(lambda c: c != x, chk[0]))
		else:
			chk[0].append(x)
		if (y in chk[1]):
			chk[1] = list(filter(lambda c: c != y, chk[1]))
		else:
			chk[1].append(y)

	print(chk[0][0], chk[1][0])

	

main()
