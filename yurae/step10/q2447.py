def stars(n, line):
	if (n == 3):
		if (line == 1):
			return "* *"
		else:
			return "***"
	else:
		nxt = n//3
		if (line < nxt):
			return 3 * stars(nxt, line)
		elif (line >= nxt and line < 2*nxt):
			return stars(nxt, line - nxt) + " " * nxt + stars(nxt, line - nxt)
		else:
			return (3 * stars(nxt, line - 2*nxt))


def main():
	n = int(input())
	for l in range(n):
		print(stars(n, l))


if __name__ == "__main__":
	main()
